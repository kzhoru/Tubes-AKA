import time
import matplotlib.pyplot as plt

# Fungsi Iteratif
def text_to_ascii_iterative(text):
    ascii_codes = []
    for char in text:  # Iterasi melalui setiap karakter dalam teks
        ascii_codes.append(ord(char))
    return ascii_codes

# Fungsi Rekursif
def text_to_ascii_recursive(text):
    # Basis: jika teks kosong, kembalikan daftar kosong
    if not text:
        return []
    # Rekursi: ambil kode ASCII karakter pertama, lalu proses sisanya
    return [ord(text[0])] + text_to_ascii_recursive(text[1:])

# Mengukur waktu eksekusi untuk fungsi rekursif
def measure_execution_time_recursive(text):
    start_time = time.time()
    text_to_ascii_recursive(text)
    end_time = time.time()
    return (end_time - start_time) * 1e6  # Waktu dalam mikrodetik

# Pengujian kompleksitas waktu untuk rekursif
test_sizes = range(1, 1001, 50)  # Ukuran masukan dari 1 hingga 1000 dengan langkah 50
recursive_times = []

for size in test_sizes:
    test_text = "a" * size  # Membuat teks dengan panjang tertentu
    recursive_times.append(measure_execution_time_recursive(test_text))

# Visualisasi hasil
plt.figure(figsize=(10, 6))
plt.plot(test_sizes, recursive_times, label="Recursive", marker="x")
plt.title("Time Complexity: Recursive Running Time")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (microseconds)")
plt.legend()
plt.grid()
plt.show()