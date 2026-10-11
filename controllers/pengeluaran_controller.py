
from models.pengeluaran_model import (
    get_all_pengeluaran,
    tambah_pengeluaran,
    ubah_pengeluaran,
    hapus_pengeluaran
)


class PengeluaranController:

    def tampilkan_pengeluaran(self):
        return get_all_pengeluaran()

    def tambah(
        self,
        id_mahasiswa,
        id_kategori,
        tanggal,
        nominal,
        deskripsi
    ):
        return tambah_pengeluaran(
            id_mahasiswa,
            id_kategori,
            tanggal,
            nominal,
            deskripsi
        )

    def ubah(
        self,
        id_pengeluaran,
        id_mahasiswa,
        id_kategori,
        tanggal,
        nominal,
        deskripsi
    ):
        return ubah_pengeluaran(
            id_pengeluaran,
            id_mahasiswa,
            id_kategori,
            tanggal,
            nominal,
            deskripsi
        )

    def hapus(self, id_pengeluaran):
        return hapus_pengeluaran(id_pengeluaran)
