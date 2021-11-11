from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
import cruds, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id: int, title: str = None):
    return {"item_id": item_id, "title": title}

@router.post("/items/", response_model=schemas.Item)
async def create_item_for_user(
    item: schemas.Item, db: Session = Depends(get_db)
):
    return cruds.create_item(db=db, item=item)

@router.get("/items/", response_model=List[schemas.Item])
async def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = cruds.get_items(db, skip=skip, limit=limit)
    return items