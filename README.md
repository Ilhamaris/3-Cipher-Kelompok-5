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

# 2. Proses Enkripsi
1. User mengunggah file yang ingin dienkripsi
2. User memasukkan kunci untuk enkripsi
3. Sistem membangkitkan kunci AES dan IV dari kunci user
4. File dienkripsi menggunakan AES mode CFB
5. Hasil enkripsi disimpan dalam format hexadecimal
6. File terenkripsi (.enc) secara otomatis diunduh

# 3. Proses Dekripsi
1. User mengunggah file terenkripsi (.enc)
2. User memasukkan kunci yang sama dengan enkripsi
3. Sistem membangkitkan kunci AES dan IV yang sama
4. File didekripsi menggunakan AES mode CFB
5. Hasil dekripsi secara otomatis diunduh

## Teknologi yang Digunakan
- Python 3
- Flask (Web Framework)
- PyCryptodome (untuk implementasi AES)
- HTML/CSS (antarmuka web)
