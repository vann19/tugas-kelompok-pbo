from stok_gudang import barang
from stok_gudang import gudang
from stok_gudang import Tambah_barang
from stok_gudang import Ambil_barang
from db import Database
import pickle

db = Database ('localhost', 'root', '' ,'stok_gudang_barang')
db.connect()
db.buat_table()

print('input data stok gudang barang jika berhenti isi id barang dengan keluar')

while True:
    print('Menu ')
    print('1. Input data barang')
    print('2. Input data gudang ')
    print('3. Cetak data barang')
    print('4. Cetak data gudang')
    print('5. Update data barang')
    print('6. Update data gudang')
    print('7. Delete data barang')
    print('8. Delete data gudang')
    print('0. Selesai')
    pilih = int(input('Pilih Menu :'))
    if pilih == 1:
        a = str(input('Masukan id barang :'))
        if a!='keluar':
            b = str(input('Masukan nama barang         :'))
            c = int(input('Masukan harga satuan        :'))
            d = str(input('Masukan Jumlah stok         :'))
            e = str(input('Masukan Jumlah ambil barang :'))
            y1=str(input('Hitung stok data barang : <y/t>? : '))
            if y1 == 'y':
                jml_barang = 5000
                yang_akan_di_stok = 3000
            else:
                jml_barang = 0
                yang_akan_di_stok = 250
            
            gud = Tambah_barang(a,b,c,d,e)
            x = gud.hitung_barang(jml_barang,yang_akan_di_stok)
            gud.Barang = x
            db.insert('Barang', pickle.dump(gud))

            
    
