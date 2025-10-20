# Implementasi Pipeline Enkripsi AES-CFB dengan Playfair dan Vigenere

Proyek ini mengimplementasikan sistem enkripsi pipeline yang menggabungkan tiga algoritma kriptografi: Playfair Cipher, Vigenere Autokey Cipher, dan AES-CFB. Sistem ini dirancang untuk mengenkripsi file dengan aman menggunakan kombinasi algoritma klasik dan modern.

# Alur Kerja Sistem

# 1. Pembangkitan Kunci AES dan IV
- User memasukkan kunci (key) yang akan digunakan untuk proses enkripsi
- Sistem menggunakan kunci tersebut untuk:
  - Mengenkripsi teks "KRIPTOGRAFI PLAYFAIR" menggunakan Playfair Cipher
  - Mengenkripsi teks "KRIPTOGRAFI VIGENERE" menggunakan Vigenere Autokey Cipher
- Hasil enkripsi Playfair digunakan sebagai kunci AES (16 byte pertama)
- Hasil enkripsi Vigenere digunakan sebagai IV (16 byte pertama)


# 2. Proses Enkripsi File
1. Klik tombol "Choose File" dan pilih file yang ingin dienkripsi (bisa berupa file teks, dokumen, gambar, dll).
2. Masukkan kunci enkripsi (key) sesuai keinginan.
3. Klik tombol "Encrypt" pada aplikasi web.
4. Sistem akan membangkitkan kunci AES dan IV dari kunci yang  dimasukkan.
5. File akan dienkripsi menggunakan algoritma AES mode CFB, dan hasil enkripsi akan disimpan dalam format hexadecimal.
6. File hasil enkripsi akan otomatis diunduh ke komputer dengan ekstensi tambahan `.enc` (misal: `file.txt` menjadi `file.txt.enc`).

# 3. Proses Dekripsi File
1. Klik tombol "Choose File" dan pilih file terenkripsi (berekstensi `.enc`).
2. Masukkan kunci yang sama persis dengan yang digunakan saat enkripsi.
3. Klik tombol "Decrypt" pada aplikasi web.
4. Sistem akan membangkitkan kunci AES dan IV yang sama dari kunci yang  dimasukkan.
5. File akan didekripsi menggunakan algoritma AES mode CFB.
6. File hasil dekripsi akan otomatis diunduh ke komputer. 

## Catatan Penting
- File hasil dekripsi akan memiliki format dan ekstensi yang sama seperti file aslinya.
- Pastikan untuk menggunakan kunci yang sama saat enkripsi dan dekripsi agar file dapat dikembalikan ke bentuk aslinya tanpa kerusakan.
- Sistem ini dapat mengenkripsi dan mendekripsi berbagai jenis file (teks, gambar, dokumen, dll) tanpa mengubah format file.

## Teknologi yang Digunakan
- Python 3
- Flask (Web Framework)
- PyCryptodome (untuk implementasi AES)
- HTML/CSS (antarmuka web)
