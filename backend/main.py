from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Leyton Document Platform API",
    description="API de gestion documentaire intelligente pour Leyton",
    version="0.1.0"
)

# Configuration CORS pour le frontend React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Leyton API is running 🚀"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
