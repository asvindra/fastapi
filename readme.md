# 📝 Todo API (FastAPI + PostgreSQL + Docker)

A simple and clean Todo backend API built using FastAPI, SQLAlchemy, PostgreSQL, and Docker.  
This project follows best practices for environment variable management and containerized development.

---

## 🚀 Tech Stack

- FastAPI – High-performance Python web framework
- SQLAlchemy – ORM for database interactions
- PostgreSQL – Relational database
- psycopg – PostgreSQL driver
- Docker – Containerization
- Uvicorn – ASGI server

---

## 📦 Project Structure

.
├── main.py
├── db.py
├── models.py
├── schemas.py
├── requirements.txt
├── Dockerfile
└── README.md

---

## ⚙️ Prerequisites

- Python 3.11+
- PostgreSQL 15+
- Docker (optional but recommended)

---

## 🗄️ Database Setup (Local)

Database used:
todos

Verify:

```bash
psql -d todos
🔐 Environment Variables
.env files are NOT committed to the repository.

Required variable:

DATABASE_URL=postgresql+psycopg://{username}@host.docker.internal:5432/todos
▶️ Run Locally (Without Docker)
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
Application URL:

http://127.0.0.1:8000
Swagger Docs:

http://127.0.0.1:8000/docs
🐳 Run with Docker
Build Image
docker build -t asvindra/todo .
Run Container
docker run -p 8000:8000 \
  -e DATABASE_URL="postgresql+psycopg://{username}@host.docker.internal:5432/todos" \
  asvindra/todo
Note:

host.docker.internal allows Docker to connect to local PostgreSQL

Supported on macOS and Windows

🧠 Important Notes
No .env file inside Docker image

Environment variables passed at runtime

SQLAlchemy fails fast if DATABASE_URL is missing

Tables are created automatically on startup

🧪 Database Connectivity Check
psql -h localhost -U asvindrar -d todos
❗ Common Errors
role "postgres" does not exist
Use correct local user: asvindrar

database does not exist
Ensure database name is todos

connection refused
Do not use localhost inside Docker
Use host.docker.internal

🛣️ Future Improvements
Alembic migrations

Async SQLAlchemy

Docker Compose

Authentication

Pagination and filtering

👨‍💻 Author
Asvindrar Rajpoot


```
