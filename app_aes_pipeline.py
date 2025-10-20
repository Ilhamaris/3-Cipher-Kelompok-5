from flask import Flask, render_template, request, redirect, url_for, flash, send_file

from ciphers import playfair, vig_auto, aes_cfb # Import modul cipher yang telah dibuat
import os # Import os untuk operasi file dan direktori
from werkzeug.utils import secure_filename # Import secure_filename untuk membersihkan nama file dari karakter berbahaya

# Inisialisasi aplikasi Flask
app = Flask(__name__)
# Set secret key untuk keamanan session dan flash messages
app.secret_key = "supersecretkey"

# Konfigurasi folder untuk menyimpan file
app.config['UPLOAD_FOLDER'] = 'uploads'        # Folder untuk file yang diunggah
app.config['ENCRYPTED_FOLDER'] = 'encrypted'   # Folder untuk file hasil enkripsi
app.config['DECRYPTED_FOLDER'] = 'decrypted'  # Folder untuk file hasil dekripsi

# Buat direktori jika belum ada (exist_ok=True mencegah error jika folder sudah ada)
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['ENCRYPTED_FOLDER'], exist_ok=True)
os.makedirs(app.config['DECRYPTED_FOLDER'], exist_ok=True)


def derive_aes_key_iv(user_key):
    
    # Plaintext tetap yang akan dienkripsi
    plaintext_pf = "KRIPTOGRAFI PLAYFAIR"
    plaintext_vig = "KRIPTOGRAFI VIGENERE"

    # Enkripsi menggunakan kunci dari user
    pf_ct = playfair.encrypt(plaintext_pf, user_key)    # Hasil enkripsi Playfair
    vig_ct = vig_auto.encrypt(plaintext_vig, user_key)  # Hasil enkripsi Vigenere

    # Konversi hasil enkripsi menjadi kunci AES dan IV
    # [:16] mengambil 16 byte pertama, ljust(16, b'0') menambah padding '0' jika kurang dari 16 byte
    aes_key = pf_ct.encode()[:16].ljust(16, b'0')   # Kunci AES dari hasil Playfair
    iv = vig_ct.encode()[:16].ljust(16, b'0')       # IV dari hasil Vigenere

    return aes_key, iv


# Route untuk halaman utama
@app.route('/')
def index():
    # Menampilkan halaman utama aplikasi.
    return render_template('pipeline.html')


@app.route('/encrypt', methods=['POST'])
def encrypt_file():
    
    # Ambil file dan kunci dari form request
    file = request.files.get('file')
    key = request.form.get('key')

    # Validasi input
    if not file or not key:
        flash("Harap masukkan file dan key untuk enkripsi!", "error")
        return redirect(url_for('index'))

    # Amankan nama file dan simpan file yang diunggah
    filename = secure_filename(file.filename)  # Bersihkan nama file
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(upload_path)  # Simpan file ke folder upload

    # Baca konten file dalam mode biner
    with open(upload_path, 'rb') as f:
        data = f.read()

    # Generate kunci AES dan IV menggunakan kunci dari user
    aes_key, iv = derive_aes_key_iv(key)
    # Enkripsi data menggunakan AES-CFB dan konversi ke format hex
    encrypted_hex = aes_cfb.encrypt_bytes(data, aes_key, iv)

    # Simpan hasil enkripsi dengan ekstensi .enc
    output_filename = filename + ".enc"  # Tambah ekstensi .enc
    output_path = os.path.join(app.config['ENCRYPTED_FOLDER'], output_filename)
    with open(output_path, 'w') as f:
        f.write(encrypted_hex)  # Simpan hasil enkripsi dalam format hex

    # Kirim file hasil enkripsi ke user untuk diunduh
    return send_file(output_path, as_attachment=True)


@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    
    # Ambil file terenkripsi dan kunci dari form request
    file = request.files.get('file')
    key = request.form.get('key')

    # Validasi input
    if not file or not key:
        flash("Harap masukkan file terenkripsi (.enc) dan key yang sama untuk dekripsi!", "error")
        return redirect(url_for('index'))

    # Amankan nama file dan simpan file yang diunggah
    filename = secure_filename(file.filename)
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(upload_path)

    # Baca konten file hex terenkripsi
    with open(upload_path, 'r') as f:
        hex_data = f.read()

    # Generate kunci AES dan IV yang sama dengan proses enkripsi
    aes_key, iv = derive_aes_key_iv(key)
    # Dekripsi data dari format hex ke bentuk asli
    decrypted_data = aes_cfb.decrypt_bytes(hex_data, aes_key, iv)

    # Hapus ekstensi .enc untuk mendapatkan nama file asli
    if filename.endswith(".enc"):
        filename = filename[:-4]

    # Simpan hasil dekripsi dengan nama file asli
    output_path = os.path.join(app.config['DECRYPTED_FOLDER'], filename)
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)  # Simpan dalam mode biner

    # Kirim file hasil dekripsi ke user untuk diunduh
    return send_file(output_path, as_attachment=True)

# Jalankan aplikasi Flask
if __name__ == '__main__':
    app.run(debug=True)
    