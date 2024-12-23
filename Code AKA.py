def text_to_ascii_iterative(text):
    ascii_codes = []
    for char in text:  # Iterasi melalui setiap karakter dalam teks
        ascii_codes.append(ord(char))
    return ascii_codes

# Contoh penggunaan
text = "Hello"
ascii_iterative = text_to_ascii_iterative(text)
print("Iterasi:", ascii_iterative)

def text_to_ascii_recursive(text):
    # Basis: jika teks kosong, kembalikan daftar kosong
    if not text:
        return []
    # Rekursi: ambil kode ASCII karakter pertama, lalu proses sisanya
    return [ord(text[0])] + text_to_ascii_recursive(text[1:])

# Contoh penggunaan
ascii_recursive = text_to_ascii_recursive(text)
print("Rekursi:", ascii_recursive)