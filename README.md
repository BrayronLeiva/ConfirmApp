# 🧩 ConfirmApp — Backend API

Backend system to manage users, sessions, attendance, and game-like learning features. Designed to support educational platforms through modern API practices, modular structure, and secure authentication using JWT.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-FF6F00?style=for-the-badge)
![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![Pydantic](https://img.shields.io/badge/Validation-Pydantic-0696D7?style=for-the-badge)

## 🚀 Key Features

### 👨‍🎓 For Students
- Token-based authentication (JWT)
- Game-based questions and categories
- Attendance tracking linked to sessions

### 🏢 For Administrators
- User and role management
- Session and attendance monitoring
- API-based data access for frontend integration

## 🏗️ Technical Architecture

### Layered Design
API (Routers) → Services → Repositories → Models/Database
↑
DTOs (Pydantic)

bash
Copiar
Editar

### Technology Stack

| Layer               | Technologies                                                                 |
|---------------------|------------------------------------------------------------------------------|
| **API Layer**        | FastAPI, APIRouter, Swagger UI                                               |
| **Service Layer**    | Custom service classes for business logic                                    |
| **Data Layer**       | SQLAlchemy, SQLite (can be switched), Alembic (optional)                     |
| **Security**         | JWT, OAuth2PasswordBearer, Password Hashing (bcrypt)                         |
| **Schemas/DTOs**     | Pydantic models for request/response validation                              |
| **Dependency Mgmt.** | `requirements.txt`, virtualenv, pip    
