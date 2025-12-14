from db import creat_table,add_user,get_users,delete_user,update_user
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
        angka = input(f"{teks}")
        if angka.isdigit():
            return int(angka)
        gavalid()

                
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

def main():
    while True:
        print("""
1. Tambah user
2. Lihat semua user
3. Update user
4. Hapus user
5. Keluar
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
            return
        else:
            gavalid()

main()
