# Task 4 - Expose the collected data using FastAPI

## Setting Up the Environment:
- **Install FastAPI and Uvicorn:**
  ```bash
  pip install fastapi uvicorn
### Create a FastAPI Application:
### Set up a basic project structure:
my_project/
├── main.py
├── database.py
├── models.py
├── schemas.py
└── crud.py

### Database Configuration
In database.py, configure the database connection using SQLAlchemy.

### Creating Data Models
In models.py, define SQLAlchemy models for the database tables.

### Creating Pydantic Schemas
In schemas.py, define Pydantic schemas for data validation and serialization.

### CRUD Operations
In crud.py, implement CRUD (Create, Read, Update, Delete) operations for the database.

### Creating API Endpoints
In main.py, define the API endpoints using FastAPI.
