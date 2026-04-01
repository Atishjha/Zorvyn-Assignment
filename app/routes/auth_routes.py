from fastapi import APIRouter,Depends,HTTPException 
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.models.user import User
from app.core.hashing import verify_password
from app.core.auth import create_access_token 
router = APIRouter(prefix="/auth")
@router.post("/login")
def login(email:str,password:str,db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password,user.password):
        raise HTTPException(status_code=401,detail="Invalid credentials")
    token = create_access_token({"user_id":user.id,"role":user.role})
    return {"access_token":token}

