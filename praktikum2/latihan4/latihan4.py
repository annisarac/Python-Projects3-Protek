#Program untuk menentukan gaji karyawan

kode = input('Masukan kode karyawan :')
nama = input('Masukan nama karyawan :')
golongan = input('Masukan golongan :')

print('=========================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('-----------------------------------------')
print('Nama karyawan :' + nama + ('(kode:' + kode + ')'))
print('Golongan :' + golongan)
print('-----------------------------------------')

if(golongan == 'A'):
    gajiPokok = 10000000
    potongan = 2.5
    potonganGaji = gajiPokok*potongan/100
    gajiBersih = gajiPokok-potonganGaji
elif(golongan == 'B'):
    gajiPokok = 8500000
    potongan = 2.0
    potonganGaji = gajiPokok*potongan/100
    gajiBersih = gajiPokok-potonganGaji
elif(golongan == 'C'):
    gajiPokok = 7000000
    potongan = 1.5
    potonganGaji = gajiPokok*potongan/100
    gajiBersih = gajiPokok-potonganGaji
elif(golongan == 'D'):
    gajiPokok = 5500000
    potongan = 1.0
    potonganGaji = gajiPokok*potongan/100
    gajiBersih = gajiPokok-potonganGaji
print('Gaji pokok : Rp' + str(gajiPokok))
print('Potongan (' + str(potongan) + '%) : Rp' + str(potonganGaji))
print('-----------------------------------------')
print('Gaji bersih : Rp ' + str(gajiBersih))
