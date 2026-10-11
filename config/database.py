
import mysql.connector
from mysql.connector import Error


def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_pengeluaran_mahasiswa"
        )

        if connection.is_connected():
            print("Koneksi database berhasil!")
            return connection

    except Error as e:
        print("Koneksi database gagal:", e)

    return None
