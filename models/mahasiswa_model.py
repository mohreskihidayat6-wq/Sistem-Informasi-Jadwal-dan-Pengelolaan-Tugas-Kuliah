
from config.database import get_connection


def get_all_mahasiswa():
    connection = get_connection()

    if connection is None:
        return []

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT id_mahasiswa, nama, nim
            FROM mahasiswa
            ORDER BY nama ASC
        """

        cursor.execute(query)
        return cursor.fetchall()

    except Exception as e:
        print("Gagal mengambil data mahasiswa:", e)
        return []

    finally:
        if cursor is not None:
            cursor.close()

        connection.close()
