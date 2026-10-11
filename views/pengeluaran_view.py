
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

from models.mahasiswa_model import get_all_mahasiswa
from models.kategori_model import get_all_kategori
from controllers.pengeluaran_controller import PengeluaranController


class PengeluaranView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Aplikasi Pengelolaan Pengeluaran Mahasiswa")
        self.geometry("1100x700")
        self.minsize(900, 600)

        self.controller = PengeluaranController()
        self.data_mahasiswa = []
        self.data_kategori = []
        self.id_terpilih = None

        self.buat_tampilan()
        self.muat_pilihan()
        self.tampilkan_data()

    def buat_tampilan(self):
        judul = ctk.CTkLabel(
            self,
            text="PENGELOLAAN PENGELUARAN MAHASISWA",
            font=("Arial", 24, "bold")
        )
        judul.pack(pady=(20, 5))

        subjudul = ctk.CTkLabel(
            self,
            text="Catat dan kelola pengeluaran mahasiswa"
        )
        subjudul.pack(pady=(0, 15))

        form = ctk.CTkFrame(self)
        form.pack(fill="x", padx=20, pady=10)

        form.grid_columnconfigure(1, weight=1)
        form.grid_columnconfigure(3, weight=1)

        ctk.CTkLabel(form, text="Mahasiswa").grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )
        self.pilih_mahasiswa = ctk.CTkComboBox(
            form, values=["Memuat mahasiswa..."], width=250
        )
        self.pilih_mahasiswa.grid(
            row=0, column=1, padx=10, pady=10, sticky="ew"
        )

        ctk.CTkLabel(form, text="Kategori").grid(
            row=0, column=2, padx=10, pady=10, sticky="w"
        )
        self.pilih_kategori = ctk.CTkComboBox(
            form, values=["Memuat kategori..."], width=250
        )
        self.pilih_kategori.grid(
            row=0, column=3, padx=10, pady=10, sticky="ew"
        )

        ctk.CTkLabel(form, text="Tanggal (YYYY-MM-DD)").grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )
        self.input_tanggal = ctk.CTkEntry(form)
        self.input_tanggal.grid(
            row=1, column=1, padx=10, pady=10, sticky="ew"
        )
        self.input_tanggal.insert(0, date.today().isoformat())

        ctk.CTkLabel(form, text="Nominal (Rp)").grid(
            row=1, column=2, padx=10, pady=10, sticky="w"
        )
        self.input_nominal = ctk.CTkEntry(
            form, placeholder_text="Contoh: 25000"
        )
        self.input_nominal.grid(
            row=1, column=3, padx=10, pady=10, sticky="ew"
        )

        ctk.CTkLabel(form, text="Deskripsi").grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )
        self.input_deskripsi = ctk.CTkEntry(
            form, placeholder_text="Contoh: Makan siang"
        )
        self.input_deskripsi.grid(
            row=2, column=1, columnspan=3,
            padx=10, pady=10, sticky="ew"
        )

        tombol = ctk.CTkFrame(self, fg_color="transparent")
        tombol.pack(fill="x", padx=20, pady=5)

        ctk.CTkButton(
            tombol, text="Tambah",
            command=self.tambah_data
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            tombol, text="Ubah",
            command=self.ubah_data
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            tombol, text="Hapus",
            fg_color="#B22222",
            hover_color="#8B0000",
            command=self.hapus_data
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            tombol, text="Bersihkan",
            fg_color="gray",
            hover_color="#555555",
            command=self.bersihkan_form
        ).pack(side="left", padx=5)

        tabel_frame = ctk.CTkFrame(self)
        tabel_frame.pack(fill="both", expand=True, padx=20, pady=(10, 20))

        kolom = (
            "id", "tanggal", "mahasiswa",
            "kategori", "nominal", "deskripsi"
        )

        self.tabel = ttk.Treeview(
            tabel_frame, columns=kolom, show="headings"
        )

        judul_kolom = {
            "id": "ID",
            "tanggal": "Tanggal",
            "mahasiswa": "Mahasiswa",
            "kategori": "Kategori",
            "nominal": "Nominal (Rp)",
            "deskripsi": "Deskripsi"
        }

        lebar_kolom = {
            "id": 50,
            "tanggal": 110,
            "mahasiswa": 170,
            "kategori": 150,
            "nominal": 120,
            "deskripsi": 200
        }

        for kolom_id in kolom:
            self.tabel.heading(
                kolom_id, text=judul_kolom[kolom_id]
            )
            self.tabel.column(
                kolom_id,
                width=lebar_kolom[kolom_id],
                anchor="w"
            )

        scrollbar = ttk.Scrollbar(
            tabel_frame, orient="vertical",
            command=self.tabel.yview
        )
        self.tabel.configure(yscrollcommand=scrollbar.set)

        self.tabel.pack(
            side="left", fill="both", expand=True, padx=(10, 0), pady=10
        )
        scrollbar.pack(side="right", fill="y", padx=(0, 10), pady=10)

        self.tabel.bind(
            "<<TreeviewSelect>>", self.pilih_baris
        )

    def muat_pilihan(self):
        self.data_mahasiswa = get_all_mahasiswa()
        self.data_kategori = get_all_kategori()

        daftar_mahasiswa = [
            f"{m['id_mahasiswa']} - {m['nama']} ({m['nim']})"
            for m in self.data_mahasiswa
        ]

        daftar_kategori = [
            f"{k['id_kategori']} - {k['nama_kategori']}"
            for k in self.data_kategori
        ]

        self.pilih_mahasiswa.configure(
            values=daftar_mahasiswa or ["Tidak ada mahasiswa"]
        )
        self.pilih_kategori.configure(
            values=daftar_kategori or ["Tidak ada kategori"]
        )

        if daftar_mahasiswa:
            self.pilih_mahasiswa.set(daftar_mahasiswa[0])

        if daftar_kategori:
            self.pilih_kategori.set(daftar_kategori[0])

    def ambil_input(self):
        mahasiswa = self.pilih_mahasiswa.get()
        kategori = self.pilih_kategori.get()
        tanggal = self.input_tanggal.get().strip()
        nominal = self.input_nominal.get().strip()
        deskripsi = self.input_deskripsi.get().strip()

        if mahasiswa.startswith("Tidak ada") or not mahasiswa:
            messagebox.showwarning(
                "Peringatan", "Pilih mahasiswa terlebih dahulu."
            )
            return None

        if kategori.startswith("Tidak ada") or not kategori:
            messagebox.showwarning(
                "Peringatan", "Pilih kategori terlebih dahulu."
            )
            return None

        try:
            id_mahasiswa = int(mahasiswa.split(" - ")[0])
            id_kategori = int(kategori.split(" - ")[0])
        except (ValueError, IndexError):
            messagebox.showwarning(
                "Peringatan", "Pilihan mahasiswa atau kategori tidak valid."
            )
            return None

        try:
            tanggal_obj = date.fromisoformat(tanggal)
        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Tanggal harus menggunakan format YYYY-MM-DD."
            )
            return None

        if tanggal_obj.isoformat() != tanggal:
            messagebox.showwarning(
                "Peringatan",
                "Masukkan tanggal yang valid dengan format YYYY-MM-DD."
            )
            return None

        try:
            nominal = float(nominal)
            if nominal <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning(
                "Peringatan", "Nominal harus berupa angka lebih dari 0."
            )
            return None

        return (
            id_mahasiswa, id_kategori,
            tanggal, nominal, deskripsi
        )

    def tampilkan_data(self):
        for item in self.tabel.get_children():
            self.tabel.delete(item)

        data = self.controller.tampilkan_pengeluaran()

        for item in data:
            self.tabel.insert(
                "",
                "end",
                values=(
                    item["id_pengeluaran"],
                    item["tanggal"],
                    item["nama"],
                    item["nama_kategori"],
                    f"{float(item['nominal']):,.0f}",
                    item["deskripsi"] or ""
                )
            )

    def tambah_data(self):
        data = self.ambil_input()
        if data is None:
            return

        berhasil = self.controller.tambah(*data)

        if berhasil:
            messagebox.showinfo(
                "Berhasil", "Pengeluaran berhasil ditambahkan."
            )
            self.bersihkan_form()
            self.tampilkan_data()
        else:
            messagebox.showerror(
                "Gagal", "Pengeluaran gagal ditambahkan."
            )

    def pilih_baris(self, event=None):
        pilihan = self.tabel.selection()
        if not pilihan:
            return

        nilai = self.tabel.item(pilihan[0], "values")
        self.id_terpilih = int(nilai[0])

        self.input_tanggal.delete(0, tk.END)
        self.input_tanggal.insert(0, str(nilai[1]))

        self.input_nominal.delete(0, tk.END)
        self.input_nominal.insert(
            0, str(nilai[4]).replace(",", "")
        )

        self.input_deskripsi.delete(0, tk.END)
        self.input_deskripsi.insert(0, str(nilai[5]))

        for m in self.data_mahasiswa:
            if m["nama"] == nilai[2]:
                self.pilih_mahasiswa.set(
                    f"{m['id_mahasiswa']} - {m['nama']} ({m['nim']})"
                )
                break

        for k in self.data_kategori:
            if k["nama_kategori"] == nilai[3]:
                self.pilih_kategori.set(
                    f"{k['id_kategori']} - {k['nama_kategori']}"
                )
                break

    def ubah_data(self):
        if self.id_terpilih is None:
            messagebox.showwarning(
                "Peringatan", "Pilih data pada tabel yang ingin diubah."
            )
            return

        data = self.ambil_input()
        if data is None:
            return

        berhasil = self.controller.ubah(self.id_terpilih, *data)

        if berhasil:
            messagebox.showinfo(
                "Berhasil", "Pengeluaran berhasil diubah."
            )
            self.bersihkan_form()
            self.tampilkan_data()
        else:
            messagebox.showwarning(
                "Informasi",
                "Data tidak berubah atau gagal diubah."
            )

    def hapus_data(self):
        if self.id_terpilih is None:
            messagebox.showwarning(
                "Peringatan", "Pilih data pada tabel yang ingin dihapus."
            )
            return

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah kamu yakin ingin menghapus pengeluaran ini?"
        )

        if not konfirmasi:
            return

        berhasil = self.controller.hapus(self.id_terpilih)

        if berhasil:
            messagebox.showinfo(
                "Berhasil", "Pengeluaran berhasil dihapus."
            )
            self.bersihkan_form()
            self.tampilkan_data()
        else:
            messagebox.showerror(
                "Gagal", "Pengeluaran gagal dihapus."
            )

    def bersihkan_form(self):
        self.id_terpilih = None

        self.input_tanggal.delete(0, tk.END)
        self.input_tanggal.insert(0, date.today().isoformat())

        self.input_nominal.delete(0, tk.END)
        self.input_deskripsi.delete(0, tk.END)

        if self.data_mahasiswa:
            m = self.data_mahasiswa[0]
            self.pilih_mahasiswa.set(
                f"{m['id_mahasiswa']} - {m['nama']} ({m['nim']})"
            )

        if self.data_kategori:
            k = self.data_kategori[0]
            self.pilih_kategori.set(
                f"{k['id_kategori']} - {k['nama_kategori']}"
            )

        for item in self.tabel.selection():
            self.tabel.selection_remove(item)
