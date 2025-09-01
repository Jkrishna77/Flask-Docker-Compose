# Flask + Docker + Nginx Load Balancer

A simple Flask web application containerized with Docker.  

## 🚀 Project Scope

1. Locally on your machine
2. Inside a Docker container
3. Run application using Docker Compose
4. Use nginx reverse proxy to loadbalance between three app instances

---

## 📂 Project Structure
```bash
flask-docker-app/
│── app/
│ ├── main.py
│ ├── routes.py
│ └── templates/
│ └── index.html
│── nginx/
│ └── nginx.conf
│── requirements.txt
│── Dockerfile
│── docker-compose.yml
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

## 🐳 Run with Docker (Single Instance) 

```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```
Visit 👉 http://127.0.0.1:5000

🐙 Run with Docker Compose (Single Flask Service)
```bash
docker-compose up --build
```
Visit 👉 http://127.0.0.1:5000

## 🌍 Run with Docker Compose + Nginx Load Balancer
```bash
docker-compose up --build
```

Now visit 👉 http://localhost

Refresh the page multiple times.
You’ll see alternating responses:

Hello from Flask-App1 🚀

Hello from Flask-App2 🚀
Hello from Flask-App3 🚀


This demonstrates round-robin load balancing by Nginx.
