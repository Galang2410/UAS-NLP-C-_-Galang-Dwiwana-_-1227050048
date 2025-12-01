UAS _ Galang Dwiwana Thabrani _ 1227050048 _ NLP C

1. Identifikasi Tujuan / Goals Task NLP
Pada tugas ini, saya memilih tema “Etika Penggunaan Kecerdasan Buatan (AI) dalam Pendidikan”, karena topik tersebut sedang berkembang pesat dan memiliki implikasi besar terhadap dunia akademik serta proses pembelajaran modern. Untuk mengolah materi kajian yang cukup kompleks dan panjang, saya menggunakan teknik text summarization sebagai task utama dalam Natural Language Processing (NLP).
Tujuan dari task ini adalah menghasilkan ringkasan otomatis dari lima artikel ilmiah yang membahas etika penggunaan AI di bidang pendidikan. Melalui summarization, informasi penting dari dokumen asli dapat dipadatkan tanpa menghilangkan esensi dan makna utamanya. Teknik ini dipilih karena artikel-artikel akademik biasanya memiliki struktur naratif yang panjang, kaya data, dan penuh istilah teknis, sehingga metode otomatis lebih efisien untuk:
* mengekstraksi poin-poin inti,
* menyusun kembali informasi secara terstruktur, dan
* menyajikan pemahaman komprehensif dalam format yang lebih ringkas.
Dengan demikian, summarization menjadi solusi tepat untuk menghasilkan representasi singkat dari kumpulan dokumen ilmiah tanpa kehilangan konteks dan makna fundamentalnya.


2. Pengumpulan Dataset (Bebas Eksplorasi)
Dataset diperoleh dari lima artikel ilmiah berbahasa Indonesia yang membahas berbagai aspek etika penggunaan AI dalam pendidikan. Seluruh PDF diekstraksi menjadi teks menggunakan Python, kemudian digabungkan menjadi satu dokumen teks mentah. Sumber dataset dipilih secara eksploratif dengan fokus pada relevansi topik, kualitas akademik, serta kelengkapan pembahasan terkait risiko, manfaat, dan prinsip etika dalam pemanfaatan teknologi AI di lingkungan pendidikan.

3. Pre-processing Dataset
Beberapa tahap preprocessing dilakukan untuk memastikan teks siap diolah oleh model summarization. Tahapan tersebut mencakup:
* Ekstraksi teks dari PDF.
* Penghapusan konten yang tidak relevan seperti daftar pustaka, metadata jurnal, email penulis, nomor halaman, link DOI dan URL, serta header dan footer.
* Pembersihan format teks dengan menghilangkan baris kosong, karakter tidak penting, angka tunggal, dan spasi berlebih.
* Penyeragaman struktur paragraf.
* Pemotongan teks menjadi beberapa bagian (chunking) karena model Transformer memiliki batas kapasitas input.
Tahapan ini menghasilkan file teks bersih yang siap diproses, yaitu dataset_ai_superclean.txt.

4. Penggunaan Deep Learning / Transformers / LLM
Proses summarization dilakukan menggunakan model Transformer modern dari HuggingFace, yaitu Irvan14/t5-small-indonesian-summarization
. Model ini merupakan varian T5 yang telah dilatih khusus untuk tugas summarization dalam bahasa Indonesia. Mekanisme pengerjaan meliputi:
    1. Memuat model dan tokenizer melalui pipeline summarization.
    2. Memproses setiap chunk teks menggunakan parameter panjang ringkasan tertentu (misalnya 60–150 token).
    3. Menggabungkan seluruh ringkasan per bagian menjadi satu dokumen ringkasan lengkap (summary_output.txt).

Model Transformer dipilih karena kemampuannya dalam memahami konteks teks panjang, menjaga koherensi ringkasan, serta menghasilkan output yang padat dan informatif.

Evaluasi Kualitas Model
Model summarization yang digunakan terbukti berhasil menghasilkan ringkasan dari lima artikel ilmiah secara efektif. Hasil ringkasan menunjukkan bahwa:
* Model mampu mengambil poin-poin penting dari setiap teks akademik.
* Struktur ringkasan tetap logis, koheren, dan konsisten dengan konteks aslinya.
* Tidak ditemukan distorsi makna yang signifikan atau informasi palsu (hallucination) dalam output.
* Proses chunking teks panjang dapat diproses dengan baik walaupun dilakukan secara bertahap.
* Ringkasan akhir mencerminkan keseluruhan topik secara singkat, informatif, dan mudah dipahami.
Meskipun tidak menggunakan evaluasi kuantitatif seperti ROUGE, penilaian kualitatif menunjukkan bahwa model Transformer yang digunakan telah mampu menjalankan tugas summarization dengan baik, terutama dalam konteks teks akademik berbahasa Indonesia.


Ringkasan Workflow Secara Singkat

Kumpulkan 5 PDF

Extract PDF → text.py → dataset_ai_full.txt

Cleaning → clean_text.py → dataset_ai_superclean.txt

Load & potong teks di Jupyter Notebook

Summarization dengan model T5 Indonesia

Gabungkan dan simpan hasil ringkasan

Validasi dan analisis hasil
