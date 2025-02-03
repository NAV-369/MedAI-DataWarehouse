from .database import Base
from sqlalchemy import Column, Integer, String, Float

class DetectedObject(Base):
    __tablename__ = "detected_objects"

    id = Column(Integer, primary_key=True, index=True)
    image_filename = Column(String, index=True)
    class_name = Column(String)
    confidence = Column(Float)
    xmin = Column(Integer)
    ymin = Column(Integer)
    xmax = Column(Integer)
    ymax = Column(Integer)