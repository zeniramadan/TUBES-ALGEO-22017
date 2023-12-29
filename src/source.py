import numpy as np

class Matrikskal: 
    def _init_(self):
        pass

    def menu(self): 
        while True:
            print("\n::IF III A MATRIKS CALCULATOR::")
            print("1. Penjumlahan dan Pengurangan matriks")
            print("2. Transpose Matriks")
            print("3. Determinan Matriks")
            print("4. Matriks balikan")
            print("5. Solusi SPL")
            print("6. Keluar")

            choice = int(input("Masukan Menu Pilihanmu: "))
            if choice == 6:
                exit(0)
            elif choice == 1:
                self.tambah_kurang_menu()
            elif choice == 2:
                self.transpose_menu()
            elif choice == 3:
                self.determinan_menu()
            elif choice == 4:
                self.matriks_balikan()
            elif choice == 5:
                self.spl()
            else:
                print("Pilihan tidak valid, coba lagi")

    def tambah_kurang_menu(self): 
        while True: 
            print("\n:: Penjumlahan dan Pengurangan Matriks ::")    
            print("1. Penjumlahan Matriks")                         
            print("2. Pengurangan Matriks")                                             
            print("3. Kembali ke Menu Utama")                       
            choice = int(input("Masukan Pilihanmu (1-3): ")) 
            if choice == 3:
                break

            size = 2 

            matriks1 = self.input_matriks(f"\nMasukan Matriks 1 ({size}x{size}):", size) 
            matriks2 = self.input_matriks(f"\nMasukan Matriks 2 ({size}x{size}):", size) 

            if choice == 1:
                hasil = self.matriks_tambah(matriks1, matriks2) 
                print("\nPertambahan Matriks:")
                self.print_matriks(hasil) 
            elif choice == 2:
                hasil = self.matriks_kurang(matriks1, matriks2) 
                print("\nPengurangan Matriks:")
                self.print_matriks(hasil) 
            else:
                print("masukan antara angka 1-3")

    def matriks_tambah(self, mat1, mat2): 
        hasil = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                hasil[i][j] = mat1[i][j] + mat2[i][j]
        return hasil
    
    def matriks_kurang(self, mat1, mat2): 
        hasil = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                hasil[i][j] = mat1[i][j] - mat2[i][j]
        return hasil
          
    
    def transpose_menu(self): 
        while True: 
            print("\n:: Transpose Matriks ::")
            print("1. Matriks 2x2")
            print("2. Matriks 3x3")
            print("3. Kembali ke Menu Utama")
            
            choice = int(input("Masukan Pilihanmu (1-3): "))
            if choice == 3:
                break
            if choice == 1:
                size = 2

                matriks = self.input_matriks(f"Masukan Matriks ({size}x{size}):", size) 
                print(f"\nMatriks Awal ({size}x{size}):")
                self.print_matriks(matriks) 

                transposed_matriks = self.transpose_matriks(matriks) 
                print("\nMatriks Transpose:")
                self.print_matriks(transposed_matriks) 

            elif choice == 2:
                size = 3
            
                matriks = self.input_matriks(f"Masukan Matriks ({size}x{size}):", size) 
                print(f"\nMatriks Awal ({size}x{size}):")
                self.print_matriks(matriks) 

                transposed_matriks = self.transpose_matriks1(matriks) 
                print("\nMatriks Transpose:")
                self.print_matriks(transposed_matriks) 
            else:
                print("masukan antara angka 1-3")

    def transpose_matriks(self, matriks): 
        transposed_matriks = [[0, 0], [0, 0]]

        for i in range(2):
            for j in range(2):
                transposed_matriks[j][i] = matriks[i][j]

        return transposed_matriks
    
    def transpose_matriks1(self, matriks):
        transposed_matriks1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(3):
            for j in range(3):
                transposed_matriks1[j][i] = matriks[i][j]

        return transposed_matriks1
    
    def determinan_menu(self): 
        while True: 
            print("\n:: Determinan Matriks ::")
            print("1. Matriks 2x2")
            print("2. Matriks 3x3")
            print("3. Kembali ke Menu Utama")
            # menu
            choice = int(input("Masukan Pilihanmu (1-2): "))
            if choice == 3:
                break
            if choice == 1:
                size = 2

                matriks = self.input_matriks(f"Masukan Matriks ({size}x{size}):", size) 
                print(f"\nMatriks Awal ({size}x{size}):")
                self.print_matriks(matriks) 

                determinan_value = self.hitung_determinan(matriks) 
                print(f"\nDeterminan dari matriks ({size}x{size}):", determinan_value) 
            elif choice == 2:
                size = 3

                matriks = self.input_matriks(f"Masukan Matriks ({size}x{size}):", size) 
                print(f"\nMatriks Awal ({size}x{size}):")
                self.print_matriks(matriks)

                determinan_value = self.hitung_determinan1(matriks)
                
                print(f"\nDeterminan dari matriks ({size}x{size}):", determinan_value) 
            else:
                print("masukan antara angka 1-3")

    def hitung_determinan(self, matriks): 
        determinan = matriks[0][0] * matriks[1][1] - matriks[0][1] * matriks[1][0] 
        return determinan
    
    def hitung_determinan1(self, matriks):
        determinan = (
            matriks[0][0] * (matriks[1][1] * matriks[2][2] - matriks[1][2] * matriks[2][1]) -
            matriks[0][1] * (matriks[1][0] * matriks[2][2] - matriks[1][2] * matriks[2][0]) +
            matriks[0][2] * (matriks[1][0] * matriks[2][1] - matriks[1][1] * matriks[2][0])

        )
        return determinan
        
    
    def matriks_balikan(self):
        size = 2
        matriks = self.input_matriks(f"Masukan Matriks ({size}x{size}):", size) 
        print(f"\nMatriks Awal ({size}x{size}):")
        self.print_matriks(matriks)
        balikan_matriks = self.hitung_balikan(matriks) 

        if balikan_matriks is not None: 
            print("\nBalikan Matriks:")
            self.print_matriks(balikan_matriks) 
        else:
            print("\nMatriks tidak invertible.")

    def hitung_balikan(self, matriks):
        determinan = matriks[0][0] * matriks[1][1] - matriks[0][1] * matriks[1][0] 

        if determinan == 0:
            return None 

        balikan_matriks = [
            [matriks[1][1] / determinan, -matriks[0][1] / determinan],
            [-matriks[1][0] / determinan, matriks[0][0] / determinan]
        ]
        
        return balikan_matriks

    def spl(self):
        size = 2
        koef = self.input_matriks(f"\nMasukan Matriks Koefisien (2x3):", size) 
        print("made by kelompok 3")
        kons = [float(input(f"Masukan Konstanta {i + 1}: ")) for i in range(size)] 

        solution = self.hitung_spl(koef, kons) 

        if solution is not None and not np.isnan(solution).any(): 
            print("\nSolusi SPL adalah: ")
            for i, val in enumerate(solution): 
                print(f'x{i + 1} = {val:.2f}') 
        else:
            print("\nSPL tidak mempunyai solusi atau solusi tidak valid.") 

    def hitung_spl(self, koef, kons):
        try:
            solusi = np.linalg.solve(koef, kons) 
            return solusi
        except np.linalg.LinAlgError:
            return None
    
    def input_matriks(self, prompt, size):
        matriks = []
        print(prompt)

        for i in range(size):
            baris = []
            for j in range(size):
                elemen = float(input(f"Masukan elemen ({i + 1}, {j + 1}): ")) 
                baris.append(elemen)
            matriks.append(baris)

        return matriks

    def print_matriks(self, mat):
        for baris in mat: 
            print(baris)

def main():
    kalkulator = Matrikskal() 
    kalkulator.menu() 

if __name__ == "__main__":
    main()