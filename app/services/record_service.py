from sqlalchemy.orm import Session
from app.models.record import Record
def get_filtered_records(db: Session,filters:dict):
    query = db.query(Record)
    if filters.get("type"):
        query = query.filter(Record.type == filters["type"])
    if filters.get("category"):
        query = query.filter(Record.category == filters["category"])
    return query.all()