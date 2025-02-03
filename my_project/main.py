from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from my_project.database import SessionLocal, engine
from my_project.models import Base
from my_project.schemas import DetectedObjectCreate, DetectedObject
from my_project.crud import (
    create_detected_object, get_detected_objects, get_detected_object,
    update_detected_object, delete_detected_object
)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a detected object
@app.post("/detected-objects/", response_model=DetectedObject)
def create_object(detected_object: DetectedObjectCreate, db: Session = Depends(get_db)):
    return create_detected_object(db, detected_object)

# Read all detected objects
@app.get("/detected-objects/", response_model=list[DetectedObject])
def read_objects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_detected_objects(db, skip=skip, limit=limit)

# Read a single detected object by ID
@app.get("/detected-objects/{object_id}", response_model=DetectedObject)
def read_object(object_id: int, db: Session = Depends(get_db)):
    db_object = get_detected_object(db, object_id)
    if db_object is None:
        raise HTTPException(status_code=404, detail="Object not found")
    return db_object

# Update a detected object
@app.put("/detected-objects/{object_id}", response_model=DetectedObject)
def update_object(object_id: int, detected_object: DetectedObjectCreate, db: Session = Depends(get_db)):
    db_object = update_detected_object(db, object_id, detected_object)
    if db_object is None:
        raise HTTPException(status_code=404, detail="Object not found")
    return db_object

# Delete a detected object
@app.delete("/detected-objects/{object_id}", response_model=DetectedObject)
def delete_object(object_id: int, db: Session = Depends(get_db)):
    db_object = delete_detected_object(db, object_id)
    if db_object is None:
        raise HTTPException(status_code=404, detail="Object not found")
    return db_object