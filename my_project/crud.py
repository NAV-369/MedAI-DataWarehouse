from sqlalchemy.orm import Session
from .models import DetectedObject
from .schemas import DetectedObjectCreate

def create_detected_object(db: Session, detected_object: DetectedObjectCreate):
    db_object = DetectedObject(**detected_object.model_dump())
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    return db_object

def get_detected_objects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DetectedObject).offset(skip).limit(limit).all()

def get_detected_object(db: Session, object_id: int):
    return db.query(DetectedObject).filter(DetectedObject.id == object_id).first()

def update_detected_object(db: Session, object_id: int, detected_object: DetectedObjectCreate):
    db_object = db.query(DetectedObject).filter(DetectedObject.id == object_id).first()
    if db_object:
        for key, value in detected_object.model_dump().items():
            setattr(db_object, key, value)
        db.commit()
        db.refresh(db_object)
    return db_object

def delete_detected_object(db: Session, object_id: int):
    db_object = db.query(DetectedObject).filter(DetectedObject.id == object_id).first()
    if db_object:
        db.delete(db_object)
        db.commit()
    return db_object