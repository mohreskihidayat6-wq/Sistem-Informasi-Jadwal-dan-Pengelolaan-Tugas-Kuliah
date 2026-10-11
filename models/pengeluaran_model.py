
from config.database import get_connection


def get_all_pengeluaran():
    connection = get_connection()

    if connection is None:
        return []

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                p.id_pengeluaran,
                m.nama,
                m.nim,
                k.nama_kategori,
                p.tanggal,
                p.nominal,
                p.deskripsi
            FROM pengeluaran p
            JOIN mahasiswa m
                ON p.id_mahasiswa = m.id_mahasiswa
            JOIN kategori k
                ON p.id_kategori = k.id_kategori
            ORDER BY p.tanggal DESC
        """

        cursor.execute(query)
        return cursor.fetchall()

    except Exception as e:
        print("Gagal mengambil data pengeluaran:", e)
        return []

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def tambah_pengeluaran(
    id_mahasiswa,
    id_kategori,
    tanggal,
    nominal,
    deskripsi
):
    connection = get_connection()

    if connection is None:
        return False

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO pengeluaran
            (id_mahasiswa, id_kategori, tanggal, nominal, deskripsi)
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            id_mahasiswa,
            id_kategori,
            tanggal,
            nominal,
            deskripsi
        )

        cursor.execute(query, values)
        connection.commit()

        return True

    except Exception as e:
        connection.rollback()
        print("Gagal menambahkan pengeluaran:", e)
        return False

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def ubah_pengeluaran(
    id_pengeluaran,
    id_mahasiswa,
    id_kategori,
    tanggal,
    nominal,
    deskripsi
):
    connection = get_connection()

    if connection is None:
        return False

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            UPDATE pengeluaran
            SET id_mahasiswa = %s,
                id_kategori = %s,
                tanggal = %s,
                nominal = %s,
                deskripsi = %s
            WHERE id_pengeluaran = %s
        """

        values = (
            id_mahasiswa,
            id_kategori,
            tanggal,
            nominal,
            deskripsi,
            id_pengeluaran
        )

        cursor.execute(query, values)
        connection.commit()

        return cursor.rowcount > 0

    except Exception as e:
        connection.rollback()
        print("Gagal mengubah pengeluaran:", e)
        return False

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


def hapus_pengeluaran(id_pengeluaran):
    connection = get_connection()

    if connection is None:
        return False

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            DELETE FROM pengeluaran
            WHERE id_pengeluaran = %s
        """

        cursor.execute(query, (id_pengeluaran,))
        connection.commit()

        return cursor.rowcount > 0

    except Exception as e:
        connection.rollback()
        print("Gagal menghapus pengeluaran:", e)
        return False

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()
