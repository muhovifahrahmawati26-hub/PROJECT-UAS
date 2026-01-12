#CLASS DATA

class Mahasiswa:
    def __init__(self, nama, nim, tugas, uts, uas,):
        self.nama = nama
        self.nim = nim
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.nilai_akhir = self.hitung_nilai_akhir()

    def hitung_nilai_akhir(self):
        return (0.3 * self.tugas) + (0.3 * self.uts) + (0.4 * self.uas)

#CLASS PROCESS

class MahasiswaProcess:
    def __init__(self):
        self.data = []

    def validasi_nilai(self, nilai):
        if nilai < 0 or nilai > 100:
            raise ValueError("Nilai harus antara 0 - 100")

    def tambah(self, nama, nim, tugas, uts, uas):
        if not nama.replace(" ", "").isalpha():
            raise ValueError("Nama harus berupa huruf")

        if not nim.isdigit():
            raise ValueError("NIM harus berupa angka")

        self.validasi_nilai(tugas)
        self.validasi_nilai(uts)
        self.validasi_nilai(uas)

        self.data.append(Mahasiswa(nama, nim, tugas, uts, uas))

    def edit(self, nim, tugas, uts, uas):
        for mhs in self.data:
            if mhs.nim == nim:
                self.validasi_nilai(tugas)
                self.validasi_nilai(uts)
                self.validasi_nilai(uas)

                mhs.tugas = tugas
                mhs.uts = uts
                mhs.uas = uas
                mhs.nilai_akhir = mhs.hitung_nilai_akhir()
                return True
        return False

    def get_data(self):
        return self.data

# CLASS VIEW

class MahasiswaView:
    def menu(self):
        print("\n" + "=" * 60)
        print("      SISTEM PENILAIAN MAHASISWA")
        print("=" * 60)
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data")
        print("3. Edit Nilai Mahasiswa")
        print("4. Keluar")
        print("=" * 60)

    def tampilkan_tabel(self, data):
        if not data:
            print("\nData masih kosong!")
            return

        print("\n" + "=" * 95)
        print(f"{'No':<4}{'Nama':<20}{'NIM':<12}{'Tugas':<8}{'UTS':<8}{'UAS':<8}{'Nilai Akhir':<12}")
        print("=" * 95)

        for i, mhs in enumerate(data, start=1):
            print(f"{i:<4}{mhs.nama:<20}{mhs.nim:<12}"
                  f"{mhs.tugas:<8.1f}{mhs.uts:<8.1f}{mhs.uas:<8.1f}"
                  f"{mhs.nilai_akhir:<12.2f}")

        print("=" * 95)

# PROGRAM UTAMA

def main():
    process = MahasiswaProcess()
    view = MahasiswaView()

    while True:
        view.menu()
        pilihan = input("Pilih menu (1-4): ")

        try:
            if pilihan == "1":
                print("\n--- Tambah Data Mahasiswa ---")
                nama = input("Nama  : ")
                nim = input("NIM   : ")
                tugas = float(input("Nilai Tugas : "))
                uts = float(input("Nilai UTS   : "))
                uas = float(input("Nilai UAS   : "))

                process.tambah(nama, nim, tugas, uts, uas)
                print("Data berhasil ditambahkan!")

            elif pilihan == "2":
                view.tampilkan_tabel(process.get_data())

            elif pilihan == "3":
                print("\n--- Edit Nilai Mahasiswa ---")
                nim = input("Masukkan NIM yang akan diedit: ")
                tugas = float(input("Nilai Tugas Baru : "))
                uts = float(input("Nilai UTS Baru   : "))
                uas = float(input("Nilai UAS Baru   : "))

                if process.edit(nim, tugas, uts, uas):
                    print("Data berhasil diperbarui!")
                else:
                    print("Data dengan NIM tersebut tidak ditemukan!")

            elif pilihan == "4":
                print("\nTerima kasih, program selesai.")
                break

            else:
                print("Menu tidak valid!")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()