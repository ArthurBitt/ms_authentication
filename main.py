# third party
from fastapi import FastAPI
# local
from src.app.api.dependencies.db import get_db
from src.app.api.v1.endpoints import user_router, auth_router

app = FastAPI()

app.include_router(user_router.router, prefix="/api/v1")
app.include_router(auth_router.router, prefix="/api/v1")

@app.on_event("startup")
def test_db_connection():
    try:
        db = next(get_db())
        print("✅ Conexão com o banco estabelecida com sucesso!")
    except Exception as e:
        print("❌ Erro ao conectar no banco:", e)
        raise

@app.on_event("shutdown")
def shutdown_event():
    print("👋 Encerrando aplicação e liberando recursos...")
