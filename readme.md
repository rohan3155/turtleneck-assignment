# 🛡️ SIEM Log Ingestion System

This is a Django-based backend system that simulates a simple SIEM (Security Information and Event Management) log ingestion pipeline.

It provides APIs to ingest logs, filter them, and optionally simulate real-time ingestion using a Python script.

---

## 📦 Features

* RESTful API for log ingestion and retrieval
* Filtering by `source_ip`, `level`, `timestamp`
* SQLite database for simplicity
* Log sender script to simulate real-time log pushing
* Admin dashboard to view and manage logs

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/siem-log-ingestion.git
cd siem-log-ingestion
```

### 2. Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not available, install manually:

```bash
pip install django djangorestframework django-filter requests
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional - for Admin Panel)

```bash
python manage.py createsuperuser
```

### 6. Start the Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🚀 API Endpoints

### 🔹 POST `/api/logs/`

Submit a single log entry.

```json
{
  "timestamp": "2025-06-25T10:05:32Z",
  "source_ip": "192.168.1.101",
  "event_type": "login_failed",
  "level": "warning",
  "message": "User admin failed login 3 times"
}
```

### 🔹 GET `/api/logs/`

Fetch logs with optional filters:

* `source_ip`
* `level`
* `timestamp`

**Example:**

```
GET /api/logs/?source_ip=192.168.1.101&level=warning
```

---

## 📄 Example `alerts.json`

```json
[
  {
    "timestamp": "2025-06-25T10:05:32Z",
    "source_ip": "192.168.1.101",
    "event_type": "login_failed",
    "level": "warning",
    "message": "User admin failed login 3 times"
  },
  {
    "timestamp": "2025-06-25T10:06:15Z",
    "source_ip": "192.168.1.102",
    "event_type": "login_success",
    "level": "info",
    "message": "User test logged in successfully"
  }
]
```

---

## 🐍 Run Log Sender Script

Make sure the server is running.

```bash
python log_sender.py
```

This will read from `alerts.json` and POST each log to the API with a delay.

---

## 🔐 Admin Panel

Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
Login with your superuser credentials to view logs in the Django admin.

---

## 📚 Dependencies

* Django
* djangorestframework
* django-filter
* requests

---

## 📌 Author

Built with ❤️ by Rohan Bhatia for Turtleneck Systems' Backend Developer Assignment.
