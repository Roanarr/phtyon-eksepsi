try:
    a = int(input("Masukan nilai a : "))
    b = int(input("Masukan nilai b : "))
except ValueError:
    print("Nilai harus bertipe numerik")
else: 
    hasil=a+b
    print("Hasil Penjumlahan :",hasil)