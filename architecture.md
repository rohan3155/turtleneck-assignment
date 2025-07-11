# 🏗️ SIEM Log Ingestion System Architecture

This document describes the architecture and working of the SIEM (Security Information and Event Management) log ingestion system developed as part of the backend developer assignment.

---

## 📌 Objective

To simulate a simple SIEM system that:

* Accepts logs via a REST API
* Stores them in a database
* Supports filtering and querying
* Mimics real-time log ingestion using a sender script

---

## 🔧 Components Overview

| Component       | Description                                                 |
| --------------- | ----------------------------------------------------------- |
| Django Backend  | Handles API requests, data validation, and database storage |
| SQLite Database | Stores all ingested logs                                    |
| `log_sender.py` | Python script to simulate real-time log pushing             |
| `alerts.json`   | Sample log entries used by the sender script                |
| Admin Panel     | Django admin interface to view logs manually                |

---

## 🔁 Log Ingestion Flow

```text
+-------------------+
|  alerts.json      | ← contains sample logs
+-------------------+
           |
           | (reads)
           v
+-------------------+     POST    +-----------------------+
| log_sender.py     | --------->  | Django REST API       |
+-------------------+             | /api/logs/ (POST)     |
                                  +-----------------------+
                                            |
                                            v
                                  +-----------------------+
                                  | SQLite Database       |
                                  +-----------------------+
```

### 📝 Log Format

Each log has the following fields:

* `timestamp` (ISO format)
* `source_ip` (IPv4)
* `event_type` (string)
* `level` (info/warning/error)
* `message` (free-text)

---

## 🧪 API Design

### 🔹 POST `/api/logs/`

Ingest a new log (single JSON object).

### 🔹 GET `/api/logs/`

Retrieve logs with optional filters:

* `?source_ip=...`
* `?level=...`
* `?timestamp=...`

---

## ⚙️ Django Model

```python
class Log(models.Model):
    timestamp = models.DateTimeField()
    source_ip = models.GenericIPAddressField()
    event_type = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    message = models.TextField()
```

---

## 🧠 Assumptions

* Logs arrive in valid JSON format.
* Real-time ingestion is simulated with `time.sleep()`.
* SQLite is used for simplicity; can be swapped with PostgreSQL in production.
* No authentication is enforced (for assignment scope).

---

## ✅ Technologies Used

* Python 3.9
* Django 4.2
* Django REST Framework
* SQLite
* `requests` (for sender script)
* Django Admin

---

## 📚 Future Improvements (Optional)

* Add JWT authentication
* Implement rule engine (e.g., detect brute force attacks)
* Add Swagger UI using `drf-spectacular`
* Store logs in PostgreSQL for scalability

---

## 🙌 Conclusion

This system demonstrates the core components of a real-world SIEM pipeline:

* Log ingestion
* Storage
* Query/filter
* Basic documentation

Ready for extension with real-time detection, alerts, and dashboards.
