from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    YOUNG = "young"
    ADMIN = "admin"