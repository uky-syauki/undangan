from app.models import Barang, Terjual

data = Barang.query.all()

kode_barang = []

for isi in data:
    kode_barang.append(isi.kode_barang)


print(kode_barang)