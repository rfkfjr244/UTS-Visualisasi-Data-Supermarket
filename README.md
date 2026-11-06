# SUPERMARKET SALES PERFORMANCE DASHBOARD

## Identitas Mahasiswa

| Keterangan | Informasi |
|---|---|
| Nama | Rifki Fajar |
| NIM | 241051018 |
| Mata Kuliah | Visualisasi Data |
| Proyek | Ujian Tengah Semester (UTS) |

## 1. Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis data penjualan supermarket dan menyajikan hasilnya dalam bentuk visualisasi interaktif. Analisis berfokus pada tren penjualan, kategori produk, performa cabang, metode pembayaran, serta rating pelanggan.

Proyek menggunakan Python untuk pemeriksaan data, preprocessing, exploratory data analysis (EDA), dan visualisasi. Hasil analisis kemudian disajikan melalui dashboard interaktif menggunakan Streamlit dan Plotly.

## 2. Link Proyek

- **GitHub Repository:** https://github.com/rfkfjr244/UTS-Visualisasi-Data-Supermarket
- **Live Dashboard:** https://uts-visualisasi-data-supermarket-rifki-fajar.streamlit.app/

## 3. Sumber Dataset

Dataset yang digunakan adalah **Supermarket Sales Dataset** yang dibuat oleh Aung Pyae dan tersedia melalui Kaggle.

- **Sumber:** https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales
- **Jumlah data:** 1.000 baris
- **Jumlah atribut awal:** 17 kolom
- **Periode transaksi:** Januari sampai Maret 2019

Dataset mencakup informasi transaksi, cabang supermarket, kategori produk, jumlah pembelian, harga, total transaksi, metode pembayaran, dan rating pelanggan.

## 4. Latar Belakang

Data transaksi penjualan memiliki informasi yang dapat digunakan untuk memahami perilaku pembelian pelanggan dan kinerja penjualan supermarket. Namun, data mentah perlu diperiksa dan diolah sebelum menghasilkan informasi yang mudah dipahami.

Melalui proyek ini, data penjualan dianalisis untuk mengetahui kategori produk dengan penjualan tertinggi, cabang dengan kontribusi penjualan terbesar, distribusi metode pembayaran, dan perubahan penjualan berdasarkan waktu.

Hasil analisis disajikan melalui dashboard agar pengguna dapat mengeksplorasi informasi berdasarkan filter yang tersedia.

## 5. Tahapan Pengolahan Data

Proses pengerjaan proyek terdiri dari beberapa tahapan:

1. **Pemeriksaan Data:** Memeriksa struktur dataset, tipe data, nilai kosong, dan duplikasi.
2. **Data Preprocessing:** Menghapus kolom kosong, mengubah format tanggal dan waktu, serta membuat atribut tambahan.
3. **Exploratory Data Analysis (EDA):** Menghitung ringkasan statistik dan menganalisis karakteristik penjualan.
4. **Visualisasi Data:** Membuat grafik tren penjualan, kategori produk, cabang, metode pembayaran, dan rating.
5. **Dashboard Interaktif:** Mengintegrasikan hasil analisis ke dalam aplikasi Streamlit.

## 6. Key Insights (Temuan Utama)

Berdasarkan hasil analisis terhadap dataset, diperoleh beberapa temuan berikut.

### 1. Total Penjualan

Total nilai transaksi mencapai **322.966,75** dari 1.000 transaksi. Rata-rata nilai transaksi sebesar **322,97**.

### 2. Kategori Produk

Kategori **Food and Beverages** memiliki nilai penjualan tertinggi sebesar **56.144,84**. Sementara itu, kategori **Health and Beauty** memiliki nilai penjualan terendah sebesar **49.193,74**.

### 3. Performa Cabang

Cabang C yang berlokasi di Naypyitaw mencatat nilai penjualan tertinggi sebesar **110.568,71**. Cabang A dan B memiliki nilai penjualan yang relatif berdekatan.

### 4. Metode Pembayaran

Ewallet menjadi metode pembayaran dengan jumlah transaksi terbanyak, yaitu **345 transaksi**, diikuti Cash sebanyak 344 transaksi dan Credit Card sebanyak 311 transaksi.

### 5. Tren Penjualan Bulanan

Januari mencatat nilai penjualan tertinggi sebesar **116.291,87**. Penjualan mengalami penurunan pada Februari menjadi **97.219,37**, kemudian meningkat pada Maret menjadi **109.455,51**.

## 7. Fitur Dashboard

Dashboard menyediakan beberapa fitur utama:

- **KPI Cards:** Total Revenue, Total Transactions, Units Sold, dan Average Rating.
- **Daily Sales Trend:** Grafik tren penjualan berdasarkan tanggal.
- **Sales by Product Category:** Perbandingan penjualan antar kategori produk.
- **Sales by City:** Perbandingan performa penjualan setiap kota.
- **Payment Method Distribution:** Distribusi metode pembayaran.
- **Rating vs Transaction:** Hubungan antara rating dan nilai transaksi.
- **Interactive Filters:** Filter tanggal, kota, kategori produk, dan metode pembayaran.
- **Sales Insights:** Ringkasan temuan berdasarkan data yang ditampilkan.

## 8. Struktur Folder Proyek

```text
UTS-Visualisasi-Data-Supermarket/
│
├── data/
│   ├── raw/
│   │   └── supermarket_sales.csv
│   │
│   └── processed/
│       └── supermarket_sales_clean.csv
│
├── outputs/
│   ├── 01_tren_penjualan_harian.png
│   ├── 02_penjualan_kategori.png
│   ├── 03_penjualan_cabang.png
│   ├── 04_metode_pembayaran.png
│   ├── 05_rating_vs_transaksi.png
│   ├── ringkasan_produk.csv
│   ├── ringkasan_cabang.csv
│   ├── ringkasan_pembayaran.csv
│   └── ringkasan_bulanan.csv
│
├── 01_Pemeriksaan_Data.ipynb
├── 02_Data_Preprocessing.ipynb
├── 03_EDA.ipynb
├── 04_Visualisasi_Data.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 9. Teknologi yang Digunakan

| Teknologi | Kegunaan |
|---|---|
| Python | Bahasa pemrograman |
| JupyterLab | Lingkungan pengolahan dan analisis data |
| Pandas | Manipulasi dan pengolahan data |
| NumPy | Operasi numerik |
| Matplotlib | Visualisasi data |
| Seaborn | Visualisasi statistik |
| Plotly | Grafik interaktif |
| Streamlit | Pengembangan dashboard |

## 10. Cara Menjalankan Proyek Secara Lokal

### Persyaratan

Pastikan Python sudah terinstal pada komputer.

### Langkah 1. Clone Repository

```bash
git clone https://github.com/rfkfjr244/UTS-Visualisasi-Data-Supermarket.git
```

### Langkah 2. Masuk ke Folder Proyek

```bash
cd UTS-Visualisasi-Data-Supermarket
```

### Langkah 3. Instal Dependencies

```bash
pip install -r requirements.txt
```

### Langkah 4. Jalankan Dashboard

```bash
streamlit run app.py
```

Dashboard akan terbuka melalui browser pada alamat lokal yang diberikan Streamlit.

## 11. Catatan dan Batasan Analisis

Dataset hanya mencakup periode Januari sampai Maret 2019. Oleh karena itu, hasil analisis tidak dapat digunakan untuk menyimpulkan tren penjualan sepanjang tahun atau kondisi penjualan supermarket pada periode saat ini.

Selain itu, atribut `gross income` pada dataset memiliki nilai yang sama dengan `Tax 5%`. Oleh karena itu, atribut tersebut tidak ditafsirkan sebagai keuntungan bersih perusahaan. Atribut `gross margin percentage` juga memiliki nilai konstan sehingga tidak digunakan untuk membandingkan kinerja transaksi.

## 12. Kesimpulan

Proyek ini menunjukkan proses pengolahan data penjualan supermarket mulai dari pemeriksaan data mentah, preprocessing, analisis eksploratif, hingga penyajian visualisasi interaktif.

Dashboard membantu pengguna memahami karakteristik penjualan berdasarkan waktu, kategori produk, lokasi cabang, metode pembayaran, dan rating pelanggan. Penggunaan filter interaktif juga memudahkan pengguna dalam mengeksplorasi data berdasarkan kriteria tertentu.

---

**Dibuat oleh: Rifki Fajar**  
**NIM: 241051018**  
**Proyek UTS Visualisasi Data**
