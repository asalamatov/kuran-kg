import axios from 'axios';

const getSurah = async (name: string) => {
  const response = await axios.get(
    `https://optionally-sweeping-mouse.ngrok-free.app/api/kg/quran/${name}`
  );
  console.log(response);
  return JSON.parse(response.data);
};

const getSurahAPI = async (name: string) => {
  console.log('getSurahAPI');
  const response = await axios.get(
    `https://optionally-sweeping-mouse.ngrok-free.app/api/kg/quran/no/${name}`
  );
  console.log(response.data);
  return response.data;
};

export { getSurah, getSurahAPI };
