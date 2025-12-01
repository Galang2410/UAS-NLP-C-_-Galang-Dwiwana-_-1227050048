import re

# Baca file hasil clean sebelumnya
with open("dataset_ai_clean.txt", "r", encoding="utf-8") as f:
    text = f.read()

# ============================
# 1. Hilangkan bagian REFERENSI / DAFTAR PUSTAKA secara otomatis
# ============================

# Hapus semua teks setelah kata berikut:
patterns_refs = [
    r"DAFTAR PUSTAKA.*",
    r"Daftar Pustaka.*",
    r"REFERENSI.*",
    r"References.*",
    r"REFERENCES.*"
]

for p in patterns_refs:
    text = re.sub(p, "", text, flags=re.IGNORECASE | re.DOTALL)

# ============================
# 2. Hapus DOI, URL, ISSN, P-ISSN, E-ISSN
# ============================

text = re.sub(r"http\S+", "", text)
text = re.sub(r"doi:\S+", "", text, flags=re.IGNORECASE)
text = re.sub(r"DOI\S+", "", text, flags=re.IGNORECASE)
text = re.sub(r"E-ISSN.*", "", text)
text = re.sub(r"P-ISSN.*", "", text)

# ============================
# 3. Hapus email penulis & afiliasi
# ============================

text = re.sub(r"\S+@\S+", "", text)            # hapus email
text = re.sub(r"(Universitas|Program Studi|Fakultas|Magister|Sekolah Tinggi).*", "", text)

# ============================
# 4. Hapus baris penulis/metadata jurnal (nama doang)
# ============================

text = re.sub(r"^[A-Z][a-z]+\s[A-Z][a-z]+.*$", "", text, flags=re.MULTILINE)

# ============================
# 5. Hapus baris yang hanya angka atau sangat pendek
# ============================

text = re.sub(r"^\s*\d{1,4}\s*$", "", text, flags=re.MULTILINE)   # angka berdiri
text = re.sub(r"^\s*[IVXLC]+\s*$", "", text, flags=re.MULTILINE)   # angka romawi
text = re.sub(r"^\s*[A-Za-z]\s*$", "", text, flags=re.MULTILINE)   # huruf satuan

# ============================
# 6. Hilangkan spasi kosong berlebihan
# ============================

text = re.sub(r"\n\s*\n", "\n", text)   # hapus blank lines
text = text.strip()

# ============================
# 7. Simpan output final
# ============================

with open("dataset_ai_superclean.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("DONE! Dataset super clean tersimpan sebagai dataset_ai_superclean.txt")
