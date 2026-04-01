from fastapi import APIRouter,Depends 
from sqlalchemy.orm import Session
from app.core.hashing import hash_password
from app.db.deps import get_db
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import require_role
router = APIRouter(prefix="/users")
@router.post("/")
def create_user(user:UserCreate,db:Session = Depends(get_db),admin=Depends(require_role(["admin"]))):
    db_user = User(name =user.name,email=user.email,password=hash_password(user.password),role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
