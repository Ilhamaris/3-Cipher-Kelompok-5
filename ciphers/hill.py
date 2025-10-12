import string
from typing import List


def _prepare_text(text: str) -> str:
    return ''.join([c for c in text.upper() if c.isalpha()])


def _key_to_matrix(key: str) -> List[List[int]]:
    # derive 2x2 matrix from key text by taking letter ordinals mod 26
    s = _prepare_text(key)
    if len(s) < 4:
        s = (s * 4)[:4]
    vals = [ord(c) - ord('A') for c in s[:4]]
    mat = [[vals[0], vals[1]], [vals[2], vals[3]]]
    # ensure invertible mod 26 by tweaking elements if needed
    if _mod_inv(_det(mat) % 26, 26) is None:
        found = False
        for pos in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            r, c = pos
            base = mat[r][c]
            for delta in range(1, 26):
                mat[r][c] = (base + delta) % 26
                if _mod_inv(_det(mat) % 26, 26) is not None:
                    found = True
                    break
            if found:
                break
        if not found:
            # as a last resort, force a known invertible matrix
            mat = [[1, 0], [0, 1]]
    return mat


def _mod_inv(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def _det(matrix):
    return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])


def _inv_matrix(matrix):
    det = _det(matrix) % 26
    inv_det = _mod_inv(det, 26)
    if inv_det is None:
        raise ValueError('Key matrix not invertible mod 26')
    a, b = matrix[0]
    c, d = matrix[1]
    inv = [[d * inv_det % 26, (-b) * inv_det % 26], [(-c) * inv_det % 26, a * inv_det % 26]]
    return inv


def _mat_mult(mat, vec):
    return [(mat[0][0] * vec[0] + mat[0][1] * vec[1]) % 26, (mat[1][0] * vec[0] + mat[1][1] * vec[1]) % 26]


def encrypt(plaintext: str, key: str) -> str:
    text = _prepare_text(plaintext)
    matrix = _key_to_matrix(key)
    out = []
    i = 0
    while i < len(text):
        a = ord(text[i]) - ord('A')
        b = ord(text[i + 1]) - ord('A') if i + 1 < len(text) else 23  # 'X' pad
        res = _mat_mult(matrix, [a, b])
        out.append(chr(res[0] + ord('A')))
        out.append(chr(res[1] + ord('A')))
        i += 2
    return ''.join(out)


def decrypt(ciphertext: str, key: str) -> str:
    text = _prepare_text(ciphertext)
    matrix = _key_to_matrix(key)
    inv = _inv_matrix(matrix)
    out = []
    i = 0
    while i < len(text):
        a = ord(text[i]) - ord('A')
        b = ord(text[i + 1]) - ord('A') if i + 1 < len(text) else 23
        res = _mat_mult(inv, [a, b])
        out.append(chr(res[0] + ord('A')))
        out.append(chr(res[1] + ord('A')))
        i += 2
    return ''.join(out)
