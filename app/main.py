from fastapi import FastAPI
from datetime import datetime
import socket

app = FastAPI(title="EKS Production Microservice")


@app.get("/")
def root():
    return {
        "service": "eks-microservice",
        "message": "Hello from Amazon EKS - version 2",
        "hostname": socket.gethostname(),
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/api")
def api():
    return {
        "message": "Production-style microservice is running",
        "platform": "Amazon EKS"
    }
