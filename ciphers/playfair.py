import string


def _prepare_text(text: str) -> str: # menyiapkan teks untuk dibuat sesuai dengan matriksnya., menerima inputan teks dalam bentuk sttring dan mengembalikannya stirng
    text = ''.join([c for c in text.upper() if c.isalpha()]) # text.upper/lower digunakan untuk mengubah menjadi huruf kapital
    text = text.replace('J', 'I') # c.isaalpha digunakan untuk mengapus spasi dan simbol"
    return text #text = text.replace('J', 'I') digunakan untuk mengalihkan dari J menjadi I

def _create_square(key: str) -> list: # digunakan untuk membuat matris 5x5 berdasarkan keynya.
    key = _prepare_text(key)
    seen = set()  # digunakan untuk menyimpan huruf unik sesuai dengan urutan kemunculan keynya
    square = []
    for ch in key:
        if ch not in seen:
            seen.add(ch)
            square.append(ch)
    for ch in string.ascii_uppercase: #melewati hujuf J atau menghilangkan huruf J
        if ch == 'J':
            continue
        if ch not in seen:
            seen.add(ch)
            square.append(ch)
    # 5x5
    return [square[i * 5:(i + 1) * 5] for i in range(5)]


def _find_pos(square, ch): # digunakn untuk mencari posisi baris dan kolom
    for r in range(5):
        for c in range(5):
            if square[r][c] == ch:
                return r, c
    return None


def _pairs(text: str): # digunakan untuk mencari pasangan huruf
    res = []
    i = 0
    while i < len(text):
        a = text[i]
        b = ''
        if i + 1 < len(text):
            b = text[i + 1]
        if not b:
            res.append((a, 'X'))
            i += 1
        elif a == b:
            res.append((a, 'X'))
            i += 1
        else:
            res.append((a, b))
            i += 2
    return res


def encrypt(plaintext: str, key: str) -> str: #proses enkripsi
    text = _prepare_text(plaintext) #memanggil palinteks yang telah dibersihkan
    square = _create_square(key) #memanggil key dengan matriks 5x5
    pairs = _pairs(text) # memanggil pasangan teksnya
    out = []
    for a, b in pairs:
        ra, ca = _find_pos(square, a)
        rb, cb = _find_pos(square, b)
        if ra == rb: # kedua huruf berada di baris yang sama
            out.append(square[ra][(ca + 1) % 5]) #geser masing-masing huruf ke kanan satu kolom
            out.append(square[rb][(cb + 1) % 5])
        elif ca == cb: #kedua huruf berada di kolom yang sama
            out.append(square[(ra + 1) % 5][ca]) #geser masing-masing huruf ke bawah satu baris
            out.append(square[(rb + 1) % 5][cb])
        else: #huruf di baris & kolom berbeda
            out.append(square[ra][cb]) #tiap huruf digantikan huruf yang ada pada baris yang sama tetapi kolom pasangannya (tukar kolom). Secara visual, ambil sudut rectangle yang lain.
            out.append(square[rb][ca])
    return ''.join(out)


def decrypt(ciphertext: str, key: str) -> str:
    text = _prepare_text(ciphertext) #memanggil palinteks yang telah dibersihkan
    square = _create_square(key) #memanggil key dengan matriks 5x5
    pairs = _pairs(text)# memanggil pasangan teksnya
    out = []
    for a, b in pairs:
        ra, ca = _find_pos(square, a)
        rb, cb = _find_pos(square, b)
        if ra == rb:  # kedua huruf berada di baris yang sama
            out.append(square[ra][(ca - 1) % 5]) # geser masing-masing huruf ke kiri satu kolom
            out.append(square[rb][(cb - 1) % 5])
        elif ca == cb: #kedua huruf berada di kolom yang sama
            out.append(square[(ra - 1) % 5][ca]) ##geser masing-masing huruf ke atas satu baris
            out.append(square[(rb - 1) % 5][cb])
        else: #huruf di baris & kolom berbeda
            out.append(square[ra][cb]) ##tiap huruf digantikan huruf yang ada pada baris yang sama tetapi kolom pasangannya (tukar kolom). Secara visual, ambil sudut rectangle yang lain.
            out.append(square[rb][ca])
    return ''.join(out) # hasil deskripsinya masih ada X apabila terdapat huruf ganjil atau tidak dibersihkan
 