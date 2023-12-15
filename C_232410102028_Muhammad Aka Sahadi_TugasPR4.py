# Muhammad Aka Sahadi 
# 232410102028

# NO 1
nama = str(input("masukkan nama = ")) # buatkan input dengan tipe data str
data = "" # data berfungsi sebagai tempat hasil operator
for hasil in nama : # buat kode perulangan dengan memasukkan variabel baru (hasil) ke dalam (nama)
    if hasil not in "a,i,u,e,o": # buat kode if dengan variabel (hasil) sebagai pengecualian di dalam vokal
        data += hasil  # setelah huruf vokal hilang, maka akan otomatis huruf selanjutnya untuk saling menempel/menjadi 1 kata
print(data)


# NO 2
while(True): # buat operator perulangan while dengn kondisi true di dalamnya
    masukkan = input("Masukkan data [$,x,#] : ") # buat variabel yang berisikan input dan petunjuk, simbol apa saja yang bisa di masukkan dalam input
    if 1 <= len(masukkan) <= 100: # buat kode if dengan memasukkan operator perbandingan dan (len()) sebagai pengukur/penjumlah elemen agar dapat meminimalkan dan memaksimalkan karakter
        break # masukkan break untuk memberhentikan paksa bila inputan lebih dari 100 karakter
    else:
        print("Panjang input minimal 1 karakter dan maksimal 100 karakter") # masukkan else dan beri print sebagai catatan bila user memassukkan 100 karakter lebih

total = 0 # total berfungsi sebagai tempat untuk hasil operator

for simbol in masukkan: # buat operasi perulangan for dengan variabel baru di dalamnya dan masukkan ke variabel input
    if simbol == "$": # buat if dengan variabel baru yang sudah di buat (simbol) dan samakan dengan simbol yang sudah ditentukan ($)
        total += 100 # masukkan variabel (total) dan tambahkan dengan 100, sekarang variabel total akan menampung nilai 100
    elif simbol == "x": # masukkan elif sebagai lanjutan dari if, dan samakan dengan simbol yang sudah ditentukan (x)
        total -= 10 # ketika user meng-input simbol ($x) maka kode akan melaksanakan perintah ($) dulu lalu dilanjutkan dengan perintah (x) yang dimana di kasus ini akan di -10 
        if total < 10: # masukkan kondisi if baru dengan (total) di dalamnya. bila nilai (total) < 10, maka (total) akan langsung bernilai 0
            total = 0
    elif simbol == "#": # masukkan elif sebagai lanjutan dari elif di atas, dan samakan dengan simbol yang sudah ditentukan (#)
        total *= 0.5 # sama dengan kondisi elif di atas, bila user meng-input ($x#) maka kode akan melaksanakan 0+100 lalu 100-10 dan terakhir 90*0.5 (atau 50% dalam kasus ini)
        if total == 0 : # masukkan kondisi if baru dengan (total) di dalamnya. bila nilai (total) == 0, maka (total) akan langsung bernilai 0
            total = 0
print(total)


# NO 3
isi_nomor = int(input("isi nomor = ")) # buatkan input dengan tipe int
total = 0 # total berfungsi sebagai tempat untuk hasil operator

hitung_cucup = 1 # buat variabel baru dengan 
for perhitungan in range(1, isi_nomor + 1): # buat perulangan for dengan memasukkan variabel baru (perhitungan) di dalam range. awali range dari 1 dan masukkan variabel input lalu + 1, sehingga input yang di masukkan akan di + 1
    total += hitung_cucup # masukkan variabel (total) dan tambahkan dengan variabel (hitung_cucup)
    hitung_cucup += 1 # setelah (hitung_cucup) = 1, akan di + 1
    if hitung_cucup > 3: # hasil (hitung_cucup) 2 > 3, karena belum > 3 maka, perulangan akan di lanjutkan, hingga = 4
        hitung_cucup = 1 # karena 4 > 3 maka 4 di ubah menjadi 1. perulangan akan terus di lakukan hingga (inputan) kali
print(total)