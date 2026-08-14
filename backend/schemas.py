from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# ==========================================
# TRIP RESPONSE
# ==========================================

class TripResponse(BaseModel):

    id: int

    title: str

    category: Optional[str] = None

    route: Optional[str] = None

    image: Optional[str] = None

    rating: float

    reviews: int

    price: Optional[float] = None

    duration: Optional[str] = None

    difficulty: Optional[str] = None

    description: Optional[str] = None

    tags: Optional[str] = None

    recommended_for: Optional[str] = None

    ai_match: int

    class Config:

        from_attributes = True


# ==========================================
# SIGN UP
# ==========================================

class UserSignup(BaseModel):

    full_name: str

    email: EmailStr

    password: str


# ==========================================
# LOGIN
# ==========================================

class UserLogin(BaseModel):

    email: EmailStr

    password: str


# ==========================================
# USER RESPONSE
# ==========================================

class UserResponse(BaseModel):

    id: int

    full_name: str

    email: str

    profile_image: str | None = None

    created_at: datetime

    class Config:
        from_attributes = True


# ==========================================
# AUTH RESPONSE
# ==========================================

class AuthResponse(BaseModel):

    access_token: str

    token_type: str

# =========================================================
# AI TRIP PLANNER REQUEST
# =========================================================

class AITripRequest(BaseModel):

    starting_location: str

    travel_date: str

    people: int

    budget: float

    experience: str

    duration: int

    transport: str

    weather_preference: str

    footfall_preference: str


# =========================================================
# AI TRIP RESULT
# =========================================================

class AITripResponse(BaseModel):

    recommendations: list