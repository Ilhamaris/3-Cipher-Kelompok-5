# 🔐 AES Pipeline: Playfair → Vigenere (Autokey) → AES-128-CFB

<p align="justify">
Proyek ini mendemonstrasikan pipeline dari tiga algoritma sandi, menggabungkan dua cipher klasik dengan satu cipher modern. Tujuannya adalah menunjukkan bagaimana kombinasi metode enkripsi klasik dan modern dapat memperkuat keamanan data.
</p>

---

## 🧩 Cipher Pipeline

- **Playfair Cipher** (klasik)
- **Vigenere Autokey Cipher** (klasik)
- **AES-128 in CFB Mode** (modern)

---

## 🔁 Alur Enkripsi

<p align="justify">
Sebagai contoh, misalkan plaintext: <b>"AKU SUKA MAKAN NASI GORENG"</b>
</p>

1. 🔸 Plaintext dienkripsi menggunakan **Playfair Cipher** (dengan kunci dari pengguna).
2. 🔸 Ciphertext hasil Playfair digunakan sebagai input plaintext untuk **Vigenere Autokey Cipher** (menggunakan kunci yang sama).
3. 🔸 Byte hasil ciphertext Playfair digunakan untuk membentuk **kunci AES 128-bit** (diambil 16 byte pertama, dengan padding atau pemotongan jika perlu).
4. 🔸 Byte hasil ciphertext Vigenere Autokey digunakan untuk membentuk **IV AES 128-bit** (diambil 16 byte pertama, dengan padding atau pemotongan jika perlu).
5. 🔸 **AES-128-CFB** mengenkripsi plaintext asli menggunakan _key_ dan _IV_ yang diturunkan tersebut.

---

## 🧠 Catatan dan Asumsi

<p align="justify">
Beberapa hal penting dalam implementasi:
</p>

- Playfair Cipher mengubah teks menjadi huruf besar, menghapus karakter non-huruf, mengganti huruf **J → I**, serta menambahkan huruf pengisi **X** pada pasangan huruf ganda.
- Vigenere Autokey Cipher menggunakan kunci awal dari pengguna dan secara otomatis memperpanjang kunci tersebut menggunakan plaintext untuk membentuk _keystream_ selama proses enkripsi.
- Proses derivasi AES:
  - **Key:** diambil dari byte ciphertext Playfair (maks. 16 byte, pad/truncate).
  - **IV:** diambil dari byte ciphertext Vigenere Autokey (maks. 16 byte, pad/truncate).
- Hasil dekripsi Playfair dan Vigenere tidak akan sepenuhnya mengembalikan spasi/punktuasi asli, karena output berupa huruf besar terformat.

---

## ⚙️ Cara Menjalankan (Windows CMD)

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
cd "D:\Kripto\FolderAnda\3-Cipher-Kelompok-5"
python app_aes_pipeline.py
```
