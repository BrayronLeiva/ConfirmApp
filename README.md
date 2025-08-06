# ConfirmApp

**ConfirmApp** is a backend application built with Python that provides a RESTful API to manage users, sessions, attendance, game questions, and more. It uses FastAPI as the main web framework, SQLAlchemy for database interaction, and JWT for authentication.

## 🚀 Technologies Used

- Python 3.12
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [JWT (JSON Web Tokens)](https://jwt.io/)
- SQLite (default database, can be replaced)

## 📁 Project Structure

ConfirmApp/
├── main.py # Entry point
├── requirements.txt # Python dependencies
├── app/
│ ├── config/ # Database and security config
│ │ ├── database.py
│ │ ├── init_db.py
│ │ └── security/
│ │ └── jwt_utils.py
│ ├── dtos/ # Data Transfer Objects (schemas)
│ ├── models/ # Database models
│ ├── repositories/ # Data access logic
│ ├── routers/ # API endpoints
│ └── services/ # Business logic
