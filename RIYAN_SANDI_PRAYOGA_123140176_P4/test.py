# Program Pengelolaan Data Nilai Mahasiswa (Tanpa Library Eksternal)

# Data awal mahasiswa (minimal 5)
mahasiswa_list = [
    {"nama": "Ahmad Rizki", "nim": "230101", "nilai_uts": 85, "nilai_uas": 90, "nilai_tugas": 88},
    {"nama": "Siti Nurhaliza", "nim": "230102", "nilai_uts": 75, "nilai_uas": 80, "nilai_tugas": 78},
    {"nama": "Budi Santoso", "nim": "230103", "nilai_uts": 60, "nilai_uas": 65, "nilai_tugas": 70},
    {"nama": "Dina Maulida", "nim": "230104", "nilai_uts": 45, "nilai_uas": 50, "nilai_tugas": 55},
    {"nama": "Eko Prasetyo", "nim": "230105", "nilai_uts": 90, "nilai_uas": 92, "nilai_tugas": 89}
]

def hitung_nilai_akhir(uts, uas, tugas):
    return round(0.3 * uts + 0.4 * uas + 0.3 * tugas, 2)

def tentukan_grade(nilai_akhir):
    if nilai_akhir >= 80:
        return 'A'
    elif nilai_akhir >= 70:
        return 'B'
    elif nilai_akhir >= 60:
        return 'C'
    elif nilai_akhir >= 50:
        return 'D'
    else:
        return 'E'

def tampilkan_data(mahasiswa_list):
    if not mahasiswa_list:
        print("Tidak ada data mahasiswa untuk ditampilkan.\n")
        return

    print("\n" + "="*95)
    print(f"{'Nama':<18} {'NIM':<10} {'UTS':<5} {'UAS':<5} {'Tugas':<7} {'Nilai Akhir':<12} {'Grade'}")
    print("="*95)
    for mhs in mahasiswa_list:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        grade = tentukan_grade(nilai_akhir)
        print(f"{mhs['nama']:<18} {mhs['nim']:<10} {mhs['nilai_uts']:<5} {mhs['nilai_uas']:<5} {mhs['nilai_tugas']:<7} {nilai_akhir:<12} {grade}")
    print("="*95 + "\n")

def cari_nilai_ekstrem(mahasiswa_list, tipe="tertinggi"):
    if not mahasiswa_list:
        print("Tidak ada data mahasiswa.\n")
        return None

    def nilai(m): return hitung_nilai_akhir(m['nilai_uts'], m['nilai_uas'], m['nilai_tugas'])
    if tipe == "tertinggi":
        mahasiswa = max(mahasiswa_list, key=nilai)
        print("\nMahasiswa dengan Nilai Tertinggi:")
    else:
        mahasiswa = min(mahasiswa_list, key=nilai)
        print("\nMahasiswa dengan Nilai Terendah:")

    nilai_akhir = nilai(mahasiswa)
    grade = tentukan_grade(nilai_akhir)
    print(f"Nama        : {mahasiswa['nama']}")
    print(f"NIM         : {mahasiswa['nim']}")
    print(f"Nilai Akhir : {nilai_akhir}")
    print(f"Grade       : {grade}\n")
    return mahasiswa

def input_mahasiswa_baru():
    print("\n--- Input Data Mahasiswa Baru ---")
    nama = input("Nama: ").strip()
    nim = input("NIM: ").strip()
    try:
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        tugas = float(input("Nilai Tugas: "))
        if not (0 <= uts <= 100 and 0 <= uas <= 100 and 0 <= tugas <= 100):
            print("Nilai harus antara 0 - 100. Data tidak ditambahkan.\n")
            return
        mahasiswa_list.append({
            "nama": nama, "nim": nim,
            "nilai_uts": uts, "nilai_uas": uas, "nilai_tugas": tugas
        })
        print("Data mahasiswa berhasil ditambahkan!\n")
    except ValueError:
        print("Input nilai harus berupa angka. Data tidak ditambahkan.\n")

def filter_berdasarkan_grade(grade):
    hasil = []
    for mhs in mahasiswa_list:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        if tentukan_grade(nilai_akhir) == grade.upper():
            hasil.append(mhs)
    return hasil

def hitung_rata_rata():
    if not mahasiswa_list:
        return 0
    total = sum(hitung_nilai_akhir(m['nilai_uts'], m['nilai_uas'], m['nilai_tugas']) for m in mahasiswa_list)
    return round(total / len(mahasiswa_list), 2)

def menu_utama():
    while True:
        print("\n=== PROGRAM PENGELOLAAN DATA NILAI MAHASISWA ===")
        print("1. Tampilkan Semua Data")
        print("2. Tambah Data Mahasiswa Baru")
        print("3. Cari Mahasiswa dengan Nilai Tertinggi")
        print("4. Cari Mahasiswa dengan Nilai Terendah")
        print("5. Filter Mahasiswa Berdasarkan Grade (A/B/C/D/E)")
        print("6. Hitung Rata-rata Nilai Kelas")
        print("7. Keluar")
        
        pilihan = input("Pilih menu (1-7): ").strip()
        
        if pilihan == '1':
            tampilkan_data(mahasiswa_list)
        elif pilihan == '2':
            input_mahasiswa_baru()
        elif pilihan == '3':
            cari_nilai_ekstrem(mahasiswa_list, "tertinggi")
        elif pilihan == '4':
            cari_nilai_ekstrem(mahasiswa_list, "terendah")
        elif pilihan == '5':
            grade_filter = input("Masukkan grade (A/B/C/D/E): ").strip().upper()
            if grade_filter in ['A','B','C','D','E']:
                hasil = filter_berdasarkan_grade(grade_filter)
                if hasil:
                    tampilkan_data(hasil)
                else:
                    print(f"Tidak ada mahasiswa dengan grade {grade_filter}.\n")
            else:
                print("Grade tidak valid.\n")
        elif pilihan == '6':
            print(f"\nRata-rata Nilai Kelas: {hitung_rata_rata()}\n")
        elif pilihan == '7':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    menu_utama()