
from config.database import get_connection


def get_all_kategori():
    connection = get_connection()

    if connection is None:
        return []

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT id_kategori, nama_kategori
            FROM kategori
            ORDER BY nama_kategori ASC
        """

        cursor.execute(query)
        data = cursor.fetchall()

        return data

    except Exception as e:
        print("Gagal mengambil data kategori:", e)
        return []

    finally:
        cursor.close()
        connection.close()
