from db import creat_table,add_user,get_users,delete_user,update_user,add_order,get_all_user_and_order,get_order,delete_order
creat_table()
def normal(text:str):
    return text.strip().lower()
def lj():
    input("\nEnter untuk lanjut..")
def gavalid():
    print("Inputan tidak valid!")
    lj()
def input_angka(teks="Masukan angka: "):
    while True:
        angka = input(f"{teks}").strip().capitalize()
        if angka.isdigit():
            return int(angka)
        gavalid()
def input_str(teks="Masukan teks: "):
    while True:
        x = input(f"{teks}")
        if x.strip() == '':
            gavalid()
            continue
        return x

                
def tambah_user():
    while True:
        name = input("Input nama user: ")
        email = input("Input email user: ")

        if name.strip() == '' or email.strip() == '':
            gavalid()
            continue

        keberhasilan = add_user(name,email)
        if keberhasilan:
            print("--- User berhasil di tambahkan")
        else:
            print("Email sudah berada pada daftar, mohon ulangi")
            lj()
            continue

        break

def tampilkan_users():
    data_users = get_users()
    print("")
    print("----------------------")
    for i in data_users:
        print(f"ID: {i[0]}")
        print(f"User: {i[1]}")
        print(f"Email: {i[2]}")
        print("----------------------")
    print("")
    
    
def update_data_user():
    id_user = input_angka("Masukan id yang ingnin di update: ")
    name = input("Masukan nama baru: " )
    email = input("Masukan email baru: " )
    keberhasilan = update_user(name,email,id_user)
    if keberhasilan:
        print("--- data berhasil di Update")
    else:
        print(f"data user dengan id: {id_user},tidak di temukan")

def hapus_user():
    id_user = input_angka("masukan id user yang ingin di hapus: ")
    print(type(id_user))
    keberhasilan = delete_user(id_user)
    if keberhasilan:
        print("--- data berhasil di hapus")
    else:
        print(f"data user dengan id: {id_user},tidak di temukan")

def tambah_orderan():
    id_user = input_angka("Masukan id user yang melakukan order: ")
    produk = input_str("Masukan nama produk: ")
    price = input_angka("Masukan harga produk: ")
    if produk is None:
        print("Masukan nama produk terlebih dulu ")
        return
    
    keberhasilan = add_order(id_user,produk,price)
    if keberhasilan:
        print("--- data order berhasil di buat")
    else:
        print(f"data user dengan id: {id_user},tidak di temukan")

def tampilkan_semua_user_serta_order():
    data = get_all_user_and_order()
    user = 'kosong'
    for indx,i in enumerate(data):
        if i[0] != user :
            user = i[0]
            print(f"\n{indx+1}. User: {user}, ID: {i[2]}")
    
        if not (i[1] is None):
            print(f"  - {i[1]} ({i[3]})")
        else:
            print("  - Tidak ada orderan")

def tampilkan_data_user_yang_order():
    data = get_order()
    user = 'kosong'
    for indx,i in enumerate(data):
        if i[0] != user :
            user = i[0]
            print(f"\n{indx+1}. User: {user}, ID: {i[2]}")

        print(f"  - {i[1]} ({i[3]}), id_order: {i[4]}")

def menghapus_data_orderan():
    id_orderan = input_angka("Masukan id orderan yang ingin di hapus: ")

    keberhasilan = delete_order(id_orderan)
    if keberhasilan:
        print("--- data order berhasil di hapus")
    else:
        print(f"data order dengan id: {id_orderan},tidak di temukan")


def main():
    while True:
        print("""
1. Tambah user
2. Lihat semua user
3. Update user
4. Hapus user
5. Tambah orderan
6. Tampilkan semua user serta orderannya
7. Tampilkan semua data user yang memiliki orderan
8. Hapus orderan
9. Keluar
    """)
        pilihan = normal(input("Input pilihan: "))

        if pilihan == '1':
            tambah_user()
        elif pilihan == '2':
            tampilkan_users()
        elif pilihan == '3':
            update_data_user()
        elif pilihan == '4':
            hapus_user()
        elif pilihan == '5':
            tambah_orderan()
        elif pilihan == '6':
            tampilkan_semua_user_serta_order()
        elif pilihan == '7':
            tampilkan_data_user_yang_order()
        elif pilihan == '8':
            menghapus_data_orderan()
        elif pilihan == '9':
            return
        else:
            gavalid()

main()
