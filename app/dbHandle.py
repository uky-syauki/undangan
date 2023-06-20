from app.models import Barang, Terjual

class TabelBarang:
    def __init__(self):
        self.namaTabel = "Barang"
        self.dataBarang = self.extrakDataBarang(Barang.query.all())
    def extrakDataBarang(self,data):
        hasil = []
        for isi in data:
            bungkus = []
            bungkus.append(isi.id)
            bungkus.append(isi.kode_barang)
            bungkus.append(isi.nama_barang)
            bungkus.append(isi.harga_jual)
            bungkus.append(isi.harga_modal)
            bungkus.append(isi.tersedia)
            hasil.append(bungkus)
        return hasil



class TabelTerjual:
    def __init__(self):
        self.namaTabel = "Terjual"
        self.dataTerjual = self.extrakData(Terjual.query.all())
    def extrakData(self,data):
        hasil = []
        for isi in data:
            bungkus = []
            bungkus.append(isi.id)
            bungkus.append(isi.timestamp.strftime("%Y-%m-%d"))
            bungkus.append(isi.kode_barang)
            bungkus.append(isi.user_id)
            hasil.append(bungkus)
        return hasil


class DataBase(TabelBarang, TabelTerjual):
    def __init__(self):
        TabelTerjual.__init__(self)
        TabelBarang.__init__(self)
        self.totalTransaksi = 0
        self.totalPenjualan = 0
        self.totalModal = 0
        self.keuntungan = 0
        self.tanggal = list(range(1,32))
        self.bulan = list(range(1,13))
    def cariUntukHari(self,date):
        # date = "2023-04-24"
        data = self.dataTerjual
        hasil = 0
        for isi in data:
            # Date = isi[1].split('-')
            if isi[1] == date:
                hasil += 1
        return hasil
    def cariUntukBulan(self,date):
        date = date.split("-")
        y = []
        for i in range(1,33):
            y.append(self.cariUntukHari(date[0]+"-"+date[1]+"-"+str(i)))
        return self.tanggal, y
    def cariUntukTahun(self,date):
        # x, y = cariUntukHari('2023')
        date = date.split("-")
        y = []
        for i in range(1,13):
            if i < 10:
                bulan = "0"+str(i)
            else:
                bulan = str(i)
            x,y = self.cariUntukBulan(date[0]+"-"+bulan)
            y.append(sum(y))
        return self.bulan, y