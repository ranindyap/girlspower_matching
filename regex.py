import re

s = """
Ini dia rangkaian acara MAKERFEST Padang, Besok, 21 April 2018 Di sini kamu bisa membeli produk kreasi terbaik, me… https://t.co/R3M8SMvZPY$Dapetin diskon 10 kalau kamu belanja pakai kartu kredit dan debit BTN Cek promonya di sini… https://t.co/O4CFtwESmj$Sepatu ini udah hadir loh di Indonesia.Yuk #BlibliSekarang Sepatu Under Armour Curry 4 yang super cool ini di… https://t.co/BW9ilkDP3y$Keren banget kan sepatu Under Armour Curry 4 ini. eitss, masih banyak loh keunggulan lainnya. Baca selengkapnya yuk… https://t.co/163waSOIEC$Kelebihan lain dari sepatu ini yaitu menggunakan motif spiral yang dapat menjaga fleksibilitas dan kestabilan kamu… https://t.co/LvKcmbyhRc$Hi @nabilah_afro, selamat ya kamu satu pemenang #GameWeek2. Mohon kirim data diri ke DM, ditunggu selambat-lambatny… https://t.co/B6XqByHBrO$Under Armour Curry 4 juga memiliki kemampuan one-to-one fit sehingga saat digunakan akan menyesuaikan ukuran dan be… https://t.co/CxSsUg87Eu$Stephen Curry terkenal karena kelincahannya. Karena itu, Under Armour Curry 4 memiliki Speed & Stabilizer Plate seh… https://t.co/fc2mPOkey3$Siapkan bahan & perlengkapan BBQ, lalu undang keluarga atau teman untuk menikmatinya bersama Agar lebih seru, km j… https://t.co/AU643owgGS$My week on Twitter ??: 2.66K Mentions, 775K Mention Reach, 455 Likes, 538 Retweets, 877 Replies. See yours with… https://t.co/VS5Mohmfv8$Penggemar NBA pasti udah gak asing lagi sama Stephen Curry. Currry bekerjasama dengan Under Armour mengeluarkan ko… https://t.co/GXJeqFdgwc$Saatnya #LZDGameWeek 3 nih Kali ini hadiahnya spesial dari @infinixindo lho Coba tebak kata ini dan menangkan had… https://t.co/bYvMku7prK$Rebut kesempatanmu memenangkan kamera mirrorless Sony Alpha A5100 Ayo cek Instagram Tokopedia atau ikuti kuisnya d… https://t.co/4E6JKfY4U6$Sanken DD-60 Dish Dryer merupakan alat pengering peralatan makan yang efektif membunuh kuman dan jamur. Produk ini… https://t.co/GfuUp7FxqB$Apa judul e-book yang terakhir kamu baca? Share yuk Cari Kindle favoritmu di sini >> https://t.co/B75A3NOZQY https://t.co/IBiCEtJOyJ$Kamu cuma boleh pilih satu Coba share kamu pilih yang mana... Dapatkan voucher restoran favoritmu di… https://t.co/JqjoQ5Mrmh$Weekend besok waktunya wisata kuliner bareng teman Enaknya makan apa ya? Gak perlu pusing Yuk cek voucher makan… https://t.co/7IOAEuIIce$Friends, Yuk tukarkan #BlibliRewards kamu dengan voucher Rp 25.000 dari Chopstix ??. Klik banner ini ya untuk tata c… https://t.co/dnUpeplX5z$Persiapkan untuk segala keperluan dan tampil maksimal setiap saat. Cek rekomendasi beauty & fashion dari Titan Tyra… https://t.co/8fzq5namVt$Dalam memperingati Hari Kartini, Blibli mau kasih kamu EXTRA DISCOUNT 21 untuk semua produk Kesehatan & Kecantikan… https://t.co/vQk4BHh53H$Oreo tampil dengan tampilan lebih tipis nih,Friends. EKSKLUSIF hanya di https://t.co/69vHdYmXvC kamu bisa pesan ORE… https://t.co/FAaGibzV3Q$Saatnya memerdekakan setiap perempuan dari belenggu masalah kebersihan & kecantikan Buktikan emansipasi cantikmu d… https://t.co/Dcq0hIqyUM$Happy Friday, Friends Belanja Paket Dove Natural Shampoo di https://t.co/69vHdYmXvC kamu bisa dapet FREE POUCH luc… https://t.co/332uHFktNC$Meninjau pameran Indonesia International Motor Show 2018 di JI-Expo, Kemayoran, Jakarta. Majulah industri otomotif… https://t.co/pNU6QZyFC0 Ini dia rangkaian acara MAKERFEST Padang, Besok, 21 April 2018 Di sini kamu bisa membeli produk kreasi terbaik, me… https://t.co/R3M8SMvZPY Dapetin diskon 10 kalau kamu belanja pakai kartu kredit dan debit BTN Cek promonya di sini… https://t.co/O4CFtwESmj Sepatu ini udah hadir loh di Indonesia.Yuk #BlibliSekarang Sepatu Under Armour Curry 4 yang super cool ini di… https://t.co/BW9ilkDP3y Keren banget kan sepatu Under Armour Curry 4 ini. eitss, masih banyak loh keunggulan lainnya. Baca selengkapnya yuk… https://t.co/163waSOIEC Kelebihan lain dari sepatu ini yaitu menggunakan motif spiral yang dapat menjaga fleksibilitas dan kestabilan kamu… https://t.co/LvKcmbyhRc Hi @nabilah_afro, selamat ya kamu satu pemenang #GameWeek2. Mohon kirim data diri ke DM, ditunggu selambat-lambatny… https://t.co/B6XqByHBrO Under Armour Curry 4 juga memiliki kemampuan one-to-one fit sehingga saat digunakan akan menyesuaikan ukuran dan be… https://t.co/CxSsUg87Eu Stephen Curry terkenal karena kelincahannya. Karena itu, Under Armour Curry 4 memiliki Speed & Stabilizer Plate seh… https://t.co/fc2mPOkey3 Siapkan bahan & perlengkapan BBQ, lalu undang keluarga atau teman untuk menikmatinya bersama Agar lebih seru, km j… https://t.co/AU643owgGS My week on Twitter ??: 2.66K Mentions, 775K Mention Reach, 455 Likes, 538 Retweets, 877 Replies. See yours with… https://t.co/VS5Mohmfv8 Penggemar NBA pasti udah gak asing lagi sama Stephen Curry. Currry bekerjasama dengan Under Armour mengeluarkan ko… https://t.co/GXJeqFdgwc Saatnya #LZDGameWeek 3 nih Kali ini hadiahnya spesial dari @infinixindo lho Coba tebak kata ini dan menangkan had… https://t.co/bYvMku7prK Rebut kesempatanmu memenangkan kamera mirrorless Sony Alpha A5100 Ayo cek Instagram Tokopedia atau ikuti kuisnya d… https://t.co/4E6JKfY4U6 Sanken DD-60 Dish Dryer merupakan alat pengering peralatan makan yang efektif membunuh kuman dan jamur. Produk ini… https://t.co/GfuUp7FxqB Apa judul e-book yang terakhir kamu baca? Share yuk Cari Kindle favoritmu di sini >> https://t.co/B75A3NOZQY https://t.co/IBiCEtJOyJ Kamu cuma boleh pilih satu Coba share kamu pilih yang mana... Dapatkan voucher restoran favoritmu di… https://t.co/JqjoQ5Mrmh Weekend besok waktunya wisata kuliner bareng teman Enaknya makan apa ya? Gak perlu pusing Yuk cek voucher makan… https://t.co/7IOAEuIIce Friends, Yuk tukarkan #BlibliRewards kamu dengan voucher Rp 25.000 dari Chopstix ??. Klik banner ini ya untuk tata c… https://t.co/dnUpeplX5z Persiapkan untuk segala keperluan dan tampil maksimal setiap saat. Cek rekomendasi beauty & fashion dari Titan Tyra… https://t.co/8fzq5namVt Dalam memperingati Hari Kartini, Blibli mau kasih kamu EXTRA DISCOUNT 21 untuk semua produk Kesehatan & Kecantikan… https://t.co/vQk4BHh53H Oreo tampil dengan tampilan lebih tipis nih,Friends. EKSKLUSIF hanya di https://t.co/69vHdYmXvC kamu bisa pesan ORE… https://t.co/FAaGibzV3Q Saatnya memerdekakan setiap perempuan dari belenggu masalah kebersihan & kecantikan Buktikan emansipasi cantikmu d… https://t.co/Dcq0hIqyUM Happy Friday, Friends Belanja Paket Dove Natural Shampoo di https://t.co/69vHdYmXvC kamu bisa dapet FREE POUCH luc… https://t.co/332uHFktNC Meninjau pameran Indonesia International Motor Show 2018 di JI-Expo, Kemayoran, Jakarta. Majulah industri otomotif… https://t.co/pNU6QZyFC0
"""

pat1 = "i'm"
pat2 = "your"
pat = 'Puteri Indonesia Intelegensia 2020'

def regex_search(pattern, sentence):
    pat = '\w+' + pattern + '\w+'
    match = re.search(pattern, sentence)
    if match:
        print('found', pattern)

def regex_findall(pattern, sentence):
    match = re.findall(pattern, sentence)
    count = 0
    for mat in match:
        count += 1
        print('find all',pattern)
    print(count)

regex_search(pat1, s)
regex_search(pat2, s)
regex_search(pat, s)
regex_findall('spam', s)
