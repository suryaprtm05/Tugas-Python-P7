def main():
    while True:
        print("\nNim Genap")
        print("menu pilihan")
        print("1. Barisan Fibonacci")
        print("2. M Kali N")
        print("0. Keluar")
        
        pilihan = input("Pilih Menu : ")

        if pilihan == '1':
            n_terms = int(input("Masukkan Jumlah Suku : "))
            
            # Logika Fibonacci
            n1, n2 = 1, 1
            count = 0
            
            if n_terms <= 0:
                print("Silahkan masukkan angka positif")
            else:
                print(f"barisan fibonacci sebanyak {n_terms} suku :")
                fib_list = []
                while count < n_terms:
                    fib_list.append(str(n1))
                    nth = n1 + n2
                    n1 = n2
                    n2 = nth
                    count += 1
                print(", ".join(fib_list))

        elif pilihan == '2':
            m = int(input("Masukkan Suatu Bilangan Bulat : "))
            n = int(input("Masukkan Suatu Bilangan Pengali : "))
            hasil = m * n
            print(f"\n{m} x {n} = {hasil}")

        elif pilihan == '0':
            print("Keluar dari program...")
            break
        
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()