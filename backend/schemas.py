# from pydantic import BaseModel, EmailStr
# from typing import Optional
# from datetime import datetime


# # ==========================================
# # TRIP RESPONSE
# # ==========================================

# class TripResponse(BaseModel):

#     id: int

#     title: str

#     category: Optional[str] = None

#     route: Optional[str] = None

#     image: Optional[str] = None

#     rating: float

#     reviews: int

#     price: Optional[float] = None

#     duration: Optional[str] = None

#     difficulty: Optional[str] = None

#     description: Optional[str] = None

#     tags: Optional[str] = None

#     recommended_for: Optional[str] = None

#     ai_match: int

#     class Config:

#         from_attributes = True


# # ==========================================
# # SIGN UP
# # ==========================================

# class UserSignup(BaseModel):

#     full_name: str

#     email: EmailStr

#     password: str


# # ==========================================
# # LOGIN
# # ==========================================

# class UserLogin(BaseModel):

#     email: EmailStr

#     password: str


# # ==========================================
# # USER RESPONSE
# # ==========================================

# class UserResponse(BaseModel):

#     id: int

#     full_name: str

#     email: str

#     profile_image: str | None = None

#     created_at: datetime

#     class Config:
#         from_attributes = True


# # ==========================================
# # AUTH RESPONSE
# # ==========================================

# class AuthResponse(BaseModel):

#     access_token: str

#     token_type: str

# # =========================================================
# # AI TRIP PLANNER REQUEST
# # =========================================================

# class AITripRequest(BaseModel):

#     starting_location: str

#     travel_date: str

#     people: int

#     budget: float

#     experience: str

#     duration: int

#     transport: str

#     weather_preference: str

#     footfall_preference: str


# # =========================================================
# # AI TRIP RESULT
# # =========================================================

# class AITripResponse(BaseModel):

#     recommendations: list

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


# =========================================================
# TRIP RESPONSE
# =========================================================

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


# =========================================================
# SIGN UP
# =========================================================

class UserSignup(BaseModel):

    full_name: str

    email: EmailStr

    password: str


# =========================================================
# LOGIN
# =========================================================

class UserLogin(BaseModel):

    email: EmailStr

    password: str


# =========================================================
# USER RESPONSE
# =========================================================

class UserResponse(BaseModel):

    id: int

    full_name: str

    email: str

    profile_image: Optional[str] = None

    created_at: datetime

    class Config:
        from_attributes = True


# =========================================================
# AUTH RESPONSE
# =========================================================

class AuthResponse(BaseModel):

    access_token: str

    token_type: str


# =========================================================
# AI TRIP PLANNER REQUEST
# =========================================================
#
# IMPORTANT:
#
# starting_location
#     = human-readable selected location
#
# starting_latitude
# starting_longitude
#     = exact coordinates returned by the
#       location verification system
#
# The AI engine should use the coordinates
# for distance and travel-cost calculation.
#
# =========================================================

class AITripRequest(BaseModel):

    # -----------------------------------------------------
    # STARTING LOCATION
    # -----------------------------------------------------

    starting_location: str = Field(

        ...,

        min_length=2,

        description=(
            "Verified starting location selected "
            "by the user."
        )
    )


    # -----------------------------------------------------
    # STARTING LOCATION COORDINATES
    # -----------------------------------------------------

    starting_latitude: float = Field(

        ...,

        ge=6.0,

        le=37.5,

        description=(
            "Latitude of the verified starting "
            "location in India."
        )
    )


    starting_longitude: float = Field(

        ...,

        ge=68.0,

        le=98.0,

        description=(
            "Longitude of the verified starting "
            "location in India."
        )
    )


    # -----------------------------------------------------
    # TRAVEL DATE
    # -----------------------------------------------------

    travel_date: str = Field(

        ...,

        min_length=8,

        description=(
            "Travel date in YYYY-MM-DD format."
        )
    )


    # -----------------------------------------------------
    # NUMBER OF PEOPLE
    # -----------------------------------------------------

    people: int = Field(

        ...,

        ge=1,

        le=100,

        description=(
            "Number of people travelling."
        )
    )


    # -----------------------------------------------------
    # TOTAL BUDGET
    # -----------------------------------------------------

    budget: float = Field(

        ...,

        gt=0,

        description=(
            "Maximum total trip budget in INR."
        )
    )


    # -----------------------------------------------------
    # EXPERIENCE
    # -----------------------------------------------------

    experience: str = Field(

        ...,

        min_length=1,

        description=(
            "Preferred travel experience."
        )
    )


    # -----------------------------------------------------
    # TRIP DURATION
    # -----------------------------------------------------

    duration: int = Field(

        ...,

        ge=1,

        le=60,

        description=(
            "Trip duration in days."
        )
    )


    # -----------------------------------------------------
    # TRANSPORT
    # -----------------------------------------------------

    transport: str = Field(

        ...,

        min_length=1,

        description=(
            "Preferred transport type."
        )
    )


    # -----------------------------------------------------
    # WEATHER PREFERENCE
    # -----------------------------------------------------

    weather_preference: str = Field(

        ...,

        min_length=1,

        description=(
            "Preferred weather condition."
        )
    )


    # -----------------------------------------------------
    # FOOTFALL PREFERENCE
    # -----------------------------------------------------

    footfall_preference: str = Field(

        ...,

        min_length=1,

        description=(
            "Preferred destination crowd level."
        )
    )


# =========================================================
# AI TRIP RESULT
# =========================================================

class AITripResponse(BaseModel):

    recommendations: list