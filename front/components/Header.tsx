'use client';
import { usePathname, useRouter } from 'next/navigation';
import React, { useState } from 'react';
import { IoMdArrowRoundBack } from 'react-icons/io';
import { IoMdArrowRoundForward } from 'react-icons/io';
import { FaBars } from 'react-icons/fa6';

type Props = {};

const Header = ({ title }: { title: string; back?: boolean }) => {
  const router = useRouter();
  const pathname = usePathname();
  const currentRoute: number = parseInt(pathname.split('/')[2]);
  const [dropdownOpen, setDropdownOpen] = useState(false);

  return (
    <div className="w-full p-4 pl-10 mb-4 shadow-lg sticky top-0 bg-gradient-to-r from-[#DF98FA] to-[#9055FF] text-center grid grid-cols-8 place-items-center">
      <div className={title === 'Ыйык Куран' ? 'hidden' : ''}>
        <button
          // className={`${
          //   dropdownOpen
          //     ? 'transform rotate-90 duration-300'
          //     : ' duration-300'
          // } focus:outline-none`}
          // onClick={() => setDropdownOpen((state) => !state)}
          className="text-white"
          onClick={() => {
            router.push('/');
          }}
        >
          {/* <FaBars className="text-white text-2xl" /> */}
          Үй
        </button>
      </div>
      {title !== 'Ыйык Куран' && currentRoute !== 1 && (
        <div className="flex justify-end">
          <button
            onClick={() => {
              if (currentRoute === 1) return router.push('/');
              router.push('/surahs/' + (currentRoute - 1));
            }}
            className="text-white flex flex-row items-center gap-1 hover:scale-105 transition-all duration-300 ease-in-out"
          >
            <IoMdArrowRoundBack />
            {/* {currentRoute === 1
              ? 'Башкы'
              : `${currentRoute - 1}-сүрөгө өтүү`} */}
          </button>
        </div>
      )}
      <div className="flex flex-col gap-4 col-start-3 col-span-4">
        <h1 className="text-2xl text-white font-bold">{title}</h1>
        {/* <h3 className="bismillah text-xl text-white" title="﷽">
          ﷽
        </h3> */}
      </div>
      {title !== 'Ыйык Куран' && currentRoute !== 114 && (
        <div className="flex justify-end">
          <button
            onClick={() => {
              router.push('/surahs/' + (currentRoute + 1));
            }}
            className="text-white flex flex-row items-center gap-1 hover:scale-105 transition-all duration-300 ease-in-out"
          >
            {/* {`${currentRoute + 1}-сүрөгө өтүү`} */}
            <IoMdArrowRoundForward />
          </button>
        </div>
      )}
      <div className="col-start-8 text-white"></div>
    </div>
  );
};

export default Header;
