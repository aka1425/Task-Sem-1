# Muhammad Aka Sahadi
# 232410102028
import csv # digunakan untuk mengimpor file ini agar bisa bekerja, membaca, menulis modul file csv.
import os # digunakan untuk mengimpor modul os (sistem operasi) ke dalam flie ini


if not os.path.exists("Data Kasir.csv"): # jika file tidak tersedia, maka os akan langsung menambahkan file baru dengan nama yg sudah tersedia
    header = ["Tanggal", "Nama Barang", "Jumlah Barang", "Total Harga"] # baris pertama di dalam kolom yang berisi nama kolom
    with open("Data Kasir.csv", "w", newline="") as file: # digunakan agar file bisa membaca data dari file csv
        writer = csv.writer(file) # digunakan untuk menulis data ke file CSV
        writer.writerow(header) # untuk menambahkan satu baris data ke dalam file csv di atas


while True: # untuk looping tanpa batas namun hanya jika nilainya true
    print("Menu") # menampilkan "Menu"
    print("1. Tambahkan Transaksi") # menampilkan "1. Tambahkan Transaksi"
    print("2. Tampilkan Transaksi") # menampilkan "2. Tampilkan Transaksi"
    print("3. Hapus Data") # menampilkan "3. Hapus Data"
    print("4. Berhenti") # menampilkan "4. Berhenti"
    masukkan = input("Pilih Aksi : ") # menampilkan input "Pilih Aksi : "

    match masukkan: # operasi untuk menyimpan beberapa data yang sudah dituliskan
        case "1": # untuk memanggil operasi yang telah di tentukan saat di terminal
            tanggal = input("Input tanggal (Tanggal-Bulan-Tahun): ") # menampilkan "Input tanggal (Tanggal-Bulan-Tahun): "
            barang = input("Input nama barang: ") # menampilkan "Input nama barang: "
            jumlah_barang = input("Input jumlah barang: ") # menampilkan "Input jumlah barang: "
            total_harga = input("Input total harga: ") # menampilkan "Input total harga: "

            with open("Data Kasir.csv", "a", newline="") as file: # mwmbuka file "Data Kasir.csv" dalam mode 'append" dengan menggunakan konstruksi 'with'. Ini digunakan untuk menambahkan data ke akhir file tanpa menghapus data yang sudah ada.
                writer = csv.writer(file) # digunakan untuk menulis data ke file csv
                writer.writerow([tanggal, barang, jumlah_barang, total_harga]) # menulis baris baru ke dalam file csv 
                print("Transaksi berhasil ditambahkan!") # jika operator di atas telah berhasil dilaksanakan, maka akan menampilkan "Transaksi berhasil ditambahkan!"

        case "2": # untuk memanggil operasi yang telah di tentukan saat di terminal
            if os.path.exists("Data Kasir.csv"): # jika file "Data Kasir.csv" sudah tersedia maka akan melaksanakan operator di bawah
                with open("Data Kasir.csv", "r", newline="") as file: # untuk membuka file dengan nama "Data Kasir.csv" dalam mode membaca ("r") menggunakan sebuah blok 'with'
                    reader = csv.reader(file) # digunakan untuk membaca data ke file csv
                    next(reader) # digunakan untuk membaca baris berikutnya yang terkait dengan membaca file csv
                    for row in reader: # adalah loop untuk mengiterasi melalui setiap baris dalam objek pembaca csv. Setiap baris dalam file csv akan diwakili oleh variabel row
                        print("Tanggal: {}, Barang: {}, Jumlah: {}, Total Harga: {}".format(*row)) # setelah setiap placeholder '{}' dipanggil, 'row' akan menguraikan data dalam file csv menjadi format yang lebih mudah dibaca
            else: # bila operator di atas tidak ditemukan/berjalan dengan baik maka akan melakukan operasi ini
                print("File Data Kasir.csv tidak ditemukan.") # menampilkan "File Data Kasir.csv tidak ditemukan." bila terjadi kesalahan saat operasi di atas di jalankan

        case "3": # untuk memanggil operasi yang telah di tentukan saat di terminal
            tanggal = input("Input1 tanggal transaksi (Tanggal-Bulan-Tahun): ") # menampilkan input "Pilih Aksi : "
            data = [] # mengartikan bahwa variabel data berisi daftar kosong (list kosong)

            if os.path.exists("Data Kasir.csv"):  # jika file "Data Kasir.csv" sudah tersedia maka akan melaksanakan operator di bawah
                with open("Data Kasir.csv", "r", newline="") as file: # untuk membuka file dengan nama "Data Kasir.csv" dalam mode membaca ("r") menggunakan sebuah blok 'with'
                    reader = csv.reader(file) # digunakan untuk membaca data ke file csv
                    for row in reader: # adalah loop untuk mengiterasi melalui setiap baris dalam objek pembaca csv. Setiap baris dalam file csv akan diwakili oleh variabel row
                        if row[0] != tanggal: # untuk memeriksa apakah nilai pada indeks pertama (0) dari list row tidak sama dengan nilai dari variabel "tanggal"
                            data.append(row) # jika operasi di atas berhasil maka 'row' akan ditambahkan ke dalam list "data"
                with open("Data Kasir.csv", "w", newline="") as file: # untuk membuka file dengan nama "Data Kasir.csv" dalam mode penulisan ("w") menggunakan blok 'with'
                    writer = csv.writer(file) # digunakan untuk menulis data ke file csv
                    writer.writerows(data) # menulis baris baru ke dalam file csv 
                    print("Transaksi berhasil dihapus!") # jika operator di atas telah berhasil dilaksanakan, maka akan menampilkan "Transaksi berhasil dihapus!"
            else: # bila operator di atas tidak ditemukan/berjalan dengan baik maka akan melakukan operasi ini
                print("file tidak tersedia") # menampilkan "file tidak tersedia" bila terjadi kesalahan saat operasi di atas di jalankan

    if masukkan == "4": # jika user meng-input "4" maka akan melaksanakan operasi yang sudah di sesusaikan
        break # akan menghentikan loop
    else: # bila operator di atas tidak ditemukan/berjalan dengan baik maka akan melakukan operasi ini
        print("Aksi tidak tersedia!") # jika user meng-input nomor selain "1","2","3","4" maka terminal akan menampilkan "Aksi tidak tersedia!"