Aplikasi Pengelolaan Pengeluaran Mahasiswa
1. Deskripsi Proyek
Aplikasi Pengelolaan Pengeluaran Mahasiswa adalah aplikasi desktop yang
dirancang untuk membantu mahasiswa mencatat dan memantau pengeluaran
sehari-hari. Melalui aplikasi ini, mahasiswa dapat menyimpan transaksi
pengeluaran, mengelompokkan pengeluaran berdasarkan kategori, melihat
riwayat transaksi, serta memantau total pengeluaran dalam periode
tertentu.
Proyek ini dibuat sebagai tugas praktikum Rekayasa Perangkat Lunak (RPL)
dengan menerapkan arsitektur Model-View-Controller (MVC) dan
integrasi basis data MySQL.
2. Tujuan
- Membantu mahasiswa mencatat pengeluaran secara teratur.
- Memudahkan pengelompokan pengeluaran, misalnya makanan,
  transportasi, kebutuhan kuliah, dan hiburan.
- Menampilkan riwayat transaksi agar pengeluaran mudah diperiksa
  kembali.
- Membantu mahasiswa mengetahui jumlah pengeluaran dalam periode
  tertentu.
3. Fitur Utama
- Pencatatan pengeluaran: menambahkan tanggal, kategori, nominal,
  dan keterangan transaksi.
- Pengelolaan transaksi: melihat, mengubah, dan menghapus data
  pengeluaran.
- Kategori pengeluaran: mengelompokkan transaksi berdasarkan jenis
  kebutuhan.
- Riwayat pengeluaran: menampilkan daftar transaksi yang telah
  dicatat.
- Ringkasan pengeluaran: menghitung total pengeluaran dan
  menampilkan ringkasan berdasarkan periode yang dipilih.
Catatan: Fitur dapat disesuaikan dengan ruang lingkup dan implementasi
akhir proyek.

4. Teknologi yang Digunakan
- Bahasa pemrograman: Python 3
- Antarmuka desktop: CustomTkinter
- Basis data: MySQL/MariaDB
- Lingkungan basis data: Laragon
- Konektor Python--MySQL: mysql-connector-python
- Editor kode: Visual Studio Code
- Version control: Git dan GitHub
5. Gambaran Arsitektur
Aplikasi menggunakan pola Model-View-Controller (MVC):
- Model: mengelola data dan operasi basis data, seperti menambah,
  membaca, memperbarui, dan menghapus transaksi.
- View: menampilkan antarmuka aplikasi menggunakan CustomTkinter.
- Controller: menghubungkan tindakan pengguna dari View dengan
  proses pada Model.
Pemisahan ini membantu membuat kode lebih terstruktur dan lebih mudah
dipelihara.
6. Rancangan Basis Data
Nama basis data yang direncanakan: db_pengeluaran_mahasiswa
Tabel utama yang disarankan:
Tabel mahasiswa
Menyimpan data mahasiswa yang menggunakan aplikasi. - id_mahasiswa ---
primary key - nama --- nama mahasiswa - nim --- nomor induk
mahasiswa
Tabel kategori
Menyimpan daftar kategori pengeluaran. - id_kategori --- primary key -
nama_kategori --- nama kategori
Tabel pengeluaran
Menyimpan catatan transaksi pengeluaran. - id_pengeluaran --- primary
key - id_mahasiswa --- foreign key ke tabel mahasiswa -
id_kategori --- foreign key ke tabel kategori - tanggal ---
tanggal pengeluaran - nominal --- jumlah uang yang dikeluarkan -
keterangan --- penjelasan singkat transaksi
Hubungan data: - Satu mahasiswa dapat memiliki banyak catatan
pengeluaran. - Satu kategori dapat digunakan oleh banyak catatan
pengeluaran.
Rancangan ini merupakan gambaran awal dan dapat disesuaikan ketika ERD
serta implementasi basis data dibuat.
7. Persiapan dan Instalasi
Pastikan Python 3, Git, Visual Studio Code, dan Laragon sudah terpasang.
1. Jalankan Laragon, lalu aktifkan layanan MySQL.
2. Buat basis data db_pengeluaran_mahasiswa melalui phpMyAdmin atau
   alat basis data yang tersedia.
3. Buka folder proyek di Visual Studio Code.
4. Buat dan aktifkan virtual environment di Windows:
   python -m venv env
   .\env\Scripts\activate
5. Pasang konektor MySQL:
   pip install mysql-connector-python
6. Jika proyek menggunakan CustomTkinter, pasang juga dependensinya:
   pip install customtkinter
7. Buat berkas .gitignore dan tambahkan:
   env/
   __pycache__/
   *.pyc
   .env
8. Konfigurasikan koneksi MySQL sesuai pengaturan lokal Laragon. Jangan
   unggah kata sandi atau informasi rahasia ke GitHub.
8. Struktur Folder yang Direncanakan
Struktur berikut merupakan rancangan awal yang mengikuti pemisahan MVC.
Nama atau susunan berkas dapat berubah sesuai tahapan praktikum.
pengeluaran-mahasiswa/
├── config/
│   └── database.py
├── controllers/
│   └── pengeluaran_controller.py
├── models/
│   └── pengeluaran_model.py
├── views/
│   └── pengeluaran_view.py
├── main.py
├── .gitignore
└── README.md
9. Ruang Lingkup
Aplikasi berfokus pada pencatatan dan pemantauan pengeluaran
mahasiswa. Aplikasi tidak dimaksudkan sebagai sistem perbankan, dompet
digital, atau aplikasi transaksi pembayaran. Perhitungan ringkasan
didasarkan pada data yang dimasukkan pengguna.
10. Status Proyek
Status: Perencanaan dan pengembangan awal.
Fitur, struktur folder, serta rancangan basis data akan diperbarui
mengikuti implementasi dan hasil praktikum.
