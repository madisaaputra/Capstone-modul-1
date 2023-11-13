from tabulate import tabulate

listPasien = [{'id': '1001', 'nama': 'Dimas', 'kamar': 'KM001', 'alamat': 'Bekasi', 'usia': 25, 'keterangan': 'Dirawat'},
              {'id': '1002', 'nama': 'Fahri', 'kamar': 'KM002', 'alamat': 'Depok', 'usia': 27, 'keterangan': 'Dirawat'},
              {'id': '1003', 'nama': 'Dedi', 'kamar': 'KM003', 'alamat': 'Jambi', 'usia': 22, 'keterangan': 'Dirawat'}]

trash = []

def tampilkanDaftarPasien():
    while True:
        print('''
            1. Tampilkan Daftar Seluruh Pasien
            2. Tampilkan Nama Pasien Melalui ID
            3. Kembali ke Menu Utama
            ''')
        pilihan = input("Masukkan Angka (1/2/3): ")

        if pilihan == '1':
            tampilkanDaftar(listPasien)
        elif pilihan == '2':
            cariId = input('Masukkan ID Pasien: ').upper()
            index = cariIndeksPasien(cariId)
            if index != -1:
                data = listPasien[index]
                cetakDataPasien(data)
        elif pilihan == '3':
            break


def tambahkanPasien():
    tampilkanDaftar()
    while True:
        print('''
            1. Pasien Masuk
            2. Kembali ke Menu Utama
            ''')
        pilihan = input("Masukkan angka (1/2): ")
        if pilihan == '1':
            tambah_ID = input('Masukkan ID Pasien: ').upper()
            index = cariIndeksPasien(tambah_ID)

            if index != -1:
                print('ID Pasien Sudah Ada, Pilih ID Lain')
                continue

            tambah_nama = input('Masukkan Nama Pasien: ').capitalize()
            tambah_kamar = input('Masukkan No Kamar: ').upper()
            tambah_alamat = input('Masukkan Alamat: ').capitalize()
            tambah_usia = int(input('Masukkan Usia: '))
            tambah_keterangan = input('Masukkan Keterangan Pasien: ').capitalize()
            
            temporary_table = {
                'id': tambah_ID,
                'nama': tambah_nama,
                'kamar': tambah_kamar,
                'alamat': tambah_alamat,
                'usia': tambah_usia,
                'keterangan': tambah_keterangan
            }

            res = lakukanTindakan(temporary_table,'input','tambah')
            if res:
                break

        elif pilihan == '2':
            break


def mengupdatePasien():
    
    while True:
        tampilkanDaftar() 
        print('''
                1. Update Nama
                2. Update Kamar
                3. Update Alamat
                4. Update Usia
                5. Update Keterangan
                6. Keluar
                ''')
        a = input("Pilihan (1/2/3/4/5/6): ")
        pilihan = {
            '1' : 'nama',
            '2' : 'kamar',
            '3' : 'alamat',
            '4' : 'usia',
            '5' : 'keterangan'
        }
        if a == '6':
            break
        dataBaru = str(input('Masukkan ID Pasien :')).upper()
        index = cariIndeksPasien(dataBaru)
        if index == -1 :
            print("Data Yang Di Cari Tidak Ada")
            continue
        ubahke = input(f"Ubah {pilihan[a]} Menjadi: ").capitalize()
        temp = {
            'index' : index,
            'data'  : listPasien[index].copy()

        }
        temp['data'][pilihan[a]] = ubahke
        res = lakukanTindakan(temp,'update','perbarui')
    


def menghapusPasien():
    while True:
        tampilkanDaftar()
        print('''
            1. Hapus Data Pasien
            2. Kembali ke Menu Utama
            ''')
        pilihan = input("Masukkan angka 1 atau 2: ")

        if pilihan == '1':
            tambah_ID = input('Masukkan ID Pasien: ').upper()
            index = cariIndeksPasien(tambah_ID)

            if index == -1:
                print('Pasien yang ingin dihapus tidak ada.')
                continue

            while True:
                checker = input("Yakin dihapus (y/n): ").upper()

                if checker == 'Y':
                    print("Data Pasien Telah Terhapus.")
                    trash.append(listPasien.pop(index))
                    break

                elif checker == 'N':
                    print("Batal dihapus.")
                    break

        elif pilihan == '2':
            break


def cekHistoryPasien():
    print('''
====> Pasien yang Telah Sehat
       ''')
    sampah = trash
    for i in range(len(sampah)):
        sampah[-1 * i]['keterangan'] = 'Sehat'

    tampilkanHistory(sampah)


def lakukanTindakan(data,aksi,pesan):
    checker = input(f"Mau {pesan} Y jika tidak N ? (y/n) =").upper()
    
    if(checker == 'N'):
        print(f"Data tidak Jadi di {pesan}")
        return 0
    if(aksi == 'input' and checker == 'Y'):
        print("Data Berhasil Tersimpan")
        listPasien.append(data)
        return 1
    if aksi == 'update' and checker == 'Y':
        print("Data Pasien Berhasil di Update")
        listPasien.pop(data['index'])
        listPasien.insert(data['index'],data['data'])
        return 1

    lakukanTindakan(data,aksi,pesan)


def cariIndeksPasien(dataBaru):
    for i in range(len(listPasien)):
        if listPasien[i]['id'] == dataBaru:
            return i
    return -1


def tampilkanHistory(data2):
    headers = ["ID", "Nama", "Kamar", "Alamat", "Usia", "Keterangan"]
    rows = []

    for i in range(len(data2)):
        rows.append([data2[i]['id'], data2[i]['nama'], data2[i]['kamar'],
                     data2[i]['alamat'], data2[i]['usia'], data2[i]['keterangan']])

    table = tabulate(rows, headers, tablefmt="fancy_grid")
    print(table)


def cetakDataPasien(data1):
    headers = ["ID", "Nama", "Kamar", "Alamat", "Usia", "Keterangan"]
    rows = [data1['id'], data1['nama'], data1['kamar'], data1['alamat'], data1['usia'], data1['keterangan']]
    table = tabulate([rows], headers, tablefmt="fancy_grid")
    print(table)


def tampilkanDaftar(pasien=listPasien):
    print('====> Daftar Pasien\n')
    headers = ["Index", "ID", "Nama", "Kamar", "Alamat", "Usia", "Keterangan"]
    rows = []

    for i in range(len(pasien)):
        rows.append([i + 1, pasien[i]['id'], pasien[i]['nama'], pasien[i]['kamar'],
                     pasien[i]['alamat'], pasien[i]['usia'], pasien[i]['keterangan']])

    table = tabulate(rows, headers, tablefmt="fancy_grid")
    print(table)


def menuUtama():
    while True:
        pilihanMenu = input('''
            Selamat Datang di Rumah Sakit Sehati

            List Menu :
            1. Melihat Daftar Pasien
            2. Pasien Masuk
            3. Update Data Pasien
            4. Pasien Keluar
            5. History
            6. Exit Program

            Masukkan Angka yang Ingin Dijalankan (1/2/3/4/5/6): ''')

        if pilihanMenu == '1':
            tampilkanDaftarPasien()
        elif pilihanMenu == '2':
            tambahkanPasien()
        elif pilihanMenu == '3':
            mengupdatePasien()
        elif pilihanMenu == '4':
            menghapusPasien()
        elif pilihanMenu == '5':
            cekHistoryPasien()
        elif pilihanMenu == '6':
            print("Terimakasih! Program Selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


menuUtama()
