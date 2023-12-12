
class barang:
    def __init__(self,id_barang,nama_barang,harga_satuan,jumlah_stok,jumlah_ambil):
        self.id_barang = id_barang
        self.nama_barang = nama_barang
        self.harga_satuan = harga_satuan
        self.jumlah_stok = jumlah_stok
        self.jumlah_ambil = jumlah_ambil

    def tampilkan_data_barang(self):
        print('ID BARANG           :',self.id_barang)
        print('NAMA BARANG         :',self.nama_barang)
        print('HARGA SATUAN BARANG :',self.harga_satuan)
        print('JUMLAH STOK         :',self.jumlah_stok)


    def hitung_stok_barang(self,Barang):
        return Barang*50

    
class gudang:
    def __init__(self,id_gudang,nama_gudang,lokasi):
        self.id_gudang = id_gudang
        self.nama_gudang = nama_gudang
        self.lokasi = lokasi
        
    def tampilakan_tempat_gudang(self):
        print('ID GUDANG        :',self.id_gudang)
        print('NAMA GUDANG      :',self.nama_gudang)
        print('NAMA LOKASI      :',self.lokasi)

class Tambah_barang(barang):
    Barang = 0
    def __init__(self,id_barang,nama_barang,harga_satuan,jumlah_stok,harga):
        super().__init__(id_barang,nama_barang,harga_satuan,jumlah_stok)
        self.jumlah_stok = jumlah_stok
        self.harga = harga
        Tambah_barang.Barang+=1

    def stok_barang(self):
        self.tampilkan_data_barang()
        print('Stok Barang :',self.jumlah_stok, 'Bulan')
        print('Harga Barang : Rp',self.harga)

    def hitung_barang(self,Barang):
        if Barang > 20:
            return 50*500000
        elif Barang >10:
            return Barang*50000
        elif Barang <=0:
            return 0
        else:
            return Barang*20000
    def TampilkanJumlahBarang(self):
        print('Jumlah Barang Adalah ',Tambah_barang.Barang)

class Ambil_barang(barang):
    def ambil_stok_barang(self):
        self.tampilkan_data_barang()
        print('Nama Barang      :', self.nama_barang)
        print('Jumlah Barang Yang Diammmbil :',self.jumlah_ambil, 'Bulan')

    def kurangi_stok(self):
        if self.jumlah_stok >= self.jumlah_ambil:
            self.jumlah_stok -= self.jumlah_ambil
            print(f'stok barang {self.nama_barang} berhasil dikurangi sebanyak {self.jumlah_ambil} bulan')
            print(f'Tidak dapat mengambil stok barang {self.nama_barang} sebanyak {self.jumlah_ambil} bulan. stok tidak mencukupi')
        




