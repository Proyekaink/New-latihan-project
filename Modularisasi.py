""""""
print('Menghitung luas segitiga')
""""""
alas = 20
tinggi = 10
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas {alas} dan tinggi {tinggi} mendapatkan luas {luas_segitiga}')

alas = 20
tinggi = 5
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas {alas} dan tinggi {tinggi} mendapatkan luas {luas_segitiga}')

print('\nMembuat fungsi luas segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(20, 10)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(20, 5)}')

