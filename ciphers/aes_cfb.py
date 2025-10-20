from Crypto.Cipher import AES

def encrypt(text, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    ct_bytes = cipher.encrypt(text.encode('utf-8'))
    return ct_bytes.hex()

def decrypt(hex_ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    ct = bytes.fromhex(hex_ciphertext)
    pt_bytes = cipher.decrypt(ct)
    return pt_bytes.decode('utf-8', errors='ignore')

def encrypt_bytes(data_bytes, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    encrypted = cipher.encrypt(data_bytes)
    return encrypted.hex()

def decrypt_bytes(hex_encrypted, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    encrypted_bytes = bytes.fromhex(hex_encrypted)
    return cipher.decrypt(encrypted_bytes)