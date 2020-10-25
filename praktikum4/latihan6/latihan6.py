#program untuk tebak angka
print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')

tebak = int(input('Tebakan anda :'))
poin = 0
while True:
    if(tebak<10):
        print('Hehehee... Bilangan tebakan anda terlalu kecil')
        tebak = int(input('Tebakan anda :'))
        poin += 2
    elif(tebak>10):
        print('Hehehee... Bilangan tebakan anda terlalu besar')
        tebak = int(input('Tebakan anda :'))
        poin += 2
    elif(tebak == 10):
        print('Yeeee… Bilangan tebakan anda BENAR :-)')
        score = 100 - poin
        break
print('Score anda :' + str(score))
  
        
