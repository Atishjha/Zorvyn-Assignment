from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func,extract
from app.db.deps import get_db
from app.models.record import Record

router = APIRouter(prefix="/dashboard")
@router.get("/category")
def category_summary(db: Session = Depends(get_db)):
    data = db.query(Record.category,func.sum(Record.amount)).group_by(Record.category).all()
    return [{"category": c, "total": t} for c, t in data]
@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):

    income = db.query(func.sum(Record.amount)).filter(Record.type == "income").scalar()
    expense = db.query(func.sum(Record.amount)).filter(Record.type == "expense").scalar()

    return {
        "total_income": income or 0,
        "total_expense": expense or 0,
        "net_balance": (income or 0) - (expense or 0)
    }

@router.get("/trends")
def monthly_trends(db:Session = Depends(get_db)):
    data = db.query(extract('month',Record.date).label("month"),func.sum(Record.amount)).group_by("month").all()
    return [{"month":int(m),"total":t}for m,t in data] 

@router.get("/recent")
def recent_records(db: Session = Depends(get_db)):
    return db.query(Record).order_by(Record.date.desc()).limit(5).all()