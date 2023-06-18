from app.models import Barang, Terjual


class TabelBarang:
    def __init__(self):
        self.namaTabel = "Barang"
        self.dataBarang, self.tersedia = self.toDict(Barang.query.all())
    def toDict(self,data):
        hasil = {}
        tersedia = {}
        for isi in data:
            makeDict = {}
            makeDict["nama_barang"] = isi.nama_barang
            makeDict["harga_jual"] = isi.harga_jual
            makeDict["harga_modal"] = isi.harga_modal
            tersedia[isi.kode_barang] = isi.tersedia
            hasil[isi.kode_barang] = makeDict
        tersedia = dict(sorted(tersedia.items(), key=lambda x: x[1]))
        return hasil, tersedia


class TabelTerjual:
    def __init__(self):
        self.namaTabel = "Terjual"
        self.dataTerjual = self.extrakData(Terjual.query.all())
    def getDataAll(self):
        return self.dataTerjual
    def getDataFilter(self,field):
        query = f"SELECT {field} from {self.namaTabel}"
    def getFromYear(self,year):
        hasil = []
        hitungBarang = {}
        for isi in self.dataTerjual:
            if isi[1].strftime("%Y") == year:
                hasil.append(isi)
                if isi[2] not in hitungBarang.keys():
                    hitungBarang[isi[2]] = 1
                else:
                    hitungBarang[isi[2]] += 1
        hitungBarang = dict(sorted(hitungBarang.items(), key=lambda x: x[1])[::-1])
        return hasil, hitungBarang
    def getFromMoon(self,date):
        hasil = []
        hitungBarang = {}
        for isi in self.dataTerjual:
            if isi[1].strftime("%Y-%m") == date:
                hasil.append(isi)
                if isi[2] not in hitungBarang.keys():
                    hitungBarang[isi[2]] = 1
                else:
                    hitungBarang[isi[2]] += 1
        hitungBarang = dict(sorted(hitungBarang.items(), key=lambda x: x[1])[::-1])
        return hasil, hitungBarang
    def getFromDay(self,date):
        hasil = []
        hitungBarang = {}
        for isi in self.dataTerjual:
            if isi[1].strftime("%Y-%m-%d") == date:
                hasil.append(isi)
                if isi[2] not in hitungBarang.keys():
                    hitungBarang[isi[2]] = 1
                else:
                    hitungBarang[isi[2]] += 1
        hitungBarang = dict(sorted(hitungBarang.items(), key=lambda x: x[1])[::-1])
        return hasil, hitungBarang
    def extrakData(self,data):
        hasil = []
        for isi in data:
            bungkus = []
            bungkus.append(isi.id)
            bungkus.append(isi.timestamp)
            bungkus.append(isi.kode_barang)
            bungkus.append(isi.user_id)
            hasil.append(bungkus)
        return hasil


class DataBase(TabelBarang, TabelTerjual):
    def __init__(self):
        TabelBarang.__init__(self)
        TabelTerjual.__init__(self)
        self.union, self.totalTransaksi, self.totalPenjualan, self.totalModal, self.keuntungan = self.relasi()
        self.forStatYearKey = []
        self.forStatYearValue = []
        self.data1, self.data2 = self.getAllMoon()
    def relasi(self):
        totalTransaksi = 0
        totalPenjualan = 0
        totalModal = 0
        hasil = []
        for isi in self.dataTerjual:
            bungkus = []
            bungkus.append(isi[3])
            bungkus.append(isi[2])
            bungkus.append(isi[1].strftime("%Y-%m-%d"))
            dariBarang = self.dataBarang[isi[2]]
            bungkus.append(dariBarang["nama_barang"])
            bungkus.append(dariBarang["harga_jual"])
            bungkus.append(dariBarang["harga_modal"])
            totalTransaksi += 1
            totalPenjualan += dariBarang["harga_jual"]
            totalModal += dariBarang["harga_modal"]
            hasil.append(bungkus)
        keuntungan = totalPenjualan-totalModal
        return hasil, totalTransaksi, totalPenjualan, totalModal, keuntungan
    def getAllMoon(self):
        hasil = {}
        hitung = {}
        for i in range(1,13):
            if i < 10:
                bln = f"0{i}"
            else:
                bln = i
            hasil[str(i)],hitung[str(i)] = self.getFromMoon(f"2023-{bln}")
            total = 0
            for kunci in hitung[str(i)].keys():
                total += hitung[str(i)][kunci]
            self.forStatYearKey.append(i)
            self.forStatYearValue.append(total)
            hitung[str(i)]["total"] = total
        return hasil, hitung