#program untuk tebak angka
print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')

tebak = int(input('Tebakan anda :'))

while True:
    if(tebak<10):
        print('Hehehee... Bilangan tebakan anda terlalu kecil')
        tebak = int(input('Tebakan anda :'))
    elif(tebak>10):
        print('Hehehee... Bilangan tebakan anda terlalu besar')
        tebak = int(input('Tebakan anda :'))
    elif(tebak == 10):
        print('Yeeee… Bilangan tebakan anda BENAR :-)')
        break
        
    
