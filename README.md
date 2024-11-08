# med_sku_catalogue 

A backend service for managing a medication SKU catalogue using Django Rest Framework (DRF). It supports CRUD operations, bulk upload, filtering, searching, and ordering of medication SKUs.

# Features
- CRUD Operations: Create, read, update, and delete medication SKUs.
- Bulk Upload: Upload multiple medication SKUs at once.
- Filtering, Searching, and Ordering: Easily find medication SKUs using filters and search.
- Test Case :- Added test case as well for testing the Api.

# Requirements
- Python 3.8 or higher
- Django 4.x
- Django Rest Framework
- SQLite (default, can be changed to PostgreSQL/MySQL)

# Installation
## Step 1: Clone the repository
```bash
git clone https://github.com/rishistrive/med_sku_catalogue.git
cd med_sku_catalogue
```

2.Build the Docker image:
```bash
sudo docker compose up --build
```
3.Access the application at http://0.0.0.0:8000/api/docs/swagger/
