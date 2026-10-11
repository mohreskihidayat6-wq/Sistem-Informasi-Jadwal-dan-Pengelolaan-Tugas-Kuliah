# Aplikasi Pengelolaan Pengeluaran Mahasiswa

Aplikasi desktop untuk membantu mahasiswa mencatat dan mengelola pengeluaran
sehari-hari dalam satu tempat.

## Deskripsi Proyek

Aplikasi Pengelolaan Pengeluaran Mahasiswa dirancang untuk memudahkan
mahasiswa mencatat transaksi pengeluaran, mengelompokkan pengeluaran
berdasarkan kategori, melihat riwayat transaksi, serta memantau jumlah
pengeluaran dalam periode tertentu.

Proyek ini dikembangkan sebagai proyek praktikum Rekayasa Perangkat
Lunak dengan menerapkan arsitektur Model-View-Controller (MVC), basis
data relasional MySQL, dan operasi CRUD.

## Fitur Utama

-   Mengelola kategori pengeluaran.
-   Menambahkan dan melihat data pengeluaran.
-   Mencatat tanggal, jumlah, dan deskripsi pengeluaran.
-   Mengelompokkan pengeluaran, misalnya makanan, transportasi, kebutuhan kuliah, dan hiburan.
-   Melihat riwayat pengeluaran yang telah dicatat.
-   Menampilkan ringkasan total pengeluaran melalui antarmuka desktop.

## Teknologi yang Digunakan

-   **Bahasa pemrograman:** Python
-   **Antarmuka desktop:** CustomTkinter
-   **Basis data:** MySQL
-   **Server basis data lokal:** Laragon
-   **Konektor basis data:** mysql-connector-python
-   **Arsitektur:** Model-View-Controller (MVC)
-   **Editor kode:** Visual Studio Code
-   **Version control:** Git dan GitHub
-   **Lingkungan virtual:** Python `venv`

## Struktur Proyek

``` text
Modul5/
├── config/
│   └── database.py
├── models/
├── controllers/
├── views/
├── app.py
├── test_model.py
├── requirements.txt
├── .gitignore
└── README.md
```

Struktur tersebut merupakan rancangan awal. File dan folder dapat
disesuaikan dengan implementasi serta instruksi pada Modul I--V.

## Struktur Basis Data

Nama basis data: `db_pengeluaran_mahasiswa`

Tabel yang direncanakan:

| Tabel | Keterangan |
|---|---|
| `mahasiswa` | Menyimpan identitas mahasiswa. |
| `kategori` | Menyimpan nama kategori pengeluaran, seperti makanan, transportasi, kebutuhan kuliah, dan hiburan. |
| `pengeluaran` | Menyimpan tanggal, jumlah, deskripsi, dan kategori dari setiap transaksi pengeluaran. |

## Persiapan dan Instalasi

### 1. Prasyarat

Pastikan perangkat telah memiliki:

-   Python 3
-   Visual Studio Code
-   Laragon dengan MySQL
-   Git

### 2. Buka folder proyek

Buka folder proyek ini melalui Visual Studio Code, kemudian buka
terminal terintegrasi.

### 3. Buat lingkungan virtual

Jalankan perintah berikut di terminal:

``` powershell
py -m venv env
```

Aktifkan lingkungan virtual pada Windows PowerShell:

``` powershell
.\env\Scripts\Activate.ps1
```

### 4. Instal pustaka yang dibutuhkan

``` powershell
python -m pip install --upgrade pip
pip install customtkinter mysql-connector-python
```

### 5. Siapkan basis data

1.  Buka Laragon.
2.  Jalankan layanan MySQL.
3.  Buat basis data bernama `db_pengeluaran_mahasiswa`.
4.  Buat tabel `mahasiswa`, `kategori`, dan `pengeluaran` sesuai struktur basis data proyek.
5.  Sesuaikan konfigurasi koneksi database dengan pengaturan MySQL
    lokal.

Jangan menyimpan kata sandi atau informasi rahasia di repository publik.
Gunakan konfigurasi lokal yang aman.

### 6. Jalankan aplikasi

Setelah file aplikasi dan konfigurasi selesai dibuat, jalankan aplikasi
melalui terminal:

``` powershell
python app.py
```

Perintah tersebut digunakan jika `app.py` telah menjadi titik masuk
aplikasi.

## Arsitektur MVC

-   **Model:** mengelola data dan komunikasi dengan MySQL.
-   **View:** menampilkan antarmuka desktop menggunakan CustomTkinter.
-   **Controller:** menghubungkan tindakan pengguna dengan proses pada
    Model dan tampilan pada View.

## Version Control dengan Git

Untuk memeriksa status perubahan:

``` bash
git status
```

Untuk menambahkan dan menyimpan perubahan:

``` bash
git add .
git commit -m "Initial project setup"
```

Repository GitHub dapat dihubungkan sesuai konfigurasi repository
kelompok. Jangan mengunggah folder `env/`, kata sandi, atau konfigurasi
rahasia.

## Status Pengembangan

Proyek dikembangkan secara bertahap mengikuti materi praktikum Modul
I--V. Fitur dan struktur akhir akan disesuaikan dengan implementasi yang
telah diuji.

## Pengembang

-   **Nama proyek:** Aplikasi Pengelolaan Pengeluaran Mahasiswa
-   **Kelompok:** \[Isi nama atau nomor kelompok\]
-   **Anggota:** \[Isi nama dan NIM anggota kelompok\]
-   **Program Studi:** Sistem Informasi
-   **Fakultas:** Teknik
-   **Universitas:** Universitas Tadulako

------------------------------------------------------------------------

README ini merupakan dokumentasi awal proyek dan perlu diperbarui ketika
implementasi aplikasi berubah.

