from pydantic import BaseModel

# Schema for creating a detected object
class DetectedObjectCreate(BaseModel):
    image_filename: str
    class_name: str
    confidence: float
    xmin: int
    ymin: int
    xmax: int
    ymax: int

# Schema for reading a detected object
class DetectedObject(BaseModel):
    id: int
    image_filename: str
    class_name: str
    confidence: float
    xmin: int
    ymin: int
    xmax: int
    ymax: int

    class Config:
        from_attributes = True  # Enable ORM mode