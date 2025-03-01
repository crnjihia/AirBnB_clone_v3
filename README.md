# 0x05. AirBnB Clone - RESTful API

## Background Context

This project builds upon the previous AirBnB Clone project by introducing a RESTful API using Flask. The goal is to create a web service that allows clients to interact with the AirBnB clone application programmatically. This includes retrieving, creating, updating, and deleting resources such as users, places, states, cities, amenities, and reviews.

By completing this project, you will gain experience in building RESTful APIs, handling HTTP requests and responses, and integrating with a database using Flask. You will also learn how to implement CRUD (Create, Read, Update, Delete) operations for various resources.

## Requirements

| Category         | Details |
|------------------|---------|
| **Project Type** | Mandatory |
| **Review**       | Manually reviewed by peers or TAs |
| **Python Version** | Python 3.4.3 (Ubuntu 20.04 LTS) |
| **Flask Version** | Flask 1.1.2 |
| **Flask-CORS**   | Flask-CORS for handling cross-origin requests |
| **README**       | A `README.md` file at the root of the project folder is mandatory |
| **File Extension** | All Python scripts must end with `.py` |

## General Requirements

1. **Python Scripts**: All Python scripts must be executable and follow PEP 8 style guidelines.
2. **File Structure**: All files should end with a new line, and the first line of each Python script must be a shebang (`#!/usr/bin/python3`).
3. **Ubuntu 20.04 LTS**: All files will be interpreted on Ubuntu 20.04 LTS.
4. **Flask Configuration**: Flask must be properly configured and running on the server.
5. **CORS**: Implement CORS to allow cross-origin requests.

## Tasks
---

| **Task**                          | **Description**                                                                 | **Files**                                                                 |
|-----------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **0. Restart from scratch!**      | Fork the AirBnB_clone_v2 repository and rename it to AirBnB_clone_v3. Update the README.md and ensure all tests pass. | `README.md`, `tests/`                                                    |
| **1. Never fail!**                | Ensure all existing tests pass and add new tests for API endpoints.              | `tests/`                                                                 |
| **2. Improve storage**            | Add `get(cls, id)` and `count(cls=None)` methods to `DBStorage` and `FileStorage`. | `models/engine/db_storage.py`, `models/engine/file_storage.py`, `tests/` |
| **3. Status of your API**         | Create an endpoint `/api/v1/status` that returns the API status.                 | `api/v1/app.py`, `api/v1/views/index.py`                                 |
| **4. Some stats?**                | Create an endpoint `/api/v1/stats` that returns the count of each object type.    | `api/v1/views/index.py`                                                  |
| **5. Not found**                  | Implement a 404 error handler that returns a JSON response for undefined routes.  | `api/v1/app.py`                                                          |
| **6. State**                      | Create endpoints for managing `State` objects (GET, POST, PUT, DELETE).          | `api/v1/views/states.py`, `api/v1/views/__init__.py`                     |
| **7. City**                       | Create endpoints for managing `City` objects (GET, POST, PUT, DELETE).           | `api/v1/views/cities.py`, `api/v1/views/__init__.py`                     |
| **8. Amenity**                    | Create endpoints for managing `Amenity` objects (GET, POST, PUT, DELETE).        | `api/v1/views/amenities.py`, `api/v1/views/__init__.py`                  |
| **9. User**                       | Create endpoints for managing `User` objects (GET, POST, PUT, DELETE).           | `api/v1/views/users.py`, `api/v1/views/__init__.py`                      |
| **10. Place**                     | Create endpoints for managing `Place` objects (GET, POST, PUT, DELETE).          | `api/v1/views/places.py`, `api/v1/views/__init__.py`                     |
| **11. Reviews**                   | Create endpoints for managing `Review` objects (GET, POST, PUT, DELETE).          | `api/v1/views/places_reviews.py`, `api/v1/views/__init__.py`             |
| **12. HTTP access control (CORS)**| Implement CORS to allow cross-origin requests using `flask_cors`.                | `api/v1/app.py`                                                          |
| **13. Place - Amenity**           | Create endpoints for managing the relationship between `Place` and `Amenity`.     | `api/v1/views/places_amenities.py`, `api/v1/views/__init__.py`           |
| **14. Security improvements!**    | Hash user passwords using MD5 and ensure passwords are not returned in responses. | `models/base_model.py`, `models/user.py`                                 |
| **15. Search**                    | Implement a search endpoint `/api/v1/places_search` to filter places by state, city, and amenities. | `api/v1/views/places.py`                                                 |

---


### Mission Director

This project is part of the ALX Software Engineering Program.

### Developer

**Codename**: Achraf Sadeq & Elhoucine Smaili

### Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.

