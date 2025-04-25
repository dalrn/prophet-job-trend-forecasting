# 📈 Job Trend Forecasting Model API

REST API untuk melakukan *forecasting tren kategori pekerjaan* menggunakan model [Prophet](https://facebook.github.io/prophet/). API ini memungkinkan pengguna mengirim daftar tanggal dan nama kategori pekerjaan, lalu mengembalikan prediksi tren jumlah postingan kerja (`yhat`) untuk tanggal-tanggal tersebut.

---

## 📁 Struktur Folder

```
job_trend_forecasting_model/
|
├── example_data/                      # Contoh input data berupa tanggal
│   └── sample_input.csv               # Hanya berisi kolom 'ds' berformat tanggal
|
├── models/                            # Berisi model Prophet per kategori (format JSON)
│   ├── prophet_model_Administrasi_Umum.json
│   ├── prophet_model_Akuntansi-Perbankan-Finansial.json
│   └── ... (dan lainnya, satu file per kategori)
|
├── forecast_api.py                    # Endpoint FastAPI untuk prediksi
├── predict_all.py                     # (Opsional) Jalankan prediksi untuk semua kategori dengan input 'sample_input.csv'
├── README.md                          # Dokumentasi proyek
└── requirements.txt                   # Dependencies: prophet, fastapi, pandas, dll

```

---

## ⚙️ Cara Kerja API

### 🔹 Mekanisme Input

API menerima request `POST` ke endpoint `/predict` dengan format JSON berikut:

```json
{
  "category": "Marketing",
  "dates": ["2025-05-01", "2025-06-01", "2025-07-01"]
}
```

- `category` : Nama kategori pekerjaan (20 kategori, sesuaikan dengan masing-masing nama model).
- `dates` : Daftar tanggal (string dalam format YYYY-MM-DD) untuk diprediksi.

### ✅ Output yang Dihasilkan

Output berupa prediksi tren (`yhat`) untuk setiap tanggal yang diminta:

```json
{
  "predictions": [
    {"ds": "2025-05-01", "yhat": 234.52},
    {"ds": "2025-06-11", "yhat": 339.83},
    {"ds": "2025-07-31", "yhat": 442.91}
  ]
}
```

---

## 🚀 Cara Menjalankan API

### 1. Install Dependencies


```bash
pip install -r requirements.txt
```

### 2. Jalankan API

```bash
uvicorn forecast_api:app --reload
```

API akan tersedia di `http://127.0.0.1:8000`.

---

## 💡 Contoh Penggunaan

### A. Menggunakan `curl`

```bash
curl -X POST http://127.0.0.1:8000/predict \
-H "Content-Type: application/json" \
-d '{"category": "Sales", "dates": ["2025-05-01", "2025-06-01"]}'
```

### B. Menggunakan Python Script

```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/predict",
    json={
        "category": "Marketing",
        "dates": ["2025-05-01", "2025-06-01"]
    }
)

print(response.json())
```

---

## 📂 Folder `example_data/`

File `sample_input.csv` berisi contoh tanggal (kolom `ds`) yang bisa digunakan sebagai input ke API. Format:

```csv
ds
2025-05-01
2025-06-01
2025-07-01
```

Script Python dapat membaca file ini dan menggunakannya untuk mengirim permintaan ke API.

---

## 📄 Tentang `predict_all.py` (Opsional)

Script opsional untuk:

- Membaca `sample_input.csv`
- Melakukan prediksi untuk **semua model** dalam folder `models/`
- Menyimpan atau menampilkan hasilnya per kategori

---

## 🧠 Catatan Teknis

- Nama file model disesuaikan dari kategori menggunakan fungsi `sanitize_filename()` agar tidak error karena spasi atau karakter khusus.
- Model disimpan dalam format JSON (`model_to_json` dan `model_from_json` dari Prophet).
- Semua input `dates` akan dikonversi menjadi format `datetime` oleh `pandas.to_datetime`.

---

## ❓ FAQ

### ❓ Apa yang terjadi jika kategori tidak ditemukan?

API akan memberikan error 500 dengan pesan bahwa file model tidak ditemukan.

---

### ❓ Apakah saya bisa menambahkan kategori baru?

Ya. Simpan model baru ke dalam folder `models/` dengan nama:

```plaintext
prophet_model_{category_name}.json
```

