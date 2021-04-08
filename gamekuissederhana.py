#Ran
#Day
#Hope
#Happy
#Careless
#Susu beruang
#Yang terpenting itu bukan apa yang kita ketahui melainkan apa yang bersedia kita pelajari
'''
==================-----------------------GAME SEDERHANA--------------------------------===============================
Jika terjadi kesalahan dalam hasil game mohon dimaklumi karena masih pemula dan game ini termasuk paling sederhana
game ini masih banyak kekurangan dalam segi apapun, harap dimaklumi ya ^_^
nama file : Gamekuissederhana.py
Nama      : Frans Bachtiar
Asal      : Indonesia
spek      : visual studio code
bhsygdgnkn: Bahasa pemorgraman python
deskripsi : program ini dibuat menggunakan bahasa pemrograman python, game ini dikategorikan game paling sederhana dalam
            pembuatan game ini saya menggunakan function,looping, dan operator aritmatika sehingga menjadilah game ini
            dalam pembuatan ini tentu saya membutuhkan refrensi karena tanpa adanya refrensi seorang programmer handal pun
            akan mengalami kesulitan
=============================================================================================================================
'''
import time
#menu
def menu():
    print("==========================================")
    print("| *SELAMAT DATANG DI GAME KUIS SEDERHANA |")
    print("==========================================")
    print("| [1]. Play                              |")
    print("| [2]. Help                              |")
    print("| [3]. Exit                              |")
    print("==========================================")
    pilihan=input("Masukkan pilihan anda : ")
    print()
    print("Loading....")
    time.sleep(3)
    if pilihan=="1":
        level()
    elif pilihan=="2":
        help()
    elif pilihan=="3":
        exit()
    else:
        print("Keyword yang anda masukkan salah")
#menu level
def level():
    print()
    print("========================================================================================")
    print("                                     JENIS KUIS                                        ")
    print("========================================================================================")
    print(" [1]. Pengetahuan Tentang Python                 |  SELAMAT MENCOBA ""\U0001F917                ")
    print("========================================================================================")
    print(" [2]. Pengetahuan Tentang Bahasa pemorgraman     |  SELAMAT MENCOBA \U0001F917                  ")
    print("========================================================================================")
    print(" [3]. Pengetahuan Tentang Python 2               |  SELAMAT MENCOBA \U0001F917                  ")
    print("========================================================================================")
    e=input("Masukkan pilihan anda : ")
    print("Selamat Berjuang............")
    time.sleep(5)
    if e=="1":
        pertanyaan()
    elif e=="2":
        pertanyaan1()
    elif e=="3":
        pertanyaan2()
    else:
        print("Keyword Yang Anda Masukkan Salah")
#===soal nomor 1
def pertanyaan():
    score=0
    total=12
    print()
    print("===================================")
    print("| SELAMAT BERMAIN SEMOGA TERHIBUR |")
    print("===================================")
    print("1]. Bahasa pemrograman terkenal dengan sintaksnya yang simple, bahasa pemrograman ?")
    print("    a. java                  c. python")
    print("    b. mysql                 d. php")
    print("===============================================================")
    j=input("masukkan jawaban anda : ")
    time.sleep(1)
    if j=="c":
        score += 1
        print("Benar")
        print("=============================================================")
    elif j=="a" or j=="b" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or "Next":
        print("---------------------------------------")
        print("| Masuk Soal Ke 2 Tunggu Ya.......^-^ |")
        print("---------------------------------------")
        time.sleep(2)
    elif p=="stop" or p=="Stop":
        menu()
    else:
        print("ERROR")
#=========soal nomor 2
    print()
    print("=====================================================")
    print("2]. Sintaks python termasuk sintak paling ?")
    print("    a. sulit                    c. tidak masuk akal")
    print("    b. mudah                    d. jawaban salah semua")
    print("=====================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="b":
        score += 1
        print("Benar")
        print("==================================================")
    elif j=="a" or j=="c" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("---------------------------------------")
        print("| Masuk Soal Ke 3 Tunggu Ya.......^_^ |")
        print("---------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 3  
    print()
    print("=========================================================")
    print("3]. Pembuat bahasa pemrograman python adalah ?")
    print("    a. guido van rossum                c. lambert")
    print("    b. mats hummels                    d. rasmus lerdorf")
    print("=========================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="a":
        score += 1
        print("Benar")
        print("==================================================")
    elif j=="b" or j=="c" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("------------------------------------------")
        print("| Masuk Ke Soal Ke 4 Tunggu Ya.......^-^ |")
        print("------------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 4
    print()
    print("=====================================================")
    print("4]. fungsi Looping dalam python untuk ?")
    print("    a. percabangan                   c. fungsi")
    print("    b. pembolakbalik                 d. perulangan")
    print("=====================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="d":
        score += 1
        print("Benar")
        print("==================================================")
    elif j=="a" or j=="c" or j=="b":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("----------------------------------------")
        print("| Masuk Soal Ke 5 Tunggu Ya.......^_^ |")
        print("----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 5
    print()
    print("=====================================================")
    print("5]. fungsi if,elif,dan else dalam python untuk ?")
    print("    a. membuat method             c. pemberi nilai")
    print("    b. percabangan                d. variable ")
    print("=====================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="b":
        score += 1
        print("Benar")
        print("==================================================")
    elif j=="a" or j=="c" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("----------------------------------------")
        print("| Masuk Soal Ke 6 Tunggu Ya....... ^-^ |")
        print("----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 6
    print()
    print("=====================================================")
    print("6]. kata PRINT dalam python berfungsi untuk ?")
    print("    a. menampilkan program     c. hanya penghias")
    print("    b. membaca variable        d. tidak ada fungsi")
    print("=====================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="a":
        score += 1
        print("Benar")
        print("==================================================")
    elif j=="b" or j=="c" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("----------------------------------------")
        print("| Masuk soal ke 7, ayo semangat....^_^ |")
        print("----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 7
    print()
    print("=====================================================")
    print(" 7]. fitur yang dimiliki python ?")
    print("     a. library yang luas         c. membuat aplikasi")
    print("     b. orientasi bergerak        d. sintaks yang berbelit-belit")
    print("=====================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="a":
        score += 1
        print("Benar")
        print("==================================================")
    elif j=="b" or j=="c" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("-----------------------------------------")
        print("| Masuk Soal Ke 8 Semangat Ya.......^-^ |")
        print("-----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 8
    print()
    print("====================================================================")
    print("8]. jika kita ingin menggunakan library python kita menggunakan ?")
    print("    a. class               c. import")
    print("    b. sys                 d. return()")
    print("=====================================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="c":
        score += 1
        print("Benar")
        print("==================================================")
    elif j=="a" or j=="b" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("-----------------------------------------")
        print("| Masuk Soal Ke 9 Semangat Ya.......^_^ |")
        print("-----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 9
    print()
    print("===================================================================")
    print(" 9]. Untuk membuat sebaris komentar pada python menggunakan tanda ?")
    print("     a. #         c. /#")
    print("     b. *         d. //#//")
    print("====================================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="a":
        score += 1
        print("Benar")
        print("==================================================")
    elif j=="b" or j=="c" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("-----------------------------------------")
        print("| Masuk Soal Ke 10 Semangat Ya.......^-^ |")
        print("-----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 10
    print()
    print("=====================================================")
    print(" 10]. Yang bukan kata kunci dalam python adalah ?")
    print("     a. break         c. continue")
    print("     b. return        d. void")
    print("=====================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="d":
        score += 1
        print("Benar")
        print("==================================================")
    elif j=="b" or j=="c" or j=="a":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("-----------------------------------------")
        print("| Masuk Soal Ke 11 Semangat Ya.......^_^ |")
        print("-----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 11
    print()
    print("=====================================================")
    print(" 11]. dictionary dapat dibuat dengan menggunakan tanda ?")
    print("     a. kurung kurawal     c. kurung")
    print("     b. kurung siku        d. tambah")
    print("=====================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="a":
        score += 1
        print("Benar")
        print("==================================================")
    elif j=="b" or j=="c" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("-----------------------------------------")
        print("| Masuk Soal Ke 12 Semangat Ya.......^-^ |")
        print("-----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 12
    print()
    print("====================================================================")
    print("12]. Jika kita ingin menuliskan huruf saja dalam inputan kita, tipe data apakah yang kita gunakan ?")
    print("    a. int             c. str")
    print("    b. main            d. list")
    print("=====================================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="c":
        score += 1
        print("Benar")
        print("==================================================")
    elif j=="a" or j=="b" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    i=input("Apakah ingin melihat score anda (y/t)")
    if i =="y" or i=="Y":
        print("Loading")
        time.sleep(5)
    elif i=="t" or i=="t":
        menu()
    else:
        print("Not found")
#menghitung hasil akhir point
    print()
    print("--------------------------------------------------------------------------------------")
    print("Terimakasih telah memainkan game ini, kamu menjawab",score,"pertanyaan dengan benar")
    akhir=(score/total)*100
    print("score kamu adalah: ",akhir)
    print("---------------------------------------------------------------------------------------")
    i=input("Apakah ingin kembali ke menu awal(y/t)? ")
    if i=="y" or i=="Y":
        menu()
    elif i=="t" or i=="T":
        exit()
    else:
        print("Nout found")
#-----------------------------------------------------------------------------------------------
def help():
    print("---------//---------------------NO COPYRIGHT-----------------//-----------------------//----------------------/2021/----------------------/-------")
    i = 1
    while i<110:
        print('#$game sederhana  #$hanya untuk bersenang-senang #$masih pemula  #$diciptakan hanya karena ingin mengasah kemampuan  2021 2021 by  by ran ran ran', end=" ")
        i = i+1
    print()
    print("================================-------------------------Cara bermain----------------------------------=================================")
    print("| 1. Ikuti game kuis sampai selesai                                                                                                    |")
    print("| 2. Pilihlah jawaban yang sekiranya menurut anda paling benar                                                                         |")
    print("| 3. Untuk menjawab soal pilih antara a b c dan d                                                                                      |")
    print("| 4. Jika ingin melanjutkan ke soal berikutnya tinggal klik Next                                                                       |")
    print("| 5. Jika sudah mengklik next kamu akan ke seoal berikutnya dan tunggu 2 detik untuk ke soal berikutnya                                |")
    print("| 6. Jika ingin melihat score yang dicapai cukup mengklik tombol y dan jika tidak ingin melihat score pilih T                          |")
    print("| 7. Jika sudah melakukan permainan dan ingin kembali ke halaman depan klik y untuk kembali kehalaman depan                            |")
    print("| 8. Soal game ini termasuk random yang di input user sendiri                                                                          |")
    print("| 9. play untuk memulai game dan help untuk mengetahui petunjuk dan exit untuk keluar                                                  |")
    print("| 10.enjoy game                                                                                                                        |")
    print("=====2021=============2021============2021===========2021===========2021========2021============2021===========2021=======2021==========")
    time.sleep(10)
    i = 1
    while i<100:
        print("2021 ... developer.... by .... ran ... 2021 ... develover ... by ... ran ... 2021 ... developer ... by ... ran", end="")
        i=i+1
    print()
    i=input("Kembali ke halaman depan ? ")
    if i=="y" or i=="Y":
        menu()
    elif i=="t" or i=="T":
        exit()
    else:
        print("Wrong")

def pertanyaan1():
    nilaiawl=0
    nilaiakhir=10
    print("===================================")
    print("| SELAMAT BERMAIN SEMOGA TERHIBUR |")
    print("===================================")
    print("1]. Bahasa pemorgraman tingkat kesulitanya menengah ke atas adalah ?")
    print("    a. python                  c.myql")
    print("    b. java                    d.html")
    print("====================================================================")
    i=input("masukkan jawaban anda : ")
    time.sleep(1)
    if i=="b":
        nilaiawl+=1
        print("Benar")
    elif i=="a" or i=="c" or i=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak di temukkan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("-----------------------------------------")
        print("| Masuk Soal Ke 2 Semangat Ya.......^_^ |")
        print("-----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#============soal nomor 2
    print()
    print("==========================================================================")
    print("2]. sintaks bahasa pemrograman java hampir sama dengan bahasa pemorgraman?")
    print("    a. laravel                 c. c++")
    print("    b. ruby                    d. javascript")
    print("===========================================================================")
    j=input("masukkan jawaban anda: ")
    time,time.sleep(1)
    if j=="c":
        nilaiawl+= 1
        print("Benar")
        print("==================================================")
    elif j=="a" or j=="b" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("---------------------------------------")
        print("| Masuk Soal Ke 3 Tunggu Ya.......^_^ |")
        print("---------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#======soal nomor 3
    print()
    print("=========================================================")
    print("3]. Apakah HTML termasuk bahasa pemrograman?")
    print("    a. iya              c. semua salah")
    print("    b. mungkin          d. tidak")
    print("=========================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="d":
        nilaiawl += 1
        print("Benar")
        print("==================================================")
    elif j=="b" or j=="c" or j=="a":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("------------------------------------------")
        print("| Masuk Ke Soal Ke 4 Tunggu Ya.......^-^ |")
        print("------------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 4
    print()
    print("=====================================================")
    print("4]. pencipta bahasa pemrograman c++ ?")
    print("    a. nick numberg           c. bjarne stroustrup")
    print("    b. careless               d. benjamin pavard")
    print("=====================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="c":
        nilaiawl+= 1
        print("Benar")
        print("==================================================")
    elif j=="a" or j=="d" or j=="b":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("----------------------------------------")
        print("| Masuk Soal Ke 5 Tunggu Ya.......^_^ |")
        print("----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#==soal nomor 5
    print()
    print("=====================================================")
    print("5]. bahasa pemrograman yang sering disebut database adalah ?")
    print("    a. mysql            c. python")
    print("    b. c++              d. c")
    print("=====================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="a":
        nilaiawl += 1
        print("Benar")
        print("==================================================")
    elif j=="b" or j=="c" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("----------------------------------------")
        print("| Masuk Soal Ke 6 Tunggu Ya....... ^-^ |")
        print("----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 6
    print()
    print("=====================================================")
    print("6]. siapa pembuat bahasa pemrograman java ?")
    print("    a. james milgagd    c. james stdfgr")
    print("    b. james milner     d. james gosling")
    print("=====================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="d":
        nilaiawl += 1
        print("Benar")
        print("==================================================")
    elif j=="b" or j=="c" or j=="a":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("----------------------------------------")
        print("| Masuk soal ke 7, ayo semangat....^_^ |")
        print("----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 7
    print()
    print("=====================================================")
    print(" 7]. tipe data pada mysql?")
    print("     a. lib-dict-base       c. fun-void-char")
    print("     b. numerik-blob-str    d. var-include-steam")
    print("=====================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="b":
        nilaiawl+= 1
        print("Benar")
        print("==================================================")
    elif j=="a" or j=="c" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("-----------------------------------------")
        print("| Masuk Soal Ke 8 Semangat Ya.......^-^ |")
        print("-----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 8
    print()
    print("====================================================================")
    print("8].bahasa pemrograman laravel terkenal dengan ?")
    print("    a. perulangan yang tanpa henti      c. berbasis teknologi kekinian")
    print("    b. open source framework            d. koneksi yang sangat aman")
    print("=====================================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="b":
        nilaiawl += 1
        print("Benar")
        print("==================================================")
    elif j=="a" or j=="c" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("-----------------------------------------")
        print("| Masuk Soal Ke 9 Semangat Ya.......^_^ |")
        print("-----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 9
    print()
    print("====================================================================")
    print("9]. Dalam bahasa pemrograman C++ void itu adalah ?")
    print("    a. fungsi           c. looping")
    print("    b. return           d. main")
    print("=====================================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="a":
        nilaiawl += 1
        print("Benar")
        print("==================================================")
    elif j=="b" or j=="c" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("-----------------------------------------")
        print("| Masuk Soal Ke 10 Semangat Ya.......^_^ |")
        print("-----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 10
    print()
    print("===================================================================")
    print(" 10]. Dalam program web ada yang namanya front-end pasangan front-end adalah ?")
    print("     a. black-end          c. center-end")
    print("     b. fermous-end        d. back-end")
    print("====================================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="d":
        nilaiawl += 1
        print("Benar")
        print("==================================================")
    elif j=="b" or j=="c" or j=="a":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    i=input("Apakah ingin melihat score anda (y/t)")
    if i =="y" or i=="Y":
        print("Loading")
        time.sleep(5)
    elif i=="t" or i=="t":
        menu()
    else:
        print("Not found")
#menghitung hasil akhir point
    print()
    print("--------------------------------------------------------------------------------------")
    print("Terimakasih telah memainkan game ini, kamu menjawab",nilaiawl,"pertanyaan dengan benar")
    akhir=(nilaiawl/nilaiakhir)*100
    print("score kamu adalah: ",akhir)
    print("---------------------------------------------------------------------------------------")
    i=input("Apakah ingin kembali ke menu awal(y/t)? ")
    if i=="y" or i=="Y":
        menu()
    elif i=="t" or i=="T":
        exit()
    else:
        print("Nout found")
#menugame3
def pertanyaan2():
    mula=0
    iyo=10
    print("===================================")
    print("| SELAMAT BERMAIN SEMOGA TERHIBUR |")
    print("===================================")
    print("1]. i= 1")
    print("    while i<100")
    print("  Jika di Run apa yang terjadi dengan programnya ?")
    print("    a. mutar-mutar tidak jelas    c.Program berjalan dengan baik")
    print("    b. mengalami error            d.Program tidak dapat berhenti")
    print("====================================================================")
    i=input("masukkan jawaban anda : ")
    time.sleep(1)
    if i=="d":
        mula+=1
        print("Benar")
    elif i=="a" or i=="c" or i=="b":
        print("Salah")
    else:
        print("Jawaban anda tidak di temukkan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("-----------------------------------------")
        print("| Masuk Soal Ke 2 Semangat Ya.......^_^ |")
        print("-----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#============soal nomor 2
    print()
    print("==========================================================================")
    print("2]. i=[Aku,suka,dia,tapi,dia,suka,orang,lain")
    print("    print(i[8]")
    print("    jika di run apa yang terjadi dengan programnya ? ")
    print("    a. Error                  c. orang,lain")
    print("    b. lain                   d. tapi")
    print("===========================================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="a":
        mula+= 1
        print("Benar")
        print("==================================================")
    elif j=="b" or j=="c" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("---------------------------------------")
        print("| Masuk Soal Ke 3 Tunggu Ya.......^_^ |")
        print("---------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#======soal nomor 3
    print()
    print("=========================================================")
    print("3].x=[[2,3],[4,5]]")
    print("   print(sum(x,[]))")
    print("   output ?")
    print("    a. error     c. [2,3,4,5]")
    print("    b. 14        d. [5,9]")
    print("=========================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="c":
        mula += 1
        print("Benar")
        print("==================================================")
    elif j=="b" or j=="d" or j=="a":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("------------------------------------------")
        print("| Masuk Ke Soal Ke 4 Tunggu Ya.......^-^ |")
        print("------------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 4
    print()
    print("=====================================================")
    print("4]. print(2**3**2*5)")
    print("    output ? ")
    print("    a. 2267           c. 3675")
    print("    b. 2560           d. 228")
    print("=====================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="b":
        mula+= 1
        print("Benar")
        print("==================================================")
    elif j=="a" or j=="d" or j=="c":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("----------------------------------------")
        print("| Masuk Soal Ke 5 Tunggu Ya.......^_^ |")
        print("----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#==soal nomor 5
    print()
    print("=====================================================")
    print("5]. print(type(0xFF))?")
    print("   jika di run maka type diatas adalah ? ")
    print("    a. hex            c. number")
    print("    b. fri            d. int")
    print("=====================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="d":
        mula += 1
        print("Benar")
        print("==================================================")
    elif j=="b" or j=="c" or j=="a":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("----------------------------------------")
        print("| Masuk Soal Ke 6 Tunggu Ya....... ^-^ |")
        print("----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 6
    print()
    print("=====================================================")
    print("6]. a=[1,2,3]")
    print("    print(a==a[:])")
    print("    output ?")
    print("    a. True     c. None")
    print("    b. False    d. Error")
    print("=====================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="a":
        mula += 1
        print("Benar")
        print("==================================================")
    elif j=="b" or j=="c" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("----------------------------------------")
        print("| Masuk soal ke 7, ayo semangat....^_^ |")
        print("----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 7
    print()
    print("=====================================================")
    print(" 7]. l=[1,2]")
    print("     print(l*2)")
    print("    Output dari hasil diatas adalah ? ")
    print("     a. [1,4]       c. [2,1]")
    print("     b. [1,2,1,2]   d. [2,1,1,2")
    print("=====================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="b":
        mula+= 1
        print("Benar")
        print("==================================================")
    elif j=="a" or j=="c" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("-----------------------------------------")
        print("| Masuk Soal Ke 8 Semangat Ya.......^-^ |")
        print("-----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 8
    print()
    print("====================================================================")
    print("8]. print(round(-0.5))?")
    print("    menghasilkan angka ?")
    print("    a. 6              c. -0.5")
    print("    b. 0,1            d. 0")
    print("=====================================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="d":
        mula += 1
        print("Benar")
        print("==================================================")
    elif j=="a" or j=="c" or j=="b":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("-----------------------------------------")
        print("| Masuk Soal Ke 9 Semangat Ya.......^_^ |")
        print("-----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 9
    print()
    print("====================================================================")
    print("9]. k=[j for j in range(3)]")
    print("    print(k)")
    print("    output program ?")
    print("    a. error          c. 1 2 3")
    print("    b. 0 1 2          d. none")
    print("=====================================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="b":
        mula += 1
        print("Benar")
        print("==================================================")
    elif j=="a" or j=="c" or j=="d":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    p=input("(next/stop) : ")
    if p=="next" or p=="Next":
        print("-----------------------------------------")
        print("| Masuk Soal Ke 10 Semangat Ya.......^_^ |")
        print("-----------------------------------------")
        time.sleep(2)
    elif p=="Stop" or "stop":
        menu()
    else:
        print("ERROR")
#soal nomor 10
    print()
    print("===================================================================")
    print(" 10]. false=true ?")
    print("      while false: ")
    print("             print('True') ")
    print("      output program ? ")
    print("     a. syntax error        c. none")
    print("     b. infinite loop       d. above")
    print("====================================================================")
    j=input("masukkan jawaban anda: ")
    time.sleep(1)
    if j=="b":
        mula += 1
        print("Benar")
        print("==================================================")
    elif j=="d" or j=="c" or j=="a":
        print("Salah")
    else:
        print("Jawaban anda tidak ditemukan")
    print()
    i=input("Apakah ingin melihat score anda (y/t)")
    if i =="y" or i=="Y":
        print("Loading")
        time.sleep(5)
    elif i=="t" or i=="t":
        menu()
    else:
        print("Not found")
#menghitung hasil akhir point
    print()
    print("--------------------------------------------------------------------------------------")
    print("Terimakasih telah memainkan game ini, kamu menjawab",mula,"pertanyaan dengan benar")
    akhir=(mula/iyo)*100
    print("score kamu adalah: ",akhir,)
    print("---------------------------------------------------------------------------------------")
    i=input("Apakah ingin kembali ke menu awal(y/t)? ")
    if i=="y" or i=="Y":
        menu()
    elif i=="t" or i=="T":
        exit()
    else:
        print("Nout found")
#memanggil method
menu()

#Ran
#By ran