#status untuk menentukan ujian kelulusan mahasisiwa

indo = int(input('Masukan nilai Bahasa Indonesia :'))
mtk = int(input('Masukan nilai Matematika :'))
ipa = int(input('Masukan nilai IPA :'))

print('====================================')

if(indo <= 0 or indo >= 100):
    print('Maaf nilai tidak valid')
elif(mtk <= 0 or mtk >= 100):
    print('Maaf nilai tidak valid')
elif(ipa <= 0 or ipa >= 100):
    print('Maaf nilai tidak valid')
    
elif(indo>60 and ipa>60 and mtk>70):
    print('Status kelulusan : LULUS')
else:
    print('Status kelulusan : TIDAK LULUS')
