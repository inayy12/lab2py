# input nilai variable
a=input("masukkan nilai a:")
b=input("Masukkan nilai b:")

# cetak nilai variabel
print("Variabel a=",a)
print("Variabel b=",b)

# cetak nilai hasil operasi kedua variabel dengan String Format
print("Hasil penggabuang {1}+{0}=%s".format(a,b) %(a+b))

# konversi nilai variabel
a=int(a)
b=int(b)
print("Hasil penjumlahan {1}+{0}=%d".format(a,b)%(a+b))
print("Hasil pembagian {1}/{0}=%d".format(a,b)%(a/b))
