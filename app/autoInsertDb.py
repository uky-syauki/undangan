from random import randint
from datetime import datetime

class buat_data:
    def __init__(self):
        self.format = "%Y-%m-%d %H:%M:%S.%f"
    def set(self,n):
        if n < 10:
            return f"0{n}"
        return n
    def toDate(self,strTime):
        return datetime.strptime(strTime,self.format)
    def untuk_bulan(self,th,bln,jumlah):
        hasil = []
        ms = datetime.now().strftime("%f")
        for i in range(jumlah):
            tanggal = set(randint(1,31))
            jam = set(randint(0,23))
            menit = set(randint(0,59))
            detik = set(randint(0,59))
            getRand = f"{th}-{self.set(bln)}-{tanggal} {jam}:{menit}:{detik}.{ms}"
            hasil.append(self.toDate(getRand))
        return hasil
    def untuk_tahun(self,th,jumlah):
        hasil = []
        for i in range(jumlah):
            bulan = set(randint(1,12))
            tanggal = set(randint(1,31))
            jam = set(randint(0,24))
            menit = set(randint(0,59))
            detik = set(randint(0,59))
            ms = datetime.now().strftime("%f")
            getRand = f"{th}-{bulan}-{tanggal} {jam}:{menit}:{detik}.{ms}"
            hasil.append(self.toDate(getRand))
        return hasil
