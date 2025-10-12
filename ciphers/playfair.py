import string


def _prepare_text(text: str) -> str:
    # Uppercase, remove non-letters, replace J with I
    text = ''.join([c for c in text.upper() if c.isalpha()])
    text = text.replace('J', 'I')
    return text


def _create_square(key: str) -> list:
    key = _prepare_text(key)
    seen = set()
    square = []
    for ch in key:
        if ch not in seen:
            seen.add(ch)
            square.append(ch)
    for ch in string.ascii_uppercase:
        if ch == 'J':
            continue
        if ch not in seen:
            seen.add(ch)
            square.append(ch)
    # 5x5
    return [square[i * 5:(i + 1) * 5] for i in range(5)]


def _find_pos(square, ch):
    for r in range(5):
        for c in range(5):
            if square[r][c] == ch:
                return r, c
    return None


def _pairs(text: str):
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


def encrypt(plaintext: str, key: str) -> str:
    text = _prepare_text(plaintext)
    square = _create_square(key)
    pairs = _pairs(text)
    out = []
    for a, b in pairs:
        ra, ca = _find_pos(square, a)
        rb, cb = _find_pos(square, b)
        if ra == rb:
            out.append(square[ra][(ca + 1) % 5])
            out.append(square[rb][(cb + 1) % 5])
        elif ca == cb:
            out.append(square[(ra + 1) % 5][ca])
            out.append(square[(rb + 1) % 5][cb])
        else:
            out.append(square[ra][cb])
            out.append(square[rb][ca])
    return ''.join(out)


def decrypt(ciphertext: str, key: str) -> str:
    text = _prepare_text(ciphertext)
    square = _create_square(key)
    pairs = _pairs(text)
    out = []
    for a, b in pairs:
        ra, ca = _find_pos(square, a)
        rb, cb = _find_pos(square, b)
        if ra == rb:
            out.append(square[ra][(ca - 1) % 5])
            out.append(square[rb][(cb - 1) % 5])
        elif ca == cb:
            out.append(square[(ra - 1) % 5][ca])
            out.append(square[(rb - 1) % 5][cb])
        else:
            out.append(square[ra][cb])
            out.append(square[rb][ca])
    return ''.join(out)
