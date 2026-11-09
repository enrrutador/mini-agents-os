"""Punto de entrada de la API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

app = FastAPI(
    title="Mini-Agents OS",
    description="Sistema Operativo de Comunidades de Mini-Agentes",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "mini-agents-os",
        "version": "0.1.0",
    }


@app.get("/")
async def root():
    return {
        "message": "Mini-Agents OS API",
        "docs": "/docs",
        "health": "/health",
    }
