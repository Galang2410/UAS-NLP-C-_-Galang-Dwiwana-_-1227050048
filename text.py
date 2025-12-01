import pdfplumber

# Ganti nama file sesuai PDF kamu
pdf_files = [
    "1.pdf",
    "2.pdf",
    "3.pdf",
    "4.pdf",
    "5.pdf"
]

all_text = ""

for pdf_file in pdf_files:
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                all_text += extracted + "\n\n"

# simpan ke satu file dataset
with open("dataset_ai_full.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("DONE! Dataset tersimpan sebagai dataset_ai_full.txt")
