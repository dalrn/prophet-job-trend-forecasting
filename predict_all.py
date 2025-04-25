import os
import pandas as pd
import requests

# === Konfigurasi ===
API_URL = "http://127.0.0.1:8000/predict"
MODELS_DIR = "models/"
INPUT_FILE = "example_data/sample_input.csv"

# bersihkan nama file menjadi nama kategori
def desanitize_filename(filename):
    name = filename.replace("prophet_model_", "").replace(".json", "")
    return name.replace("_", " ").title()

# load tanggal dari sample_input.csv
try:
    df_input = pd.read_csv(INPUT_FILE)
    if 'ds' not in df_input.columns:
        raise ValueError("File input harus memiliki kolom 'ds'")
    date_list = df_input['ds'].apply(str).tolist()
except Exception as e:
    print(f"[ERROR] Gagal membaca file input: {e}")
    exit()

# loop semua file model di folder models/
model_files = [f for f in os.listdir(MODELS_DIR) if f.endswith(".json")]

print(f"\n📤 Mengirim prediksi untuk {len(model_files)} kategori...\n")

# prediksi untuk setiap kategori
for file in model_files:
    category = desanitize_filename(file)
    print(f"🔍 Kategori: {category}")

    payload = {
        "category": category,
        "dates": date_list
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            results = response.json()['predictions']
            df_result = pd.DataFrame(results)
            print(df_result)
            print("-" * 40)
            # jika ingin menyimpan hasil prediksi ke file CSV
            # df_result.to_csv(f"output_{category.replace(' ', '_').lower()}.csv", index=False)
        else:
            print(f"[ERROR] Gagal prediksi: {response.text}")
    except Exception as e:
        print(f"[EXCEPTION] {e}")

print("\n✅ Selesai.\n")
