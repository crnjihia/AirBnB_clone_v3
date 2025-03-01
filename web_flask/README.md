# 0x04. AirBnB Clone - Web Framework

## Background Context

This project focuses on building a web application using Flask, a lightweight web framework in Python. By completing this project, you will gain hands-on experience with Flask, including routing, templates, and integrating with a storage engine (FileStorage or DBStorage). You will also learn how to create dynamic web pages and handle data from a database.

## Requirements

| Category         | Details |
|------------------|---------|
| **Project Type** | Mandatory |
| **Review**       | Manually reviewed by peers or TAs |
| **Python Version** | Python 3.4.3 (Ubuntu 20.04 LTS) |
| **Flask Version** | Flask 1.1.2 |
| **README**       | A `README.md` file at the root of the project folder is mandatory |
| **File Extension** | All Python scripts must end with `.py` |

## General Requirements

1. **Python Scripts**: All Python scripts must be executable and follow PEP 8 style guidelines.
2. **File Structure**: All files should end with a new line, and the first line of each Python script must be a shebang (`#!/usr/bin/python3`).
3. **Ubuntu 20.04 LTS**: All files will be interpreted on Ubuntu 20.04 LTS.
4. **Flask Configuration**: Flask must be properly configured and running on the server.

## Tasks

| Task                          | Description                                  | Files                         |
|-------------------------------|---------------------------------------------|-------------------------------|
| **0. Hello Flask!**           | Write a script that starts a Flask web application and displays "Hello HBNB!" at the root route. | `0-hello_route.py` |
| **1. HBNB**                   | Add a new route `/hbnb` that displays "HBNB". | `1-hbnb_route.py` |
| **2. C is fun!**              | Add a route `/c/<text>` that displays "C " followed by the value of the `text` variable. | `2-c_route.py` |
| **3. Python is cool!**        | Add a route `/python/<text>` that displays "Python " followed by the value of the `text` variable. | `3-python_route.py` |
| **4. Is it a number?**        | Add a route `/number/<n>` that displays "<n> is a number" only if `n` is an integer. | `4-number_route.py` |
| **5. Number template**        | Add a route `/number_template/<n>` that displays an HTML page only if `n` is an integer. | `5-number_template.py`, `templates/5-number.html` |
| **6. Odd or even?**           | Add a route `/number_odd_or_even/<n>` that displays an HTML page indicating if `n` is odd or even. | `6-number_odd_or_even.py`, `templates/6-number_odd_or_even.html` |
| **7. Improve engines**        | Update the `FileStorage` and `DBStorage` engines to include a `close` method. | `models/engine/file_storage.py`, `models/engine/db_storage.py`, `models/state.py` |
| **8. List of states**         | Add a route `/states_list` that displays a list of all State objects from the database. | `7-states_list.py`, `templates/7-states_list.html` |
| **9. Cities by states**       | Add a route `/cities_by_states` that displays a list of all State objects and their associated City objects. | `8-cities_by_states.py`, `templates/8-cities_by_states.html` |
| **10. States and State**      | Add routes `/states` and `/states/<id>` to display State objects and their associated City objects. | `9-states.py`, `templates/9-states.html` |
| **11. HBNB filters**          | Add a route `/hbnb_filters` that displays a page with filters for States, Cities, and Amenities. | `10-hbnb_filters.py`, `templates/10-hbnb_filters.html`, `web_flask/static/` |
| **12. HBNB is alive!**        | Add a route `/hbnb` that displays a complete web page with filters and places. | `100-hbnb.py`, `templates/100-hbnb.html`, `web_flask/static/` |

## Submission

- **GitHub Repository**: [AirBnB_clone_v2](https://github.com/Achrafsadeq/AirBnB_clone_v2)
- **Directory**: `web_flask`
---

### Mission Director

This project is part of the ALX Software Engineering Program.

### Developer

**Codename**: Achraf Sadeq

### Acknowledgments

This project was developed by Holberton School, in collaboration with the ALX Software Engineering Program, to provide practical, hands-on learning experiences in a professional and real-world context. It aims to equip learners with the skills and knowledge necessary to tackle complex challenges in software engineering.
