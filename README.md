# 📈 Job Trend Forecasting Model API

REST API untuk melakukan *forecasting tren kategori pekerjaan* menggunakan model [Prophet](https://facebook.github.io/prophet/). API ini menerima input berupa daftar tanggal dan nama kategori pekerjaan dari pengguna, lalu memberikan prediksi tren jumlah postingan kerja pada situs [Jobstreet Indonesia](https://id.jobstreet.com) (`yhat`) untuk tanggal-tanggal tersebut.

---

## 📁 Struktur Folder

```
job_trend_forecasting_model/
|
├── example_data/                      # Contoh input data berupa tanggal
│   └── sample_input.csv               # Hanya berisi kolom 'ds' berformat datetime
|
├── models/                            # Berisi model Prophet per kategori (format JSON)
│   ├── prophet_model_Administrasi_Umum.json
│   ├── prophet_model_Akuntansi_Umum.json
│   └── ... (dll., satu file per kategori)
|
├── forecast_api.py                    # Endpoint FastAPI untuk model
├── predict_all.py                     # Jalankan prediksi untuk semua kategori dengan input 'sample_input.csv'
├── README.md                          # Dokumentasi proyek
└── requirements.txt                   # Dependencies: prophet, fastapi, pandas, dll.

```

---

## ⚙️ Cara Kerja API

### Input

API menerima request `POST` ke endpoint `/predict` dengan format JSON berikut:

```json
{
  "category": "Digital_Marketing",
  "dates": ["2025-05-01", "2025-06-01", "2025-07-01"]
}
```

- `category` : Nama kategori pekerjaan (20 kategori, sesuaikan dengan nama masing-masing model).
- `dates` : Daftar tanggal (string dalam format YYYY-MM-DD) yang ingin diprediksi.

### Output

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
-d '{"category": "Manufaktur", "dates": ["2025-05-01", "2025-06-01"]}'
```

### B. Menggunakan Python Script

```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/predict",
    json={
        "category": "Manufaktur",
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

## 📄 Tentang `predict_all.py`

Script opsional untuk:

- Membaca `sample_input.csv`
- Melakukan prediksi untuk **semua model** dalam folder `models/`
- Menyimpan atau menampilkan hasilnya per kategori

---
