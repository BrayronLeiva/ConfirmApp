# 🧩 ConfirmApp — Backend API for Managing Attendance, Sessions & Learning Activities

Backend system to manage users, sessions, attendance, and game-like learning features. Designed to support educational platforms through modern API practices, modular structure, and secure authentication using JWT.

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
