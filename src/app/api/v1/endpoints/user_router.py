# third party
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

# local
from src.infrastructure.db.models.user_model import UserModel
from src.infrastructure.config.settings import settings
from src.app.api.dependencies.db import get_db

router = APIRouter()


@router.get("/info")
def info():
    return {
        "redis": f"{settings.REDIS_HOST}:{settings.REDIS_PORT}",
        "secret_key": settings.SECRET_KEY,
        "dns": settings.DNS,
        "access_token_expire_minutes": settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        "refresh_token_expire_days": settings.REFRESH_TOKEN_EXPIRE_DAYS,
    }


@router.get("/health")
def health_check():
    return {"status": "ok", "message": "API is healthy"}


@router.get("/list_all")
def list_users(db: Session = Depends(get_db)):
    try:
        # Exemplo de listagem — substitua 'users' por uma tabela real
        result = db.execute(text("SELECT * FROM users"))
        rows = result.fetchall()
        return {"success": True, "data": [dict(row._mapping) for row in rows]}
        # result_output = []
        # for row in result:
        #     result_output.append(dict(row))
        # return {"success": True, "data": result_output}
    except Exception as e:
        return {"success": False, "error": str(e)}


@router.post("/register")
def register(name: str, email: str, cpf: str, password: str, db: Session = Depends(get_db)):
    try:
        name = name.lower().strip()
        email = email.lower().strip()
        cpf = cpf
        password = password.strip()

        new_user = UserModel(name=name, email=email, cpf=cpf, password=password)
        db.add(new_user)
        db.commit()

        db.commit()
        db.refresh(result)
        tables = result.fetchall()
    except Exception as e:
        return {"success": False, "error": str(e)}


@router.post("/soft_delete")
def soft_delete(db: Session = Depends(get_db)):
    try:
        # Exemplo de soft delete — substitua 'users' e 'id' por uma tabela e coluna reais
        db.execute("UPDATE users SET is_active = FALSE WHERE id = :id", {"id": "some-uuid"})
        db.commit()
        return {"success": True, "message": "Soft delete executado com sucesso"}
    except Exception as e:
        return {"success": False, "error": str(e)}


@router.post("/hard_delete")
def hard_delete(db: Session = Depends(get_db)):
    try:
        # Exemplo de hard delete — substitua 'users' e 'id' por uma tabela e coluna reais
        db.execute("DELETE FROM users WHERE id = :id", {"id": "some-uuid"})
        db.commit()
        return {"success": True, "message": "Hard delete executado com sucesso"}
    except Exception as e:
        return {"success": False, "error": str(e)}


@router.post("update")
def update(db: Session = Depends(get_db)):
    try:
        # Exemplo de update — substitua 'users', 'name' e 'id' por uma tabela e colunas reais
        db.execute("UPDATE users SET name = :name WHERE id = :id", {"name": "New Name", "id": "some-uuid"})
        db.commit()
        return {"success": True, "message": "Update executado com sucesso"}
    except Exception as e:
        return {"success": False, "error": str(e)}
