from anomali.persegipanjang import hitung_luas_persegpanjang, info as info_persegipanjang
from anomali.segitiga import hitung_luas_segitiga, info as info_segitiga
from anomali.vbalok import hitung_volume_balok, info as info_balok
print('-'*10)
print(info_segitiga())
print(f'hitung_luas_segitiga = {hitung_luas_segitiga(20, 60)}')
print('-'*10)
print(info_persegipanjang())
print(f'hitung_luas_persegipanjang = {hitung_luas_persegpanjang(20, 20)}')
print('-'*10)
print(info_balok())
print(f'hitung_volume_balok = {hitung_volume_balok(25, 10, 6)}')
