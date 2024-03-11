import React from 'react';

type Props = {};

const Loading = (props: Props) => {
  let circleCommonClasses = 'h-2.5 w-2.5 bg-white rounded-full';

  return (
    <div className="flex flex-col gap-12 w-full bg-gradient-to-r from-[#DF98FA] to-[#9055FF] h-screen items-center justify-center">
      <h1 className="font-bold text-3xl text-white">Жүктөлүүдө...</h1>
      <div className="flex flex-row">
        <div
          className={`${circleCommonClasses} mr-1 animate-bounce`}
        />
        <div
          className={`${circleCommonClasses} mr-1 animate-bounce200`}
        />
        <div className={`${circleCommonClasses} animate-bounce400`} />
      </div>
    </div>
  );
};

export default Loading;
