# Task 3 - Object Detection Using YOLO

## Overview
In this task, we will use YOLO (You Only Look Once), a popular object detection model, to detect objects in images. We will process images collected from a Telegram channel, extract relevant data (bounding box coordinates, confidence scores, and class labels), and store the detection results in a database.

## Setting Up the Environment

Ensure you have the necessary dependencies installed for YOLO and its required libraries. You can use either the PyTorch-based YOLO model or the TensorFlow-based YOLO model. Below are the installation steps for both:

### Install Dependencies:
1. **Install OpenCV (for image processing)**:
    ```bash
    pip install opencv-python
    ```

2. **Install PyTorch and torchvision (for PyTorch-based YOLO)**:
    ```bash
    pip install torch torchvision
    ```

3. **Install TensorFlow (for TensorFlow-based YOLO)**:
    ```bash
    pip install tensorflow
    ```

4. **Clone the YOLOv5 repository** (PyTorch-based):
    ```bash
    git clone https://github.com/ultralytics/yolov5.git
    cd yolov5
    pip install -r requirements.txt
    ```

### Install Additional Required Libraries:
1. **Pandas** (for handling detection results):
    ```bash
    pip install pandas
    ```

2. **SQLite** (for storing detection data):
    ```bash
    pip install sqlite3
    ```

## Downloading the YOLO Model

1. Clone the YOLOv5 repository:
    ```bash
    git clone https://github.com/ultralytics/yolov5.git
    cd yolov5
    pip install -r requirements.txt
    ```

2. Download the pre-trained YOLO model from the repository. This model will be used to detect objects in images.

## Preparing the Data

1. **Collect images from the Chemed Telegram Channel**: 
    - Visit the [Chemed Telegram Channel](https://t.me/lobelia4cosmetics) to gather images for object detection.

2. **Store the images**: Ensure the images are stored in a directory that can be accessed by your script. Set the input directory path in the script accordingly.

## Processing the Detection Results

1. **Run Object Detection with YOLO**: Use the pre-trained YOLO model to detect objects in the collected images.
2. **Extract Data**: From the detection results, extract bounding box coordinates, confidence scores, and class labels for each detected object.
3. **Save Detection Results**: Save the extracted data (image path, label, confidence, bounding box coordinates) to an SQLite database.

### Sample Detection Results:
For each image, the following data will be stored in the database:
- `image_path`: Path to the image file
- `label`: The class label of the detected object
- `confidence`: The confidence score of the detection
- `xmin, ymin, xmax, ymax`: Coordinates of the bounding box
- `timestamp`: Timestamp of when the detection was performed

## Storing Detection Data in Database

The detection results will be stored in an SQLite database. The database will have a table `detections` with the following structure:

```sql
CREATE TABLE IF NOT EXISTS detections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_path TEXT,
    label TEXT,
    confidence REAL,
    xmin REAL,
    ymin REAL,
    xmax REAL,
    ymax REAL,
    timestamp TEXT
);