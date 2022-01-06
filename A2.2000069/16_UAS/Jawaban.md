1. Class adalah cetak biru atau prototipe dari objek dimana kita mendefinisikan atribut dari suatu objek. Atribut ini terdiri dari data member (variabel) dan fungsi (metode).
2. Instance adalah istilah lain dari objek suatu kelas. Sebuah objek yang dibuat dari prototipe kelas Lingkaran misalnya disebut sebagai instance dari kelas tersebut.
3. class adalah cetak biru yang digunakan untuk menggambarkan bagaimana membuat sesuatu, instance adalah objek yang dibuat dari cetak biru tersebut.
4. Menggunakan kata kunci class diikuti oleh nama kelas tersebut
    contoh: class hero:
                pass
5. Nama kelas biasanya harus menggunakan konvensi CapWords. Perhatikan bahwa ada konvensi terpisah untuk nama bawaan: sebagian besar nama bawaan adalah kata tunggal (atau dua kata dijalankan bersamaan), dengan konvensi CapWords hanya digunakan untuk nama pengecualian dan konstanta bawaan.
6. Untuk membuat objek dari sebuah kelas, kita bisa memanggil nama kelas dengan argumen sesuai dengan fungsi __init__() pada saat kita mendefinisikannya.
    Contoh: hero1 = Hero("lesley", 100, 10, 4)
            hero2 = Hero("alucard", 100, 15, 1)
            hero3 = Hero("aldous", 1000, 100, 0)
7. Untuk mengakses atribut objek dengan menggunakan operator titik. Variabel kelas bisa diakses dengan menggunakan nama kelasnya.
    Contoh: hero1.siapa()
            hero1.healthUp(10)

            print(hero1.getHealth())
8. Metode adalah fungsi yang didefinisikan di dalam suatu kelas
9. Keyword self digunakan untuk merepresentasikan setiap objek yang dibuat.
10. Metode __init__() adalah metode konstruktor, yaitu metode khusus yang digunakan Python untuk menginisialisasi pembuatan objek dari kelas tersebut.
11. class child mewarisi semua atribut dan perilaku parents.
12. Bisa