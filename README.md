# AES Pipeline: Playfair -> Hill -> AES-128-CFB

This project demonstrates a pipeline of three ciphers:

- Playfair (classic)
- Hill (2x2 matrix, classic)
- AES-128 in CFB mode (modern)

Flow (for plaintext example "AKU SUKA MAKAN NASI GORENG"):
1. Plaintext is encrypted using Playfair (key provided by user).
2. Playfair ciphertext is used as plaintext input to the Hill cipher (same key).
3. The Playfair ciphertext bytes are used to derive a 128-bit AES key (first 16 bytes, padded/truncated).
4. The Hill ciphertext bytes are used to derive a 128-bit IV (first 16 bytes, padded/truncated).
5. AES-128-CFB encrypts the original plaintext using the derived key and IV.

Notes and assumptions:
- Playfair implementation converts to uppercase, removes non-letters, replaces 'J' with 'I', and pads repeated letters with 'X'.
- Hill uses a 2x2 matrix derived from the first 4 letters of the key. If the matrix is not invertible modulo 26, small adjustments are attempted to make it invertible.
- AES key/IV derivation: ASCII bytes of ciphertext are used directly; if shorter than 16 bytes the bytes are right-padded with ASCII '0' (0x30), if longer they are truncated.
- Decryption of Playfair/Hill will not fully restore whitespace/punctuation; it returns normalized uppercase letters.

Run locally (Windows cmd.exe):

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
cd "D:\MATKUL\SEMESTER 5\KRIPTOGRAFI (P. IKHWAN)\3 Cipher"
python app_aes_pipeline.py
```

Open `http://127.0.0.1:5000/` and use the form to encrypt/decrypt.

Files added:
- `ciphers/playfair.py`
- `ciphers/hill.py`
- `ciphers/aes_cfb.py`
- `app_aes_pipeline.py`
- `templates/pipeline.html`

If you'd like, I can:
- Add unit tests
- Improve decryption spacing reconstruction
- Provide a downloadable package or a simple CLI wrapper
