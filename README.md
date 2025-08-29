# Flask + Docker Starter Project

A simple Flask web application containerized with Docker.  
This project demonstrates how to run a Flask app:
1. Locally on your machine
2. Inside a Docker container

Later, we will extend this with **Nginx** and **Docker Compose**.

---

## 🚀 Project Scope
- Build a basic Flask app with routes and templates
- Run the app locally with `venv`
- Containerize the app with a Dockerfile
- Expose the app on `http://localhost:5000`

---

## 📂 Project Structure
```bash
flask-docker-app/
│── app/
│ ├── main.py
│ ├── routes.py
│ └── templates/
│ └── index.html
│── requirements.txt
│── Dockerfile
│── README.md
```
---

## 🛠️ Run Locally (Without Docker)

### 1. Create a virtual environment
```bash
python -m venv venv
```
2. Activate the environment

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the app
```bash
python app/main.py
```

App will be available at 👉 http://127.0.0.1:5000