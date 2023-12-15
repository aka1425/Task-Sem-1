# Muhammad Aka Sahadi (232410102028) (C)

masukkan = int(input("Masukkan angka = "))
angka = masukkan % 2

if angka == 1:
    if masukkan < 10 :
        print( "Bilangan tersebut adalah bilangan gasal dan termasuk dalam nilai kecil")
    elif 10 <= masukkan <= 50 :
        print("Bilangan tersebut adalah bilangan gasal dan termasuk dalam nilai sedang")
    elif masukkan > 50 :
        print("Bilangan tersebut adalah bilangan gasal dan termasuk dalam nilai besar")

if angka == 0:
    if masukkan < 10 :
        print( "Bilangan tersebut adalah bilangan genap dan termasuk dalam nilai kecil")
    elif 10 <= masukkan <= 50 :
        print("Bilangan tersebut adalah bilangan genap dan termasuk dalam nilai sedang")
    elif masukkan > 50 :
        print("Bilangan tersebut adalah bilangan genap dan termasuk dalam nilai besar")