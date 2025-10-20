from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from ciphers import playfair, vig_auto, aes_cfb


import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Folder upload dan output
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ENCRYPTED_FOLDER'] = 'encrypted'
app.config['DECRYPTED_FOLDER'] = 'decrypted'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['ENCRYPTED_FOLDER'], exist_ok=True)
os.makedirs(app.config['DECRYPTED_FOLDER'], exist_ok=True)


def derive_aes_key_iv(user_key):
    """Gunakan input user sebagai KEY untuk Playfair & Vigg, sedangkan plaintext tetap."""
    plaintext_pf = "KRIPTOGRAFI PLAYFAIR"
    plaintext_vig = "KRIPTOGRAFI VIGENERE"

    # Key dari input user
    pf_ct = playfair.encrypt(plaintext_pf, user_key)
    vig_ct = vig_auto.encrypt(plaintext_vig, user_key)

    # Ambil hasil cipher sebagai kunci AES
    aes_key = pf_ct.encode()[:16].ljust(16, b'0')
    iv = vig_ct.encode()[:16].ljust(16, b'0')

    return aes_key, iv


@app.route('/')
def index():
    return render_template('pipeline.html')


@app.route('/encrypt', methods=['POST'])
def encrypt_file():
    # Enkripsi file menggunakan AES-CFB dengan key hasil kombinasi Playfair + Vigenere.
    file = request.files.get('file')
    key = request.form.get('key')

    if not file or not key:
        flash("Harap masukkan file dan key untuk enkripsi!", "error")
        return redirect(url_for('index'))

    filename = secure_filename(file.filename)
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(upload_path)

    with open(upload_path, 'rb') as f:
        data = f.read()

    # Hasilkan AES key dan IV dari input key
    aes_key, iv = derive_aes_key_iv(key)
    encrypted_hex = aes_cfb.encrypt_bytes(data, aes_key, iv)

    # Simpan hasil enkripsi sebagai file .enc
    output_filename = filename + ".enc"
    output_path = os.path.join(app.config['ENCRYPTED_FOLDER'], output_filename)
    with open(output_path, 'w') as f:
        f.write(encrypted_hex)

    return send_file(output_path, as_attachment=True)


@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    file = request.files.get('file')
    key = request.form.get('key')

    if not file or not key:
        flash("Harap masukkan file terenkripsi (.enc) dan key yang sama untuk dekripsi!", "error")
        return redirect(url_for('index'))

    filename = secure_filename(file.filename)
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(upload_path)

    with open(upload_path, 'r') as f:
        hex_data = f.read()

    # Hasilkan AES key & IV dari key yang sama
    aes_key, iv = derive_aes_key_iv(key)
    decrypted_data = aes_cfb.decrypt_bytes(hex_data, aes_key, iv)

    # Hapus ekstensi .enc
    if filename.endswith(".enc"):
        filename = filename[:-4]

    output_path = os.path.join(app.config['DECRYPTED_FOLDER'], filename)
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)