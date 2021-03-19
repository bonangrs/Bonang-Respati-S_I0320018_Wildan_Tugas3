listTeman = ['Safri', 'Zaneta', 'Yola', 'Maurich', 'Yuku', 'Vizal', 'Densur', 'Fajri', 'Sekar', 'Zapira']

print('Nama teman saya yang berada di indeks 4 adalah', listTeman[4])
print('Nama teman saya yang berada di indeks 6 adalah', listTeman[6])
print('Nama teman saya yang berada di indeks 7 adalah', listTeman[7])

listTeman[3] = "Toni"  # mengganti nama teman di indeks 3, 5, dan 9
listTeman[5] = "Dika"
listTeman[9] = "Aril"

listTeman.extend(["Eca", "Nabil"])

print("Teman-teman saya bernama", end=" ")  # menampilkan nama-nama teman
for namaTeman in listTeman:
    if namaTeman == listTeman[-1]:
        print(namaTeman, end='. \n')
        break
    if namaTeman == listTeman[-2]:
        print(namaTeman, end=', dan ')
    else:
        print(namaTeman, end=', ')

print("Jumlah nama teman dalam list: ", len(listTeman))
