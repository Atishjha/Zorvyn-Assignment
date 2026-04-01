from sqlalchemy import Column,Integer,String,Float,Date,ForeignKey
from app.db.database import Base
class Record(Base):
    __tablename__ = "records"
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    amount = Column(Float)
    type = Column(String)
    category = Column(String)
    date = Column(Date)
    notes = Column(String)
    is_deleted = Column(Integer,default=0)