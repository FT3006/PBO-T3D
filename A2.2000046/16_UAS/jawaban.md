1. Class adalah sebuah rancangan yang berisi pendefinisian varibel dan methode yang menggambarkan objek tertentu.

2. Instance adalah salinan yang berbeda dari class, maksudnya instance itu menggambarkan object.\
   Misal objectnya hero, maka instancenya "lina","axe".

3. Jika class menyediakan rancangan untuk object, maka instance merupakan gambaran dari object yang dibentuk dari suatu class.\
   Intinya, instance suatu object yang dibuat dari rancangan tersebut.

4. Dengan menulis "class" diawal, kemudian diikuti dengan nama kelasnya dan diakhiri dengan titik dua.
   Contoh : 
   ```python
   class Hero:
   ```

5. Ditulis dengan notasi CamelCase, dimulai dengan huruf Kapital.
   ```python
   Hero()
   ```

6. Yakni dengan menggunakan nama class, lalu diikuti tanda kurung.\
   Misal, nama classnya `Hero`, maka penulisannya : 
   ```python
   my_hero = Hero()
   ```

7. Dengan menambahkan titik ( . )\
   Misal, `nama_instance.nama_atribut`

8. Sebuah fungsi yang didefinisikan di dalam class.

9. self digunakan untuk menampung dirinya sendiri, maksudnya self ini adalah argumen pertama dari setiap metode merujuk pada instance class saat ini.

10. `__init__` Metode menginisialisasi sebuah instance dari class.

11. Karena konsep Inheritance diturunkan, maka semua kode yang telah dibuat sebelumnya (didalam class) dapat dipakai kembali di class lain sebagai class turunannya. Dengan begitu code yang sama tidak perlu dibuat berulang kali, dan alhasil bisa mencegah duplikasi code.

12. Tentu saja bisa.