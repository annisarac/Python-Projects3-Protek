#Program untuk menentukan gaji karyawan

kode = input('Masukan kode karyawan :')
nama = input('Masukan nama karyawan :')
golongan = input('Masukan golongan :')
status = input('Masukan status (1: menikah, 2: belum) :')
if(status == '1'):
    jumlahAnak = int(input('Masukan jumlah anak :'))
    nikah = 'Sudah menikah'
    tunjanganIstri = 10/100
    tunjanganAnak = 5/100*jumlahAnak
else:
    jumlahAnak = 0
    blmNikah = 'Belum menikah'
    tunjanganIstri = 0
    tunjanganAnak = 0

print('=========================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('-----------------------------------------')
print('Nama karyawan :' + nama + ('(kode:' + kode + ')'))
print('Golongan :' + golongan)
print('Status menikah :' + nikah)
print('Jumlah anak :' + str(jumlahAnak))
print('-----------------------------------------')

if(golongan == 'A'):
    gajiPokok = 10000000
    potongan = 2.5
    jumlahtunjanganMenikah = tunjanganIstri*gajiPokok
    jumlahtunjanganAnak = tunjanganAnak*gajiPokok
    gajiKotor = gajiPokok + jumlahtunjanganMenikah + jumlahtunjanganAnak 
    potonganGaji = gajiKotor*potongan/100
    gajiBersih = gajiPokok-potonganGaji
elif(golongan == 'B'):
    gajiPokok = 8500000
    potongan = 2.0
    jumlahtunjanganMenikah = tunjanganIstri*gajiPokok
    jumlahtunjanganAnak = tunjanganAnak*gajiPokok
    gajiKotor = gajiPokok + jumlahtunjanganMenikah + jumlahtunjanganAnak 
    potonganGaji = gajiKotor*potongan/100
    gajiBersih = gajiPokok-potonganGaji
elif(golongan == 'C'):
    gajiPokok = 7000000
    potongan = 1.5
    jumlahtunjanganMenikah = tunjanganIstri*gajiPokok
    jumlahtunjanganAnak = tunjanganAnak*gajiPokok
    gajiKotor = gajiPokok + jumlahtunjanganMenikah + jumlahtunjanganAnak 
    potonganGaji = gajiKotor*potongan/100
    gajiBersih = gajiPokok-potonganGaji
elif(golongan == 'D'):
    gajiPokok = 5500000
    potongan = 1.0
    jumlahtunjanganMenikah = tunjanganIstri*gajiPokok
    jumlahtunjanganAnak = tunjanganAnak*gajiPokok
    gajiKotor = gajiPokok + jumlahtunjanganMenikah + jumlahtunjanganAnak 
    potonganGaji = gajiKotor*potongan/100
    gajiBersih = gajiPokok-potonganGaji
print('Gaji pokok : Rp' + str(gajiPokok))
print('Tunjangan istri/suami :' + str(jumlahtunjanganMenikah))
print('Tunjangan anak :' + str(jumlahtunjanganAnak))
print('-----------------------------------------')
print('Gaji kotor :' + str(gajiKotor))
print('Potongan (' + str(potongan) + '%) : Rp' + str(potonganGaji))
print('-----------------------------------------')
print('Gaji bersih : Rp ' + str(gajiBersih))
