print("List Harga Warung Sayur A")
print("=========================")
print("| Tomat    || 7000/Kg   |")
print("| Beras    || 14000/Kg  |")
print("| Telur    || 29000/Kg  |")
print("=========================")

harga1 = 7000
harga2 = 14000
harga3 = 29000

var1 = "Tomat"
var2 = "Beras"
var3 = "Telur"

print("Masukan belanjaan Anda")

item_1 = input("Masukkan Belanjaan Pertama Anda : ")
kg1 = input("Berapa Kg Belanjaan Pertama Anda : ")

item_2 = input("Masukkan Belanjaan Kedua Anda : ")
kg2 = input("Berapa Kg Belanjaan Kedua Anda : ")

uang = input("Masukan Uang Anda : ")

if item_1 == var1:
  hasil1 = (harga1 * int(kg1))
elif item_1 == var2:
  hasil1 = (harga2 * int(kg1))
elif item_1 == var3:
  hasil1 = (harga3 * int(kg1))

if item_2 == var1:
  hasil2 = (harga1 * int(kg1))
elif item_2 == var2:
  hasil2 = (harga2 * int(kg1))
elif item_2 == var3:
  hasil2 = (harga3 * int(kg1))

hasil = hasil1 + hasil2
print("Ttal Belanjaan Anda Adalah : " + str(hasil))

Kembali = int(uang) - int(hasil)
print("Hasilnya adalah : " + str(Kembali))