# masukin data awal sesuai soal
dictAwal = {'Nama': 'Bonang Respati S.',
        'Hobi 1': 'Membaca',
        'Hobi 2': 'Tidur',
        'Hobi 3': 'Bermain game',
        'Media sosial 1': '@bonangrs (IG)',
        'Media sosial 2': '@bonangrs (Twitter)',
        'Media sosial 3': 'LINE satbonang',
        'Lagu favorit 1': 'Sayang - Via Vallen',
        'Lagu favorit 2': 'Perlahan - GuyonWaton',
        'Lagu favorit 3': 'Rahasia - Payung Teduh',
        'Makanan favorit 1': 'Sate kambing',
        'Makanan favorit 2': 'Mie yamin',
        'Makanan favorit 3': 'Nasi goreng'}

dictAwal['Hobi 2'] = 'Menonton YouTube'     # ubah hobi
dictAwal['Media sosial 3'] = 'Bonang Respati (FB)'      # ubah medsos
dictAwal.pop('Makanan favorit 2')       # hapus makanan favorit
del dictAwal['Makanan favorit 3']       # hapus makanan favorit
dictAwal.update({'Hobi 4': 'Bermaain Lego'})      # tambah hobi

listAwal = []                # inisiasi awal
for k,v in dictAwal.items():     # k utk key, v utk value
    listAwal.append((str(k) + ": " + str(v)))

listNama = []           #inisiasi awal
listHobi = []
listMedsos = []
listMakanan = []
listLagu = []

for x in listAwal:  # ngebagi list awal yg msh acak ke list per bagian(nama, hobi, medsos, dll)
    if 'Hobi' in x:
        listHobi.append(x)
        # listHobi.sort()   # bisa di-sort buat urutin
    if 'Nama' in x:
        listNama.append(x)
    if 'Media' in x:
        listMedsos.append(x)
    if 'Lagu' in x:
        listLagu.append(x)
    if 'Makanan' in x:  # klo pake else hasilnya ngulang lagi dari awal, jdnya pake if
        listMakanan.append(x)

listFinal = listNama + listHobi + listMedsos + listLagu + listMakanan   # gabungin list per bagian mjd 1 list

for kelar in listFinal:
    print(kelar)

