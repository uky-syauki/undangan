from random import randint
import calendar
from datetime import datetime

class buat_data:
    def __init__(self):
        self.format = "%Y-%m-%d %H:%M:%S.%f"
    def jumlah_hari_pada_bulan(self,tahun,bulan):
        return calendar.monthrange(tahun,bulan)[1]
    def set(self,n):
        n = int(n)
        if n < 10:
            return f"0{n}"
        return n
    def toDate(self,strTime):
        return datetime.strptime(strTime,self.format)
    def untuk_bulan(self,th,bln,jumlah):
        hasil = []
        ms = datetime.now().strftime("%f")
        for i in range(jumlah):
            tanggal = randint(1,self.jumlah_hari_pada_bulan(int(th),int(bln)))
            jam = randint(0,23)
            menit = randint(0,59)
            detik = randint(0,59)
            getRand = f"{th}-{self.set(bln)}-{tanggal} {jam}:{menit}:{detik}.{ms}"
            hasil.append(self.toDate(getRand))
        return hasil
    def untuk_tahun(self,th,jumlah):
        hasil = []
        for i in range(jumlah):
            bulan = randint(1,12)
            tanggal = randint(1,self.jumlah_hari_pada_bulan(int(th),int(bulan)))
            jam = randint(0,23)
            menit = randint(0,59)
            detik = randint(0,59)
            ms = datetime.now().strftime("%f")
            getRand = f"{th}-{bulan}-{tanggal} {jam}:{menit}:{detik}.{ms}"
            hasil.append(self.toDate(getRand))
        return hasil

