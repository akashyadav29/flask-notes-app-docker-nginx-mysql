# 🚀 Flask Notes App (Docker | MySQL | Nginx)

A **3-tier notes application** built using Flask, MySQL, and Nginx, fully containerized with Docker and Docker Compose.

---

## 📌 Tech Stack

* Flask (Backend)
* MySQL (Database)
* Nginx (Reverse Proxy)
* Docker & Docker Compose
* Multi-stage Docker Build
* Environment Variables
* Healthchecks

---

## 🧱 Architecture

```
Browser
   ↓
Nginx (Port 80)
   ↓
Flask App (Port 5000)
   ↓
MySQL Database (Port 3306)
```

---

## 📂 Project Structure

```
notes-app/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│
├── nginx/
│   └── default.conf
│
├── Dockerfile
├── docker-compose.yml
└── .env
```

---

## ⚙️ Features

* Add and delete notes
* Color-based notes (Google Keep style)
* Persistent storage using Docker volumes
* Reverse proxy using Nginx
* Multi-container setup
* Healthchecks for reliability
* Environment variables for secure config

---

## 🐳 Run the Project

### 1️⃣ Clone the repo

```
git clone https://github.com/<your-username>/flask-notes-app-docker-nginx-mysql.git
cd flask-notes-app-docker-nginx-mysql
```

### 2️⃣ Start containers

```
docker compose up -d --build
```

### 3️⃣ Open in browser

```
http://<EC2-PUBLIC-IP>
```

---

## 🗄 Database Setup

Enter MySQL container:

```
docker exec -it mysql mysql -uroot -p
```

Run:

```
USE notesdb;

CREATE TABLE notes(
id INT AUTO_INCREMENT PRIMARY KEY,
content TEXT,
color VARCHAR(20)
);
```

---

## 🔐 Environment Variables

Stored in `.env`:

```
MYSQL_ROOT_PASSWORD=password
MYSQL_DATABASE=notesdb
MYSQL_HOST=mysql
```

---

## 🧠 DevOps Concepts Used

* Docker Multi-stage Build
* Docker Compose
* Reverse Proxy (Nginx)
* Container Networking
* Healthchecks
* Environment Variables
* Persistent Volumes

---

## 👨‍💻 Author

Akash Yadav
