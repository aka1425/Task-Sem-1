# OLEH-OLEH 08/09/23 (Muhammad Aka Sahadi 232410102028)
# NO.1
ini_list = [2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2]
print(f"{ini_list[7:9]}") # Done

# NO.2
Arr1 = [1,2,3,4]
Arr2 = [5,6,7,8]
Arr1.remove(1)
Arr1.pop(1)
Arr2.remove(5)
Arr2.pop(1)
Arr1.reverse()
Arr2.reverse()
print(f"{Arr2 + Arr1}") # Done

# NO.3
word1 = "Hello"
word2 = "World"
print(f"{word1[:1] + word2[:1] + word1[1:2] + word2[1:2] + word1[2:3] + word2[2:3] + word1[3:4] + word2[3:4] + word1[4:5] + word2[4:5]}") # Done

# NO.4
Hari = ["rabu","jum'at","senin","minggu","sabtu","selasa","kamis"]
Hari_Fix =[]
Hari_Fix = Hari
print(Hari_Fix[3:4] + Hari_Fix[2:3] + Hari_Fix[5:6] + Hari_Fix[0:1] + Hari_Fix[6:] + Hari_Fix[1:2] + Hari_Fix[4:5]) # Done

# NO.5
ini_string = '1''2''3''4''5''6''7''8''9''10'
casting_ke_integer = int(ini_string)
ini_baru = [casting_ke_integer]
print(ini_baru) #Done