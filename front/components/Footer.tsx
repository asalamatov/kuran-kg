import React from 'react';

type Props = {};

const Footer = (props: Props) => {
  return (
    <div className="absolute bottom-0 w-full p-4 bg-gradient-to-r from-[#DF98FA] to-[#9055FF] text-center">
      <h3 className="text-white">
        2023 - {new Date().getFullYear()} © Ыйык Куран
      </h3>
    </div>
  );
};

export default Footer;
