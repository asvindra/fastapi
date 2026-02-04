# FastAPI Todo App (Docker + PostgreSQL)

A production-style FastAPI application containerized with Docker and orchestrated using Docker Compose.  
The project follows clean separation of concerns: application code, configuration, and infrastructure.

---

## 🚀 Tech Stack

- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL 15
- Docker
- Docker Compose

---

## 📁 Project Folder Structure

FastAPI/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── db.py
│ ├── models.py
│ └── routers/
│ └── todo.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md

---

## 🧱 Architecture Overview

- FastAPI runs in its own Docker container
- PostgreSQL runs in a separate Docker container
- Containers communicate via a private Docker network
- Database credentials are provided via environment variables
- No secrets or `.env` files are committed to git
- Application image is reusable across environments

---

## 🐳 Docker Image

The FastAPI application is prebuilt and published as:

asvindra/todo:latest

This image contains **no environment-specific configuration**.

---

## 📄 docker-compose.yml

```yaml
services:
  api:
    image: asvindra/todo:latest
    container_name: todo-api
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: ${DATABASE_URL}
    depends_on:
      - db
    restart: always

  db:
    image: postgres:15
    container_name: todo-db
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: always

volumes:
  postgres_data:
🔐 Environment Variables
Create a .env file locally (do not commit this file):

POSTGRES_DB=dbname
POSTGRES_USER=username
POSTGRES_PASSWORD=password
DATABASE_URL=postgresql+psycopg://username:password@db:5432/todos
Docker Compose loads this file automatically.

▶️ Running the Application
Start all services:

docker compose up -d
Check status:

docker compose ps
🌐 Access the Application
API:
http://localhost:8000

Swagger Docs:
http://localhost:8000/docs

🛑 Stopping the Application
docker compose down
Remove containers and database data:

docker compose down -v
🧪 Useful Commands
View API logs
docker logs todo-api
Access PostgreSQL shell
docker exec -it todo-db psql -U asvindrar -d todos
```
