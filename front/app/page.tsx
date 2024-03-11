'use client';
import axios from 'axios';
import Image from 'next/image';
import { useEffect, useState } from 'react';
import SurahCard from '@/components/SurahCard';
import Header from '@/components/Header';

export default function Home() {
  const [data, setData] = useState<any>([]);
  const [error, setError] = useState<any>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          `https://optionally-sweeping-mouse.ngrok-free.app/api/kg/surahs`
        );
        // need to parse json
        // const parsed_data = JSON.parse(response.data);
        setData(response.data);
      } catch (error) {
        setError(error);
      }
    };
    fetchData();
  }, []);

  if (error) return <pre>{JSON.stringify(error, null, 2)}</pre>;

  return (
    <div className="min-h-screen h-full w-full flex flex-col items-center pb-10">
      <Header title={'Ыйык Куран'} />
      <div className="w-[85%] max-md:w-[65%] max-sm:w-[90%] flex flex-col gap-2 items-center">
        <SurahCard title={'Сүрөлөр'} center={true} />
        <div className="w-full grid grid-cols-3 max-lg:grid-cols-2 max-md:grid-cols-1 place-items-center gap-2">
          {data.map(
            (
              item: {
                id: string;
                no: number;
                name: string;
                meaning: string;
              },
              index: number
            ) => {
              return (
                <SurahCard
                  name={item.id}
                  no={item.no}
                  key={index}
                  number={item.no}
                  title={item.name}
                  titleTranslation={item.meaning}
                  center={false}
                />
              );
            }
          )}
        </div>
      </div>
    </div>
  );
}
