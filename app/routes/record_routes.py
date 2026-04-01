from fastapi import APIRouter, Depends, Request
from datetime import date
from sqlalchemy import or_
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.models.record import Record
from app.schemas.record import RecordCreate
from app.core.security import require_role
from app.services.record_service import get_filtered_records
from app.core.limiter import limiter   
router = APIRouter(prefix="/records")
@router.post("/")
def create_record(record: RecordCreate,db: Session = Depends(get_db),admin=Depends(require_role(["admin"]))):
    db_record = Record(**record.dict(), user_id=1)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

@router.get("/")
@limiter.limit("5/minute")
def get_records(request: Request,type: str = None,category: str = None,start_date: date = None,end_date: date = None,skip: int = 0,limit: int = 10,db: Session = Depends(get_db),user=Depends(require_role(["admin", "analyst", "viewer"]))):
    query = db.query(Record).filter(Record.is_deleted == False)
    if type:
        query = query.filter(Record.type == type)
    if category:
        query = query.filter(Record.category == category)
    if start_date:
        query = query.filter(Record.date >= start_date)
    if end_date:
        query = query.filter(Record.date <= end_date)

    return query.offset(skip).limit(limit).all()

@router.get("/clean")
def clean_records(db: Session = Depends(get_db)):
    return get_filtered_records(db, {})

@router.get("/search")
def search_records(query: str,db: Session = Depends(get_db),user=Depends(require_role(["admin", "analyst", "viewer"]))):
    results = db.query(Record).filter(Record.is_deleted == False).filter(or_(Record.category.ilike(f"%{query}%"),Record.notes.ilike(f"%{query}%"))).all()
    return results

@router.delete("/{id}")
def delete_record(id: int, db: Session = Depends(get_db)):
    record = db.query(Record).filter(Record.id == id).first()
    if not record:
        return {"error": "Record not found"}
    record.is_deleted = True
    db.commit()
    return {"message": "Record marked as deleted"}