# membuat dict
dictAwal = {'Nama': 'Bonang Respati S.',
        'Hobi': ['baca buku', 'tidur', 'main game'],
        'Twitter': '@bonangrs',
        'IG': '@bonangrs',
        'LINE': 'satbonang',
        'Lagu favorit': ['Sayang - Via Vallen',
                         'Perlahan - GuyonWaton',
                         'Rahasia - Payung Teduh'],
        'Makanan favorit': ['nasi goreng', 'mie yamin', 'sate kambing'] }

dictAwal['Hobi'][1] = 'menonton youtube'            # mengubah value hobi
dictAwal['FB'] = dictAwal.pop('LINE')               # mengganti key media sosial
dictAwal['FB'] = 'Bonang Respati'                   # menambahkan value media sosial
dictAwal['Makanan favorit'].remove('nasi goreng')   # menghapus value
dictAwal['Makanan favorit'].remove('mie yamin')
dictAwal['Hobi'].append('belajar')                  # menambahkan hobi

print(dictAwal)

