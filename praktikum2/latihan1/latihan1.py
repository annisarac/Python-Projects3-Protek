#status untuk menentukan ujian kelulusan mahasisiwa

indo = int(input('Masukan nilai Bahasa Indonesia :'))
if(indo >= 0 and indo <= 100):
    mtk = int(input('Masukan nilai Matematika :'))
if(mtk >= 0 and mtk <= 100):
    ipa = int(input('Masukan nilai IPA :'))
if(ipa >= 0 and ipa <= 100):
    print('=============================')

if(indo > 60 and ipa > 60 and mtk > 70):
    print('Status Kelulusan : LULUS')
else:
    print('Status Kelulusan : TIDAK LULUS')
