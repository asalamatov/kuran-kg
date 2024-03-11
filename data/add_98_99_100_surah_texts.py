import json

# file_name = 'SurahTextExported1.json_without_ids.json'

# with open(file_name) as f:
#     data = json.load(f)

# print(type(data))

# text_to_add='''
# 1.        Дүбүрттүү күлүк аттарга ант!
# 2.        (Туйактарынан) от чачыраган (күлүк) аттарга ант!
# 3.        Таңда (казатка) чабуул коюучу аттарга ант!
# 4.        (Ошол күлүк аттар) чаңды обого уюлгутат.
# 5.        Топту жарып ортого кирет.[2]
# 6.        Ырасында, инсан өз Эгесине капырлыгы (менен) чектен ашкан.
# 7.        Буга ал[3] өзү да күбө.
# 8.        Акыйкатта инсандын ырахат-жыргалды жакшы көрүүсү өтө күчтүү.
# 9.        Билишпейби?! Эгерде мүрзөлөрдүн ичиндегилер чыгарылса,
# 10.       Жана да жүрөктөрдөгү (катылган) нерселер ачылса,
# 11.       Аныгында алардын Эгеси ошол күнү тигилер жөнүндө толук кабардар.[4]
# '''



# for dic in data:
#     for k, v in dic.items():
#         if k == 'surah_name' and v == 'adiyat' and len(dic) == 2:
#             dic.append({
#               'text_number': 3,
#               'surah_name': 'adiyat',
#               'ayah_number': 1,
#               'ayah_text': 'Дүбүрттүү күлүк аттарга ант!',
#               'controlled': '0'
#             })
#             dic.append({
#               'text_number': 4,
#               'surah_name': 'adiyat',
#               'ayah_number': 2,
#               'ayah_text': '(Туяктарынан) от чачыраган (күлүк) аттарга ант!',
#               'controlled': '0'
#             })
#             dic.append({
#               'text_number': 5,
#               'surah_name': 'adiyat',
#               'ayah_number': 3,
#               'ayah_text': 'Таңда (казатка) чабуул коюучу аттарга ант!',
#               'controlled': '0'
#             })
#             dic.append({
#               'text_number': 6,
#               'surah_name': 'adiyat',
#               'ayah_number': 4,
#               'ayah_text': '(Ошол күлүк аттар) чаңды обого уюлгутат.',
#               'controlled': '0'
#             })
#             dic.append({
#               'text_number': 7,
#               'surah_name': 'adiyat',
#               'ayah_number': 5,
#               'ayah_text': 'Топту жарып ортого кирет.',
#               'controlled': '0'
#             })
#             dic.append({
#               'text_number': 8,
#               'surah_name': 'adiyat',
#               'ayah_number': 6,
#               'ayah_text': 'Ырасында, инсан өз Эгесине капырлыгы (менен) чектен ашкан.',
#               'controlled': '0'
#             })
#             dic.append({
#               'text_number': 9,
#               'surah_name': 'adiyat',
#               'ayah_number': 7,
#               'ayah_text': 'Буга ал өзү да күбө.',
#               'controlled': '0'
#             })
#             dic.append({
#               'text_number': 10,
#               'surah_name': 'adiyat',
#               'ayah_number': 8,
#               'ayah_text': 'Акыйкатта инсандын ырахат-жыргалды жакшы көрүүсү өтө күчтүү.',
#               'controlled': '0'
#             })
#             dic.append({
#               'text_number': 11,
#               'surah_name': 'adiyat',
#               'ayah_number': 9,
#               'ayah_text': 'Билишпейби?! Эгерде мүрзөлөрдүн ичиндегилер чыгарылса,',
#               'controlled': '0'
#             })
#             dic.append({
#               'text_number': 12,
#               'surah_name': 'adiyat',
#               'ayah_number': 10,
#               'ayah_text': 'Жана да жүрөктөрдөгү (катылган) нерселер ачылса,',
#               'controlled': '0'
#             })
#             dic.append({
#               'text_number': 13,
#               'surah_name': 'adiyat',
#               'ayah_number': 11,
#               'ayah_text': 'Аныгында алардын Эгеси ошол күнү тигилер жөнүндө толук кабардар.',
#               'controlled': '0'
#             })
#             break

# for dic in data:
#     for k, v in dic.items():
#         if k == 'surah_name' and v == 'adiyat':
#             print(dic)
#             break

# list_to_add = [
#     {
#         'text_number': 13,
#         'surah_name': 'adiyat',
#         'ayah_number': 11,
#         'ayah_text': 'Аныгында алардын Эгеси ошол күнү тигилер жөнүндө толук кабардар.[4]',
#         'controlled': '0'
#     },
#     {
#         'text_number': 12,
#         'surah_name': 'adiyat',
#         'ayah_number': 10,
#         'ayah_text': 'Жана да жүрөктөрдөгү (катылган) нерселер ачылса,',
#         'controlled': '0'
#     },
#     {
#         'text_number': 11,
#         'surah_name': 'adiyat',
#         'ayah_number': 9,
#         'ayah_text': 'Билишпейби?! Эгерде мүрзөлөрдүн ичиндегилер чыгарылса,',
#         'controlled': '0'
#     },
#     {
#         'text_number': 10,
#         'surah_name': 'adiyat',
#         'ayah_number': 8,
#         'ayah_text': 'Акыйкатта инсандын ырахат-жыргалды жакшы көрүүсү өтө күчтүү.',
#         'controlled': '0'
#     },
#     {
#         'text_number': 9,
#         'surah_name': 'adiyat',
#         'ayah_number': 7,
#         'ayah_text': 'Буга ал[3] өзү да күбө.',
#         'controlled': '0'
#     },
#     {
#         'text_number': 8,
#         'surah_name': 'adiyat',
#         'ayah_number': 6,
#         'ayah_text': 'Ырасында, инсан өз Эгесине капырлыгы (менен) чектен ашкан.',
#         'controlled': '0'
#     },
#     {
#         'text_number': 7,
#         'surah_name': 'adiyat',
#         'ayah_number': 5,
#         'ayah_text': 'Топту жарып ортого кирет.[2]',
#         'controlled': '0'
#     },
#     {
#         'text_number': 6,
#         'surah_name': 'adiyat',
#         'ayah_number': 4,
#         'ayah_text': '(Ошол күлүк аттар) чаңды обого уюлгутат.',
#         'controlled': '0'
#     },
#     {
#         'text_number': 5,
#         'surah_name': 'adiyat',
#         'ayah_number': 3,
#         'ayah_text': 'Таңда (казатка) чабуул коюучу аттарга ант!',
#         'controlled': '0'
#     },
#     {
#         'text_number': 4,
#         'surah_name': 'adiyat',
#         'ayah_number': 2,
#         'ayah_text': '(Туяктарынан) от чачыраган (күлүк) аттарга ант!',
#         'controlled': '0'
#     },
#     {
#         'text_number': 3,
#         'surah_name': 'adiyat',
#         'ayah_number': 1,
#         'ayah_text': 'Дүбүрттүү күлүк аттарга ант!',
#         'controlled': '0'
#     },
# ]

# with open('adiyat_addion.json', 'w') as f:
#     json.dump(list_to_add, f, indent=2)


# zalzalah_text = '''
# 1.     Жер силкинип титиреген кезде,
# 2.     Жер өз ичине камтыган (дүнүйө-мүлк жана өлүктөрдү) сыртка чыгарып салган кезде,
# 3.     «Буга[2] эмне болду?»  – деп инсан айткан кезде,
# 4.     Дал ошол Күнү Жер (өзүнүн үстүндө эмне окуйалар болгонун) кабар берип сүйлөйт.
# 5.     Анткени бул сенин Эгеңдин ага[3] берген буйругу.
# 6.     Мына ошол Күнү адамдар өздөрүнүн[4] амалдары көргөзүлүп, топ-топ болуп чыга келишет.
# 7.     Демек, кимде-ким кыпындай жакшы иш кылган болсо аны көрөт,
# 8.     Кимде-ким кыпындай жаман иш кылган болсо аны да көрөт.
# '''

# zalzalah_list_to_add = [
#     {
#         'text_number': 10,
#         'surah_name': 'zalzalah',
#         'ayah_number': 8,
#         'ayah_text': 'Кимде-ким кыпындай жаман иш кылган болсо аны да көрөт.',
#         'controlled': '0'
#     },
#     {
#         'text_number': 9,
#         'surah_name': 'zalzalah',
#         'ayah_number': 7,
#         'ayah_text': 'Демек, кимде-ким кыпындай жакшы иш кылган болсо аны көрөт',
#         'controlled': '0'
#     },
#     {
#         'text_number': 8,
#         'surah_name': 'zalzalah',
#         'ayah_number': 6,
#         'ayah_text': 'Мына ошол Күнү адамдар өздөрүнүн[4] амалдары көргөзүлүп, топ-топ болуп чыга келишет.',
#         'controlled': '0'
#     },
#     {
#         'text_number': 7,
#         'surah_name': 'zalzalah',
#         'ayah_number': 5,
#         'ayah_text': 'Анткени бул сенин Эгеңдин ага[3] берген буйругу.',
#         'controlled': '0'
#     },
#     {
#         'text_number': 6,
#         'surah_name': 'zalzalah',
#         'ayah_number': 4,
#         'ayah_text': 'Дал ошол Күнү Жер (өзүнүн үстүндө эмне окуялар болгонун) кабар берип сүйлөйт.',
#         'controlled': '0'
#     },
#     {
#         'text_number': 5,
#         'surah_name': 'zalzalah',
#         'ayah_number': 3,
#         'ayah_text': '«Буга[2] эмне болду?»  – деп инсан айткан кезде',
#         'controlled': '0'
#     },
#     {
#         'text_number': 4,
#         'surah_name': 'zalzalah',
#         'ayah_number': 2,
#         'ayah_text': 'Жер өз ичине камтыган (дүнүйө-мүлк жана өлүктөрдү) сыртка чыгарып салган кезде',
#         'controlled': '0'
#     },
#     {
#         'text_number': 3,
#         'surah_name': 'zalzalah',
#         'ayah_number': 1,
#         'ayah_text': 'Жер силкинип титиреген кезде',
#         'controlled': '0'
#     }
# ]

# with open('zalzalah_addition.json', 'w') as f:
#     json.dump(zalzalah_list_to_add, f, indent=2)

# bayyinah_text = '''
# 1.     Китеп ээлеринен[2] жана мушриктерден[3] болгон ишенбөөчүлөр өздөрүнө ачык-айкын кабарлар[4] келген кезге чейин, өз жаңылыштыктарынан[5] ажырай алышпады.
# 2.     Алладан келген элчи[6] аларга таза кабарларды окуду (айтып берди).
# 3.     Аларда[7] туура өкүмдөр бар.
# 4.     Китеп ээлеринен болгондор[8] качан гана аларга ачык-айкын кабарлар[9] келген кезге чейин (бир-биринен) ажырашкан жок;
# 5.     Аларга чыныгы динди таза, бекем кармап, бир гана Аллага сыйынууга жана намаз окуп, зекетти (тиешелүү) орундарга берүүгө буйрук кылынды. Мына ушул гана – акыйкат жолунда адамдардын тутунган дини.
# 6.     Акыйкатта, Китеп ээлеринен жана мушриктерден чыккан ишенбөөчүлөр - алар Тозоктун алоолонгон отунда түбөлүккө болушат. Алар - адамдардын эң жаманы.
# 7.     Акыйкатта, ыйман келтирип – Аллага ишенгендер жана жакшылык иштерди кылгандар, алар – адамдардын эң жакшысы.
# 8.     Аларга Жараткан тарабынан төмөн жактарында өзөн-дарыйалар агып турган бейиш бактары түбөлүккө сыйлык үчүн берилет. Алла Таала аларга ыраазы болот жана алар да Аллага ыраазы болушат. Бул[10] өз Жаратканынан корккон такыбалар үчүн гана.

# '''

# bayyinah_list_to_add = [
#     {
#       'text_number': 10,
#       'surah_name': 'bayyinah',
#       'ayah_number': 8,
#       'ayah_text': 'Аларга Жараткан тарабынан төмөн жактарында өзөн-дарыялар агып турган бейиш бактары түбөлүккө сыйлык үчүн берилет. Алла Таала аларга ыраазы болот жана алар да Аллага ыраазы болушат. Бул[10] өз Жаратканынан корккон такыбалар үчүн гана.',
#       'controlled': '0'
#     },
#     {
#       'text_number': 9,
#       'surah_name': 'bayyinah',
#       'ayah_number': 7,
#       'ayah_text': 'Акыйкатта, ыйман келтирип – Аллага ишенгендер жана жакшылык иштерди кылгандар, алар – адамдардын эң жакшысы.',
#       'controlled': '0'
#     },
#     {
#       'text_number': 8,
#       'surah_name': 'bayyinah',
#       'ayah_number': 6,
#       'ayah_text': 'Акыйкатта, Китеп ээлеринен жана мушриктерден чыккан ишенбөөчүлөр - алар Тозоктун алоолонгон отунда түбөлүккө болушат. Алар - адамдардын эң жаманы.',
#       'controlled': '0'
#     },
#     {
#       'text_number': 7,
#       'surah_name': 'bayyinah',
#       'ayah_number': 5,
#       'ayah_text': 'Аларда[7] туура өкүмдөр бар.',
#       'controlled': '0'
#     },
#     {
#       'text_number': 6,
#       'surah_name': 'bayyinah',
#       'ayah_number': 4,
#       'ayah_text': 'Китеп ээлеринен болгондор[8] качан гана аларга ачык-айкын кабарлар[9] келген кезге чейин (бир-биринен) ажырашкан жок;',
#       'controlled': '0'
#     },
#     {
#       'text_number': 5,
#       'surah_name': 'bayyinah',
#       'ayah_number': 3,
#       'ayah_text': 'Алладан келген элчи[6] аларга таза кабарларды окуду (айтып берди).',
#       'controlled': '0'
#     },
#     {
#       'text_number': 4,
#       'surah_name': 'bayyinah',
#       'ayah_number': 2,
#       'ayah_text': 'Китеп ээлеринен[2] жана мушриктерден[3] болгон ишенбөөчүлөр өздөрүнө ачык-айкын кабарлар[4] келген кезге чейин, өз жаңылыштыктарынан[5] ажырай алышпады.',
#       'controlled': '0'
#     },
#     {
#       'text_number': 3,
#       'surah_name': 'bayyinah',
#       'ayah_number': 1,
#       'ayah_text': 'Китеп ээлеринен[2] жана мушриктерден[3] болгон ишенбөөчүлөр өздөрүнө ачык-айкын кабарлар[4] келген кезге чейин, өз жаңылыштыктарынан[5] ажырай алышпады.',
#       'controlled': '0'
#     }
# ]

# with open('bayyinah_addition.json', 'w') as f:
#     json.dump(bayyinah_list_to_add, f, indent=2)


tur_text = [{'id': 4837, 'text_number': 1, 'surah_name': 'tur', 'ayah_number': 0, 'ayah_text': 'Мээримдүү, Ырайымдуу Алланын аты менен!', 'controlled': '0'}, {'id': 4838, 'text_number': 2, 'surah_name': 'tur', 'ayah_number': 0, 'ayah_text': '1. Тур тоосуна ант!', 'controlled': '0'}, {'id': 4839, 'text_number': 3, 'surah_name': 'tur', 'ayah_number': 1, 'ayah_text': 'Жана жазылган Китепке ант!', 'controlled': '0'}, {'id': 4840, 'text_number': 4, 'surah_name': 'tur', 'ayah_number': 2, 'ayah_text': 'Териге жазылганга ант!', 'controlled': '0'}, {'id': 4841, 'text_number': 5, 'surah_name': 'tur', 'ayah_number': 3, 'ayah_text': 'Т ургузулган ү йгө[3] ант!', 'controlled': '0'}, {'id': 4842, 'text_number': 6, 'surah_name': 'tur', 'ayah_number': 4, 'ayah_text': 'Көтөрүлгөн шыпка[4] ант!.', 'controlled': '0'}, {'id': 4843, 'text_number': 7, 'surah_name': 'tur', 'ayah_number': 5, 'ayah_text': 'Жагылган деңизге[5] ант!', 'controlled': '0'}, {'id': 4844, 'text_number': 8, 'surah_name': 'tur', 'ayah_number': 6, 'ayah_text': 'Чындыгында Эгеңдин азабы орундалат.', 'controlled': '0'}, {'id': 4845, 'text_number': 9, 'surah_name': 'tur', 'ayah_number': 7, 'ayah_text': 'Аны токтотуучу (күч) жок!', 'controlled': '0'}, {'id': 4846, 'text_number': 10, 'surah_name': 'tur', 'ayah_number': 8, 'ayah_text': 'Ал Күнү асман катуу силкинет.', 'controlled': '0'}, {'id': 4847, 'text_number': 11, 'surah_name': 'tur', 'ayah_number': 9, 'ayah_text': 'Тоолор ордунан жылат[7].', 'controlled': '0'}, {'id': 4848, 'text_number': 12, 'surah_name': 'tur', 'ayah_number': 10, 'ayah_text': 'Акыйкатты жалган дегендерге ал Күнү азап ( болсун )!', 'controlled': '0'}, {'id': 4849, 'text_number': 13, 'surah_name': 'tur', 'ayah_number': 11, 'ayah_text': 'Алар бузуктукка чумкуп, оюн кылышкан.', 'controlled': '0'}, {'id': 4850, 'text_number': 14, 'surah_name': 'tur', 'ayah_number': 12, 'ayah_text': 'Ал Күнү алар Тозокко айдалышат', 'controlled': '0'}, {'id': 4851, 'text_number': 15, 'surah_name': 'tur', 'ayah_number': 13, 'ayah_text': '“Мына, силер жалган деген От!” (деп айтылат).', 'controlled': '0'}, {'id': 4852, 'text_number': 16, 'surah_name': 'tur', 'ayah_number': 14, 'ayah_text': 'Бул силерге сыйкырбы , же көрбөйсүңөрбү[10]?', 'controlled': '0'}, {'id': 4853, 'text_number': 17, 'surah_name': 'tur', 'ayah_number': 15, 'ayah_text': 'Тозокко күйгүлө! Чыдасаңар да, чыдабасаңар да - силерге баары бир (эмеспи). Албетте, жасаган иш-амалыңардын жазасын гана тартасыңар!', 'controlled': '0'}, {'id': 4854, 'text_number': 18, 'surah_name': 'tur', 'ayah_number': 16, 'ayah_text': 'Чындыгында, такыбалар бакчаларда[11] жана ырахатта (болушат).', 'controlled': '0'}, {'id': 4855, 'text_number': 19, 'surah_name': 'tur', 'ayah_number': 17, 'ayah_text': '(Алар) Эгеси берген жакшылыктын даамын татышат. Аларды Эгеси Тозок отунан сактайт.', 'controlled': '0'}, {'id': 4856, 'text_number': 20, 'surah_name': 'tur', 'ayah_number': 18, 'ayah_text': 'Жасаган жакшы амалдарыңар[12] себептүү : «Жегиле жана ичкиле, (тамагыңар) татуу болсун!»', 'controlled': '0'}, {'id': 4857, 'text_number': 21, 'surah_name': 'tur', 'ayah_number': 19, 'ayah_text': 'Тизилген мамыктарда жөлөнгөн абалда (олтуруп)». Биз аларды кара көз үр кыздарга үйлөндүрөбүз.', 'controlled': '0'}, {'id': 4858, 'text_number': 22, 'surah_name': 'tur', 'ayah_number': 20, 'ayah_text': 'Ыйман келтиргендердин урпактары да ыйман келтирип, аларды ээрчишсе, аларды ошол урпактарына кошобуз. Биз алардын амалдарын[13] кымындай да азайтпайбыз. Ар ким өзү жасаган иш үчүн күрөөгө коюлган.', 'controlled': '0'}, {'id': 4859, 'text_number': 23, 'surah_name': 'tur', 'ayah_number': 21, 'ayah_text': 'Биз аларга өздөрү каалагандай жемиш менен этти мол беребиз.', 'controlled': '0'}, {'id': 4860, 'text_number': 24, 'surah_name': 'tur', 'ayah_number': 22, 'ayah_text': 'Алар бири-бирине суусундуктарды сунушат. Ал жерде[14] пайдасыз жана күнөөлүү сөз сүйлөнбөйт.', 'controlled': '0'}, {'id': 4861, 'text_number': 25, 'surah_name': 'tur', 'ayah_number': 23, 'ayah_text': 'Аларга тизилген бермет сыяктуу жигиттер айланып, кызмат кылышат.', 'controlled': '0'}, {'id': 4862, 'text_number': 26, 'surah_name': 'tur', 'ayah_number': 24, 'ayah_text': 'Алар бетме-бет (олтуруп) бири-биринен сурашат:', 'controlled': '0'}, {'id': 4863, 'text_number': 27, 'surah_name': 'tur', 'ayah_number': 25, 'ayah_text': '«Чындыгында, биз мурда үй бүлөлөрүбүз менен чогуу коркчу элек[15],', 'controlled': '0'}, {'id': 4864, 'text_number': 28, 'surah_name': 'tur', 'ayah_number': 26, 'ayah_text': 'Ошондуктан Алла бизди ийгиликке жеткирип, заардуу азаптан сактады.', 'controlled': '0'}, {'id': 4865, 'text_number': 29, 'surah_name': 'tur', 'ayah_number': 27, 'ayah_text': 'Биз мурда ага жалбарчу элек. Анткени Ал[16] - Жакшылык кылууч у , Ырайымдуу» .', 'controlled': '0'}, {'id': 4866, 'text_number': 30, 'surah_name': 'tur', 'ayah_number': 28, 'ayah_text': 'Ошондуктан эскерт[17]. (Анткени) сен[18], Алланын жакшылыгы менен көзү ачык да, жинди да эмессиң[19].', 'controlled': '0'}, {'id': 4867, 'text_number': 31, 'surah_name': 'tur', 'ayah_number': 29, 'ayah_text': 'Же алар: «Ал - бир акын. Ошондуктан ага жаман учурдун келишин күтө туралы[20]!» - дешет.', 'controlled': '0'}, {'id': 4868, 'text_number': 32, 'surah_name': 'tur', 'ayah_number': 30, 'ayah_text': 'Айткын: «Күтө бергиле! Мен да силер менен бирге күтөмүн!»', 'controlled': '0'}, {'id': 4869, 'text_number': 33, 'surah_name': 'tur', 'ayah_number': 31, 'ayah_text': 'Аларды акылы ушул нерсеге буйруп жатабы , же алар чектен ашкан коомбу?', 'controlled': '0'}, {'id': 4870, 'text_number': 34, 'surah_name': 'tur', 'ayah_number': 32, 'ayah_text': 'Же алар: «Аны[21] өзү ойлоп тапкан» - дешеби? Жок! Алар[22] ишенишпейт[23]!', 'controlled': '0'}, {'id': 4871, 'text_number': 35, 'surah_name': 'tur', 'ayah_number': 33, 'ayah_text': 'Эгер алар чындыкты айтып жатышса, ушуга окшош Сөз[24] жаратышсын[25]!', 'controlled': '0'}, {'id': 4872, 'text_number': 36, 'surah_name': 'tur', 'ayah_number': 34, 'ayah_text': 'Алар[26] Жаратуучусуз[27] жаралышканбы , же өздөрү Жар а туучубу?!', 'controlled': '0'}, {'id': 4873, 'text_number': 37, 'surah_name': 'tur', 'ayah_number': 35, 'ayah_text': 'Асмандар менен жерди эмне , алар жаратышканбы?! Жок! Алар[28] ишенишпейт[29]!', 'controlled': '0'}, {'id': 4874, 'text_number': 38, 'surah_name': 'tur', 'ayah_number': 36, 'ayah_text': 'Же Эгеңдин казыналары алардын карамагындабы? Же алар өкүмдарбы?!', 'controlled': '0'}, {'id': 4875, 'text_number': 39, 'surah_name': 'tur', 'ayah_number': 37, 'ayah_text': 'Же аларда чыгып тыңшоочу[30] шатылары барбы? Андай болсо, алардын тыңшоочулары анык[31] далил келтиришсин!', 'controlled': '0'}, {'id': 4876, 'text_number': 40, 'surah_name': 'tur', 'ayah_number': 38, 'ayah_text': 'Же кыздар Аныкы[32], уулдар - силердикиби[33]?', 'controlled': '0'}, {'id': 4877, 'text_number': 41, 'surah_name': 'tur', 'ayah_number': 39, 'ayah_text': 'Же алардан сен акы сурап жатасыңбы? Анан аларга акы төлөө оор келдиби?!', 'controlled': '0'}, {'id': 4878, 'text_number': 42, 'surah_name': 'tur', 'ayah_number': 40, 'ayah_text': 'Же алардын кайыптан маалыматы бар болуп, алар ошону жазып жатышабы?', 'controlled': '0'}, {'id': 4879, 'text_number': 43, 'surah_name': 'tur', 'ayah_number': 41, 'ayah_text': 'Же алар митайым-куулук кылууну каалашабы? Каапырлар өздөрү - алданып калуучулар.', 'controlled': '0'}, {'id': 4880, 'text_number': 44, 'surah_name': 'tur', 'ayah_number': 42, 'ayah_text': 'Же алардын Алладан башка кудайы барбы?! Алла алар ойлоп тапкан шериктерден Аруу, Таза.', 'controlled': '0'}, {'id': 4881, 'text_number': 45, 'surah_name': 'tur', 'ayah_number': 43, 'ayah_text': 'Эгер асмандын бир бөлүгүнүн кулап баратканын көрүшкөн болсо : « Б ул - булуттардын үймөгү» , - деп айтышмак.', 'controlled': '0'}, {'id': 4882, 'text_number': 46, 'surah_name': 'tur', 'ayah_number': 44, 'ayah_text': 'Алар өздөрү кыйрай турган Кыямат Күнүнө жолукканга чейин жөн жайына кой.', 'controlled': '0'}, {'id': 4883, 'text_number': 47, 'surah_name': 'tur', 'ayah_number': 45, 'ayah_text': 'Кыямат Күнү аларга куулугу эч кандай жардам да бербейт. Аларга жардам да берилбейт.', 'controlled': '0'}, {'id': 4884, 'text_number': 48, 'surah_name': 'tur', 'ayah_number': 46, 'ayah_text': 'Зулумдук кылгандарга[34] мындан да башка азап (бар). Бирок алардын көбү билишпейт[35].', 'controlled': '0'}, {'id': 4885, 'text_number': 49, 'surah_name': 'tur', 'ayah_number': 47, 'ayah_text': 'Эгеңдин өкүмүнө сабыр кыл. Анткени сен Биздин көз алдыбыздасың. Турган[36] учуруңда Эгеңди мактоо менен аруула!', 'controlled': '0'}, {'id': 4886, 'text_number': 50, 'surah_name': 'tur', 'ayah_number': 48, 'ayah_text': 'Аны[37] түндүн бир бөлүгүндө жана жылдыздардын артынан[38] да аруула!', 'controlled': '0'}]


tur_dict = [
    {
    "text_number": 51,
    "surah_name": "tur",
    "ayah_number": 49,
    "ayah_text": "Аны[37] түндүн бир бөлүгүндө жана жылдыздардын артынан[38] да аруула!", "controlled": "0"},
    {
    "text_number": 50,
    "surah_name": "tur",
    "ayah_number": 48,
    "ayah_text": "Эгеңдин өкүмүнө сабыр кыл. Анткени сен Биздин көз алдыбыздасың. Турган[36] учуруңда Эгеңди мактоо менен аруула!", "controlled": "0"},
    {
    "text_number": 49,
    "surah_name": "tur",
    "ayah_number": 47,
    "ayah_text": "Зулумдук кылгандарга[34] мындан да башка азап (бар). Бирок алардын көбү билишпейт[35].", "controlled": "0"},
    {
    "text_number": 48,
    "surah_name": "tur",
    "ayah_number": 46,
    "ayah_text": "Кыямат Күнү аларга куулугу эч кандай жардам да бербейт. Аларга жардам да берилбейт.", "controlled": "0"},
    {
    "text_number": 47,
    "surah_name": "tur",
    "ayah_number": 45,
    "ayah_text": "Алар өздөрү кыйрай турган Кыямат Күнүнө жолукканга чейин жөн жайына кой.", "controlled": "0"},
    {
    "text_number": 46,
    "surah_name": "tur",
    "ayah_number": 44,
    "ayah_text": "Эгер асмандын бир бөлүгүнүн кулап баратканын көрүшкөн болсо : « Б ул - булуттардын үймөгү» , - деп айтышмак.", "controlled": "0"},
    {
    "text_number": 45,
    "surah_name": "tur",
    "ayah_number": 43,
    "ayah_text": "Же алардын Алладан башка кудайы барбы?! Алла алар ойлоп тапкан шериктерден Аруу, Таза.", "controlled": "0"},
    {
    "text_number": 44,
    "surah_name": "tur",
    "ayah_number": 42,
    "ayah_text": "Же алар митайым-куулук кылууну каалашабы? Каапырлар өздөрү - алданып калуучулар.", "controlled": "0"},
    {
    "text_number": 43,
    "surah_name": "tur",
    "ayah_number": 41,
    "ayah_text": "Же алардын кайыптан маалыматы бар болуп, алар ошону жазып жатышабы?", "controlled": "0"},
    {
    "text_number": 42,
    "surah_name": "tur",
    "ayah_number": 40,
    "ayah_text": "Же алардан сен акы сурап жатасыңбы? Анан аларга акы төлөө оор келдиби?!", "controlled": "0"},
    {
    "text_number": 41,
    "surah_name": "tur",
    "ayah_number": 39,
    "ayah_text": "Же кыздар Аныкы[32], уулдар - силердикиби[33]?", "controlled": "0"},
    {
    "text_number": 40,
    "surah_name": "tur",
    "ayah_number": 38,
    "ayah_text": "Же аларда чыгып тыңшоочу[30] шатылары барбы? Андай болсо, алардын тыңшоочулары анык[31] далил келтиришсин!", "controlled": "0"},
    {
    "text_number": 39,
    "surah_name": "tur",
    "ayah_number":37,
    "ayah_text": "Же Эгеңдин казыналары алардын карамагындабы? Же алар өкүмдарбы?!", "controlled": "0"},
    {
    "text_number": 38,
    "surah_name": "tur",
    "ayah_number": 36,
    "ayah_text": "Асмандар менен жерди эмне , алар жаратышканбы?! Жок! Алар[28] ишенишпейт[29]!", "controlled": "0"},
    {
    "text_number": 37,
    "surah_name": "tur",
    "ayah_number": 35,
    "ayah_text": "Алар[26] Жаратуучусуз[27] жаралышканбы , же өздөрү Жар а туучубу?!", "controlled": "0"},
    {
    "text_number": 36,
    "surah_name": "tur",
    "ayah_number": 34,
    "ayah_text": "Эгер алар чындыкты айтып жатышса, ушуга окшош Сөз[24] жаратышсын[25]!", "controlled": "0"},
    {
    "text_number": 35,
    "surah_name": "tur",
    "ayah_number": 33,
    "ayah_text": "Же алар: «Аны[21] өзү ойлоп тапкан» - дешеби? Жок! Алар[22] ишенишпейт[23]!", "controlled": "0"},
    {
    "text_number": 34,
    "surah_name": "tur",
    "ayah_number": 32,
    "ayah_text": "Аларды акылы ушул нерсеге буйруп жатабы , же алар чектен ашкан коомбу?", "controlled": "0"},
    {
    "text_number": 33,
    "surah_name": "tur",
    "ayah_number": 31,
    "ayah_text": "Айткын: «Күтө бергиле! Мен да силер менен бирге күтөмүн!»", "controlled": "0"},
    {
    "text_number": 32,
    "surah_name": "tur",
    "ayah_number": 30,
    "ayah_text": "Же алар: «Ал - бир акын. Ошондуктан ага жаман учурдун келишин күтө туралы[20]!» - дешет.", "controlled": "0"},
    {
    "text_number": 31,
    "surah_name": "tur",
    "ayah_number": 29,
    "ayah_text": "Ошондуктан эскерт[17]. (Анткени) сен[18], Алланын жакшылыгы менен көзү ачык да, жинди да эмессиң[19].", "controlled": "0"},
    {
    "text_number": 30,
    "surah_name": "tur",
    "ayah_number": 28,
    "ayah_text": "Биз мурда ага жалбарчу элек. Анткени Ал[16] - Жакшылык кылууч у , Ырайымдуу» .", "controlled": "0"},
    {
    "text_number": 29,
    "surah_name": "tur",
    "ayah_number": 27,
    "ayah_text": "Ошондуктан Алла бизди ийгиликке жеткирип, заардуу азаптан сактады.", "controlled": "0"},
    {
    "text_number": 28,
    "surah_name": "tur",
    "ayah_number": 26,
    "ayah_text": "«Чындыгында, биз мурда үй бүлөлөрүбүз менен чогуу коркчу элек[15],", "controlled": "0"},
    {
    "text_number": 27,
    "surah_name": "tur",
    "ayah_number": 25,
    "ayah_text": "Алар бетме-бет (олтуруп) бири-биринен сурашат:", "controlled": "0"},
    {
    "text_number": 26,
    "surah_name": "tur",
    "ayah_number": 24,
    "ayah_text": "Аларга тизилген бермет сыяктуу жигиттер айланып, кызмат кылышат.", "controlled": "0"},
    {
    "text_number": 25,
    "surah_name": "tur",
    "ayah_number": 23,
    "ayah_text": "Алар бири-бирине суусундуктарды сунушат. Ал жерде[14] пайдасыз жана күнөөлүү сөз сүйлөнбөйт.", "controlled": "0"},
    {
    "text_number": 24,
    "surah_name": "tur",
    "ayah_number": 22,
    "ayah_text": "Биз аларга өздөрү каалагандай жемиш менен этти мол беребиз.", "controlled": "0"},
    {
    "text_number": 23,
    "surah_name": "tur",
    "ayah_number": 21,
    "ayah_text": "Ыйман келтиргендердин урпактары да ыйман келтирип, аларды ээрчишсе, аларды ошол урпактарына кошобуз. Биз алардын амалдарын[13] кымындай да азайтпайбыз. Ар ким өзү жасаган иш үчүн күрөөгө коюлган.", "controlled": "0"},
    {
    "text_number": 22,
    "surah_name": "tur",
    "ayah_number": 20,
    "ayah_text": "Тизилген мамыктарда жөлөнгөн абалда (олтуруп)». Биз аларды кара көз үр кыздарга үйлөндүрөбүз.", "controlled": "0"},
    {
    "text_number": 21,
    "surah_name": "tur",
    "ayah_number": 19,
    "ayah_text": "Жасаган жакшы амалдарыңар[12] себептүү : «Жегиле жана ичкиле, (тамагыңар) татуу болсун!»", "controlled": "0"},
    {
    "text_number": 20,
    "surah_name": "tur",
    "ayah_number": 18,
    "ayah_text": "(Алар) Эгеси берген жакшылыктын даамын татышат. Аларды Эгеси Тозок отунан сактайт.", "controlled": "0"},
    {
    "text_number": 19,
    "surah_name": "tur",
    "ayah_number": 17,
    "ayah_text": "Чындыгында, такыбалар бакчаларда[11] жана ырахатта (болушат).", "controlled": "0"},
    {
    "text_number": 18,
    "surah_name": "tur",
    "ayah_number": 16,
    "ayah_text": "Тозокко күйгүлө! Чыдасаңар да, чыдабасаңар да - силерге баары бир (эмеспи). Албетте, жасаган иш-амалыңардын жазасын гана тартасыңар!", "controlled": "0"},
    {
    "text_number": 17,
    "surah_name": "tur",
    "ayah_number": 15,
    "ayah_text": "Бул силерге сыйкырбы , же көрбөйсүңөрбү[10]?", "controlled": "0"},
    {
    "text_number": 16,
    "surah_name": "tur",
    "ayah_number": 14,
    "ayah_text": "“Мына, силер жалган деген От!” (деп айтылат).", "controlled": "0"},
    {
    "text_number": 15,
    "surah_name": "tur",
    "ayah_number": 13,
    "ayah_text": "Ал Күнү алар Тозокко айдалышат", "controlled": "0"},
    {
    "text_number": 14,
    "surah_name": "tur",
    "ayah_number": 12,
    "ayah_text": "Алар бузуктукка чумкуп, оюн кылышкан.", "controlled": "0"},
    {
    "text_number": 13,
    "surah_name": "tur",
    "ayah_number": 11,
    "ayah_text": "Акыйкатты жалган дегендерге ал Күнү азап ( болсун )!", "controlled": "0"},
    {
    "text_number": 12,
    "surah_name": "tur",
    "ayah_number": 10,
    "ayah_text": "Тоолор ордунан жылат[7].", "controlled": "0"},
    {
    "text_number": 11,
    "surah_name": "tur",
    "ayah_number": 9,
    "ayah_text": "Ал Күнү асман катуу силкинет.", "controlled": "0"},
    {
    "text_number": 10,
    "surah_name": "tur",
    "ayah_number": 8,
    "ayah_text": "Аны токтотуучу (күч) жок!", "controlled": "0"},
    {
    "text_number": 9,
    "surah_name": "tur",
    "ayah_number": 7,
    "ayah_text": "Чындыгында Эгеңдин азабы орундалат.", "controlled": "0"},
    {
    "text_number": 8,
    "surah_name": "tur",
    "ayah_number": 6,
    "ayah_text": "Жагылган деңизге[5] ант!", "controlled": "0"},
    {
    "text_number": 7,
    "surah_name": "tur",
    "ayah_number": 5,
    "ayah_text": "Көтөрүлгөн шыпка[4] ант!.", "controlled": "0"},
    {
    "text_number": 6,
    "surah_name": "tur",
    "ayah_number": 4,
    "ayah_text": "Т ургузулган ү йгө[3] ант!", "controlled": "0"},
    {
    "text_number": 5,
    "surah_name": "tur",
    "ayah_number": 3,
    "ayah_text": "Териге жазылганга ант!", "controlled": "0"},
    {
    "text_number": 4,
    "surah_name": "tur",
    "ayah_number": 2,
    "ayah_text": "Жана жазылган Китепке ант!", "controlled": "0"},
    {
    "text_number": 3,
    "surah_name": "tur",
    "ayah_number": 1,
    "ayah_text": "1. Тур тоосуна ант!", "controlled": "0"},
    {
    "text_number": 2,
    "surah_name": "tur",
    "ayah_number": 0,
    "ayah_text": "Мээримдүү, Ырайымдуу Алланын аты менен!", "controlled": "0"},
    {
    "text_number": 1,
    "surah_name": "tur",
    "ayah_number": 0,
    "ayah_text": "Меккеде түшүрүлгөн. Кырк тогуз аяттан турат.", "controlled": "0"
    }
]



print(tur_dict)

with open('tur_fixed.json', 'w') as f:
    json.dump(tur_dict, f, indent=2)