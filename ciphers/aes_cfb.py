from Crypto.Cipher import AES
import base64

# ==== Untuk TEKS (pakai Base64 biar bisa disimpan sebagai string) ====
def encrypt(text, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    ct_bytes = cipher.encrypt(text.encode('utf-8'))
    return base64.b64encode(ct_bytes).decode('utf-8')

def decrypt(b64_ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    ct = base64.b64decode(b64_ciphertext)
    pt_bytes = cipher.decrypt(ct)
    return pt_bytes.decode('utf-8', errors='ignore')

# ==== Untuk FILE (biner, TANPA base64) ====
def encrypt_bytes(data_bytes, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    return cipher.encrypt(data_bytes)

def decrypt_bytes(enc_bytes, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    return cipher.decrypt(enc_bytes)