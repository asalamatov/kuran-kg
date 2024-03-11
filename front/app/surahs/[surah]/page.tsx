'use client';
import { getSurahAPI } from '@/utils/apis';
import axios from 'axios';
import { useRouter } from 'next/navigation';
import { SetStateAction, useEffect, useRef, useState } from 'react';
import { usePathname } from 'next/navigation';
import Header from '@/components/Header';
import Loading from '@/components/Loading';

const Surah = ({ params }: { params: { surah: string } }) => {
  const [data, setData] = useState([]);
  const [error, setError] = useState<any>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const pathname = usePathname();
  const router = useRouter();
  const [surah, setSurah] = useState<string>('');

  const [isPlaying, setIsPlaying] = useState<boolean>(false);
  const audioRef = useRef<HTMLAudioElement>(null);

  const playIcon = (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 20 20"
      fill="#3D3132"
    >
      <path
        fillRule="evenodd"
        d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z"
        clipRule="evenodd"
      />
    </svg>
  );

  const pauseIcon = (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 20 20"
      fill="#3D3132"
    >
      <path
        fillRule="evenodd"
        d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zM7 8a1 1 0 012 0v4a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v4a1 1 0 102 0V8a1 1 0 00-1-1z"
        clipRule="evenodd"
      />
    </svg>
  );

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getSurahAPI(params.surah);
        setData(response);
        setSurah(response[0].surah_name);
        setLoading(false);
      } catch (error) {
        setError(error);
      }
    };
    fetchData();
  }, [params.surah]);

  const toggleAudio = () => {
    if (audioRef.current) {
      if (audioRef.current.paused) {
        audioRef.current.play();
        setIsPlaying(true);
      } else {
        audioRef.current.pause();
        setIsPlaying(false);
      }
    }
  };

  const audioEnded = () => {
    setIsPlaying(false);
  };

  return (
    <>
      {loading ? (
        <Loading />
      ) : (
        <div className="flex flex-col pb-20 gap-2 min-h-screen h-full">
          {/* <div> */}
          <Header title={surah} back={true} />

          {data.map((item: any, index: number) => {
            return (
              <div
                key={index}
                className="bg-white shadow-lg p-4 rounded-lg flex flex-col gap-12"
              >
                {item['arabic_text'] !== '' && (
                  <div className=" font-bold text-3xl text-right tracking-wide leading-[4rem] mx-20 max-md:mx-5">
                    {' '}
                    {/* uthmanic */}
                    <h1>{item['arabic_text']}</h1>
                  </div>
                )}
                <div
                  className={`${
                    index >= 0 &&
                    ` font-light tracking-wide mx-20 max-md:mx-5`
                  }`}
                  style={{
                    // first two children are font-bold
                    fontWeight:
                      item.ayah_number == 0 ? 'bold' : 'light',
                  }}
                >
                  <h1>
                    {item['ayah_number'] > 0 &&
                      item.ayah_number + '. '}
                    {item['ayah_text']}
                  </h1>
                  {item.audio_link && (
                    <audio
                      src={item.audio_link}
                      autoPlay={false}
                      controls
                      onEnded={() => {}}
                      controlsList="nodownload"
                      className=""
                    />
                    // <div className="audio-player">
                    //   <audio
                    //     ref={audioRef}
                    //     src={item.audio_link}
                    //     onEnded={audioEnded}
                    //   />
                    //   <button
                    //     className="player-button"
                    //     onClick={toggleAudio}
                    //   >
                    //     {isPlaying ? pauseIcon : playIcon}
                    //   </button>
                    // </div>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      )}
    </>
  );
};

export default Surah;
