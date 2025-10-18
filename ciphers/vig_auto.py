import string

ALPHABET = string.ascii_uppercase  # Huruf A-Z
A_ORD = ord('A')


def prepare_text(text: str) -> str:
    # Hilangkan karakter non-huruf dan ubah semua ke huruf besar
    return ''.join([c.upper() for c in text if c.isalpha()])


def _char_to_num(c: str) -> int:
    return ord(c) - A_ORD


def _num_to_char(n: int) -> str:
    return chr((n % 26) + A_ORD)


def encrypt(plaintext: str, key: str) -> str:

    # Rumus: C = (P + K) mod 26
    p = prepare_text(plaintext)
    k = prepare_text(key)

    if len(k) == 0:
        raise ValueError("Key harus berisi minimal 1 huruf alfabet.")

    # Keystream = key awal + sebagian plaintext (autokey)
    keystream = (k + p)[:len(p)]

    ciphertext = []
    for pc, kc in zip(p, keystream):
        c_num = (_char_to_num(pc) + _char_to_num(kc)) % 26
        ciphertext.append(_num_to_char(c_num))

    return ''.join(ciphertext)


def decrypt(ciphertext: str, key: str) -> str:

    # Rumus: P = (C - K) mod 26
    c = prepare_text(ciphertext)
    k = prepare_text(key)

    if len(k) == 0:
        raise ValueError("Key harus berisi minimal 1 huruf alfabet.")

    plaintext = []
    keystream = list(k)

    for i, cc in enumerate(c):
        kc = keystream[i]  # ambil huruf kunci ke-i
        p_num = (_char_to_num(cc) - _char_to_num(kc)) % 26
        p_char = _num_to_char(p_num)
        plaintext.append(p_char)
        keystream.append(p_char) 

    return ''.join(plaintext)