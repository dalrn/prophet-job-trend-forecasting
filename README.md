# 📈 Job Trend Forecasting Model API

A REST API for forecasting job category trends using the [Prophet](https://facebook.github.io/prophet/) model. The API accepts user input in the form of a list of dates and job category names, and returns predicted trends of job posting counts on [Jobstreet Indonesia](https://id.jobstreet.com) (`yhat`) for the specified dates.

---

## 📁 Folder Structure

```
job_trend_forecasting_model/
|
├── example_data/                      # Example input data containing dates
│   └── sample_input.csv               # Contains only a 'ds' column in datetime format
|
├── models/                            # Prophet models per job category (JSON format)
│   ├── prophet_model_Administrasi_Umum.json
│   ├── prophet_model_Akuntansi_Umum.json
│   └── ... (etc., one model file per category)
|
├── forecast_api.py                    # FastAPI endpoint for serving forecasts
├── predict_all.py                     # Script to generate forecasts for all categories using 'sample_input.csv' as input
│                                     
├── README.md                          # Project documentation
└── requirements.txt                   # Project dependencies (prophet, fastapi, pandas, etc.)
```

---

## ⚙️ How the API Works

### Input

The API accepts a `POST` request to the `/predict` endpoint with the following JSON format:

```json
{
  "category": "Digital_Marketing",
  "dates": ["2025-05-01", "2025-06-01", "2025-07-01"]
}
```

- `category` : Name of the job category (20 available categories; must match the corresponding model name).
- `dates` : List of dates (strings in YYYY-MM-DD format) for which predictions are requested.

### Output

The API returns trend forecasts (`yhat`) for each requested date:

```json
{
  "predictions": [
    {"ds": "2025-05-01", "yhat": 234.52},
    {"ds": "2025-06-11", "yhat": 339.83},
    {"ds": "2025-07-31", "yhat": 442.91}
  ]
}
```

- `ds` : Date of the prediction
- `yhat` : Predicted trend value of job postings for the specified category
---

## 🚀 How to run the API

### 1. Install Dependencies


```bash
pip install -r requirements.txt
```

### 2. Run the API

```bash
uvicorn forecast_api:app --reload
```

API will be available on `http://127.0.0.1:8000`.

---

## 💡 Usage Example

### A. Using `curl`

```bash
curl -X POST http://127.0.0.1:8000/predict \
-H "Content-Type: application/json" \
-d '{"category": "Manufaktur", "dates": ["2025-05-01", "2025-06-01"]}'
```

### B. Using Python Script

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

## 📂 About `example_data/` Folder

`sample_input.csv` contains sample dates (kolom `ds`) that can be used as an input for the API. Format:

```csv
ds
2025-05-01
2025-06-01
2025-07-01
```

The Python script can read this file and use it to send requests to the API.

---

## 📄 About `predict_all.py`

Optional script to:

- Read `sample_input.csv`
- Generate predictions for **all available models** in the `models/` folder
- Save or display the prediction results for each job category

---
