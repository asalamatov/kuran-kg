import type { Metadata } from 'next';
import {
  Inter,
  Noto_Sans,
  Noto_Naskh_Arabic,
} from 'next/font/google';
import local from 'next/font/local';
import './globals.css';

// const inter = Inter({
//   subsets: ['latin', 'cyrillic-ext'],
// });

const notoSans = Noto_Sans({
  variable: '--display-font',
  subsets: ['latin', 'cyrillic-ext'],
});

const notoNaskhArabic = Noto_Naskh_Arabic({
  variable: "--arabic-font",
  subsets: ['arabic'],
});

const surahNameFont = local({
  src: [
    {
      path: '../assets/arabic_surah_font.ttf',
      weight: '400',
      style: 'normal',
    },
  ],
  variable: '--surah-name-font',
});

// const uthmanic = local({
//   src: [
//     {
//       path: '../assets/uthmanic_hafs.ttf',
//       weight: '400',
//       style: 'normal',
//     },
//   ],
//   variable: '--uthmanic-font',
// });

export const metadata: Metadata = {
  title: 'Ыйык Куран',
  description:
    'Ыйык Куран. Маанилеринин кыргызча котормосу менен. | Исмаилов Абдышүкүр, Дүйшөн Абдыллаев, Садибакас Доолов, Садык Гавай (Которгондор) | Редактор: Шерназар Шүкүров, Корректор: Куттугалы Закиров. Бишкек, 2006:  604 б.',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="kg">
      <body
        className={`${notoSans.variable} ${surahNameFont.variable} ${notoNaskhArabic.variable}`}
      >
        {children}
      </body>
    </html>
  );
}
