import mysql.connector
class Database:
    def __init__(self, host, user, password, database) :
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        self.db = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
        self.cur = self.db.cursor()
    
    def buat_table(self):
        self.cur.execute(''' CREATE TABLE IF NOT EXISTS Barang (
                         id_barang int PRIMARY KEY NOT NULL AUTO_INCREMENT,
                         nama_barang VARCHAR(255),
                         harga_satuan int (255),
                         jumlah_stok VARCHAR (255),
                         jumlah_ambil int (255)
        );''')

        self.cur.execute(''' CREATE TABLE IF NOT EXISTS Gudang (
                         id_gudang int PRIMARY KEY NOT NULL AUTO_INCREMENT,
                         nama_gudang VARCHAR(255),
                         lokasi VARCHAR(255)
        );''')
        self.db.commit()
        