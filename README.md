# 📷 Raspberry Pi Object Counting API

A backend service built using **FastAPI** that receives, stores, and serves object count logs from Raspberry Pi cameras. This project supports real-time data upload and retrieval of aggregated statistics, such as **latest counts**, **hourly trends**, and **daily totals**.

---

## 🚀 Features

- ✅ Upload log entries from Raspberry Pi devices
- 📊 Get latest object count per Pi device
- ⏰ Fetch hourly aggregated data for the current day
- 📅 Retrieve daily aggregated data for a specific date
- 🧾 Built-in Swagger UI and ReDoc for interactive API testing

---

## 🛠️ Tech Stack

- **FastAPI** – Modern, fast web framework for building APIs
- **Pydantic** – Data validation and parsing using Python type hints
- **Python 3.11+**
- In-memory storage (`data_store`) for logs (for demo purposes)

---

## 📁 Project Structure

```bash

├── app/
│ ├── main.py                   # API routes and logic
│ ├── models.py                 # Pydantic request models
│ ├── schemas.py                # Pydantic response schemas
│ ├── services.py               # Business logic (aggregations, filters)
│ ├── database.py               # In-memory data store
│ └── init.py                   # App initialization
|
├── README.md                   # Project documentation
├── requirements.txt            # Project dependencies
└── .gitignore

```

## 📌 API Endpoints
```bash
GET  -   /api/count/latest?pi_id=cam-777                      # Get Latest Count
GET  -   /api/count/hourly?pi_id=cam-777                      # Get Hourly Counts
GET  -   /api/count/daily?pi_id=cam-777&date=2025-06-24       # Get Daily Counts
POST -  /api/count/upload                                     # upload log to Python-Backend from Raspberry PI

```

## 🧪 Sample Test Case: Upload
``` bash
{
  "pi_id": "cam-777",
  "logs": [
    {
      "timestamp": "2025-06-24T14:00:00",
      "counts": [
        {"object_type": "person", "count": 5},
        {"object_type": "car", "count": 3}
      ]
    }
  ]
}
```
## 📦 Setup & Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/saadkhan710/Pi-camera-counter.git
cd Pi-camera-counter

# 2. Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate               # on Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the FastAPI server
uvicorn app.main:app --reload

```

## 👨‍💻 Author
```bash
Saad Khan
MSc Information Systems, University College Dublin
```

