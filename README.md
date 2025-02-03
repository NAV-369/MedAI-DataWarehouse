
# Building a Data Warehouse for Ethiopian Medical Businesses

## Business Need
You are a data engineer at Kara Solutions, a leading data science company with over 50+ data-centric solutions. You are tasked with Building a data warehouse to store data on Ethiopian medical businesses scrapped from the web and telegram channels. This project involves several key steps and considerations to ensure the data warehouse is robust, scalable, and capable of handling the unique challenges associated with scraping and data collection from Telegram channels. Additionally, it involves integrating object detection capabilities using YOLO (You Only Look Once) to enhance data analysis. 

A data warehouse significantly enhances data analysis. With all data stored centrally, your team can perform comprehensive analyses to find valuable insights about Ethiopian medical businesses. This data helps identify trends, patterns, and correlations that are hard to detect with fragmented data, leading to better decision-making. A well-designed data warehouse also makes querying and reporting more efficient, enabling businesses to get actionable intelligence quickly and accurately.

The implementation of ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) frameworks is a key part of this setup. ETL processes involve extracting data from various sources, transforming it into a suitable format, and then loading it into the data warehouse. This ensures the data is clean, consistent, and ready for analysis. ELT, on the other hand, loads raw data into the data warehouse first and then transforms it as needed. This approach can be more flexible and efficient, especially with the processing power of modern data warehouses. These frameworks are crucial for keeping the data intact and usable, allowing seamless integration and transformation of different data sets.

## Deliverables

### Task 1 - Data Scraping and Collection Pipeline

- **Telegram Scraping:**
  - Utilize the Telegram API or write custom scripts to extract data from public Ethiopian medical business channels:
    - [DoctorsET](https://t.me/DoctorsET)
    - Chemed Telegram Channel ([Lobelia4Cosmetics](https://t.me/lobelia4cosmetics))
    - [Yetenaweg](https://t.me/yetenaweg)
    - [EAHCI](https://t.me/EAHCI)
    - More channels available at [et.tgstat.com/medicine](https://et.tgstat.com/medicine)
  
- **Image Scraping:**
  - Collect images from:
    - Chemed Telegram Channel ([Lobelia4Cosmetics](https://t.me/lobelia4cosmetics))

- **Steps:**
  - Use Python packages like `telethon` for Telegram.
  - Develop scripts or export content using Telegram application.
  
- **Storing Raw Data:**
  - **Initial Storage:** Store raw scraped data temporarily in a local database or files.

- **Monitoring and Logging:**
  - **Logging:** Track the scraping process, errors, and progress.

### Task 2 - Data Cleaning and Transformation

- **Data Cleaning:**
  - Remove duplicates, handle missing values, standardize formats, and validate data.

- **Storing Cleaned Data:**
  - Use a database for storage.

- **DBT for Data Transformation:**
  - **Setting Up DBT:** 
    ```bash
    pip install [dbt](https://x.com/i/grok?text=dbt)
    dbt init my_project
    ```
  - **Defining Models:** Create SQL files for transformations.
  - **Running Models:** 
    ```bash
    dbt run
    ```
  - **Testing and Documentation:** 
    ```bash
    dbt test
    dbt docs generate
    dbt docs serve
    ```

- **Monitoring and Logging:**
  - **Logging:** Track transformation process, errors, and progress.

### Task 3 - Object Detection Using YOLO

- **Setting Up the Environment:**
  - Install necessary dependencies:
    ```bash
    pip install opencv-python
    pip install torch torchvision  # for PyTorch-based YOLO
    pip install tensorflow  # for TensorFlow-based YOLO
    ```

- **Downloading the YOLO Model:**
  ```bash
  git clone https://github.com/ultralytics/yolov5.git
  cd yolov5
  pip install -r requirements.txt

Preparing the Data:
Collect images from Lobelia4Cosmetics.
Use pre-trained YOLO model for detection.
Processing the Detection Results:
Extract bounding box coordinates, confidence scores, class labels.
Store results in a database table.
Monitoring and Logging:
Logging: Track the object detection process, errors, and progress.

### Task 4 - Expose the Collected Data using FastAPI
Setting Up the Environment:
Install FastAPI and Uvicorn:
bash
pip install fastapi uvicorn
Create a FastAPI Application:
Project structure:
my_project/
├── main.py
├── database.py
├── models.py
├── schemas.py
└── crud.py
Database Configuration:
In database.py, set up SQLAlchemy connection.
Creating Data Models:
In models.py, define SQLAlchemy models.
Creating Pydantic Schemas:
In schemas.py, define schemas for validation.
CRUD Operations:
In crud.py, implement database operations.
Creating API Endpoints:
In main.py, define endpoints using FastAPI.


```
