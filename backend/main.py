# import os

# import shutil
# import uuid
# from pathlib import Path

# from datetime import datetime, timedelta

# from fastapi.staticfiles import StaticFiles

# from dotenv import load_dotenv

# from fastapi import (
#     FastAPI,
#     Depends,
#     HTTPException,
#     Header,
#     UploadFile,
#     File
# )




# from fastapi.middleware.cors import CORSMiddleware

# from sqlalchemy.orm import Session

# from jose import jwt, JWTError

# import bcrypt


# from database import engine, get_db, Base

# from models import (
#     Trip,
#     User,
#     Destination,
#     TravelCost,
#     FootfallData,
#     Hotel
# )

# from ai_engine import generate_recommendations

# from schemas import (
#     TripResponse,
#     UserSignup,
#     UserLogin,
#     UserResponse,
#     AuthResponse,
#     AITripRequest,
#     AITripResponse
# )

# from crud import (
#     get_trip,
#     get_all_trips,
#     get_user_by_email,
#     get_user_by_id,
#     create_user
# )



# # ==========================================
# # LOAD ENVIRONMENT VARIABLES
# # ==========================================

# load_dotenv()


# # ==========================================
# # CREATE DATABASE TABLES
# # ==========================================

# Base.metadata.create_all(bind=engine)


# # ==========================================
# # FASTAPI APP
# # ==========================================

# app = FastAPI(
#     title="BengalTrail API",
#     description="Backend API for BengalTrail tourism platform",
#     version="1.0.0"
# )


# # ==========================================
# # CORS
# # ==========================================

# app.add_middleware(
#     CORSMiddleware,

#     allow_origins=["*"],

#     allow_credentials=False,

#     allow_methods=["*"],

#     allow_headers=["*"],
# )


# # ==========================================
# # JWT CONFIGURATION
# # ==========================================

# SECRET_KEY = os.getenv("JWT_SECRET_KEY")

# ALGORITHM = "HS256"

# ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24


# if not SECRET_KEY:
#     raise ValueError(
#         "JWT_SECRET_KEY is not configured in .env"
#     )


# # ==========================================
# # PASSWORD HASHING
# # ==========================================

# def hash_password(password: str):

#     return bcrypt.hashpw(
#         password.encode("utf-8"),
#         bcrypt.gensalt()
#     ).decode("utf-8")


# def verify_password(
#     password: str,
#     hashed_password: str
# ):

#     return bcrypt.checkpw(
#         password.encode("utf-8"),
#         hashed_password.encode("utf-8")
#     )


# # ==========================================
# # CREATE JWT TOKEN
# # ==========================================

# def create_access_token(user_id: int):

#     expire = datetime.utcnow() + timedelta(
#         minutes=ACCESS_TOKEN_EXPIRE_MINUTES
#     )

#     payload = {
#         "sub": str(user_id),
#         "exp": expire
#     }

#     token = jwt.encode(
#         payload,
#         SECRET_KEY,
#         algorithm=ALGORITHM
#     )

#     return token


# # ==========================================
# # GET CURRENT LOGGED-IN USER
# # ==========================================

# def get_current_user(
#     authorization: str = Header(None),
#     db: Session = Depends(get_db)
# ):

#     # No Authorization header
#     if not authorization:

#         raise HTTPException(
#             status_code=401,
#             detail="Authentication required"
#         )


#     # Check Bearer format
#     if not authorization.startswith("Bearer "):

#         raise HTTPException(
#             status_code=401,
#             detail="Invalid authentication format"
#         )


#     # Extract token
#     token = authorization.split(" ")[1]


#     try:

#         payload = jwt.decode(
#             token,
#             SECRET_KEY,
#             algorithms=[ALGORITHM]
#         )

#         user_id = payload.get("sub")


#         if user_id is None:

#             raise HTTPException(
#                 status_code=401,
#                 detail="Invalid token"
#             )


#     except JWTError:

#         raise HTTPException(
#             status_code=401,
#             detail="Invalid or expired token"
#         )


#     # Find user
#     user = get_user_by_id(
#         db,
#         int(user_id)
#     )


#     if not user:

#         raise HTTPException(
#             status_code=401,
#             detail="User not found"
#         )


#     return user


# # ==================================================
# # HOME
# # ==================================================

# @app.get("/")
# def home():

#     return {
#         "message": "Welcome to BengalTrail API"
#     }


# # ==================================================
# # TRIPS
# # ==================================================

# @app.get(
#     "/api/trips",
#     response_model=list[TripResponse]
# )
# def get_trips(
#     db: Session = Depends(get_db)
# ):

#     trips = get_all_trips(db)

#     return trips


# # ==================================================
# # SINGLE TRIP
# # ==================================================

# @app.get(
#     "/api/trips/{trip_id}",
#     response_model=TripResponse
# )
# def get_trip_details(
#     trip_id: int,
#     db: Session = Depends(get_db)
# ):

#     trip = get_trip(
#         db,
#         trip_id
#     )


#     if not trip:

#         raise HTTPException(
#             status_code=404,
#             detail="Trip not found"
#         )


#     return trip

# # ==================================================
# # GET HOTELS FOR A TRIP
# # ==================================================

# @app.get("/api/trips/{trip_id}/hotels")
# def get_trip_hotels(
#     trip_id: int,
#     db: Session = Depends(get_db)
# ):

#     # Find the trip first
#     trip = (
#         db.query(Trip)
#         .filter(
#             Trip.id == trip_id
#         )
#         .first()
#     )


#     # Trip does not exist
#     if not trip:

#         raise HTTPException(
#             status_code=404,
#             detail="Trip not found"
#         )


#     # Get all hotels belonging to this trip
#     hotels = (
#         db.query(Hotel)
#         .filter(
#             Hotel.trip_id == trip_id
#         )
#         .all()
#     )


#     return hotels

# # # =========================================================
# # # AI TRIP PLANNER
# # # =========================================================

# # @app.post(
# #     "/api/ai/plan",
# #     response_model=AITripResponse
# # )
# # def ai_trip_planner(
# #     request: AITripRequest,
# #     db: Session = Depends(get_db)
# # ):

# #     try:

# #         visit_date = datetime.strptime(
# #             request.travel_date,
# #             "%Y-%m-%d"
# #         )

# #         recommendations = (
# #             generate_recommendations(

# #                 db=db,

# #                 experience=
# #                     request.experience,

# #                 budget=
# #                     request.budget,

# #                 people=
# #                     request.people,

# #                 duration=
# #                     request.duration,

# #                 transport=
# #                     request.transport,

# #                 visit_date=
# #                     visit_date,

# #                 footfall_preference=
# #                     request.footfall_preference
# #             )
# #         )

# #         return {
# #             "recommendations":
# #                 recommendations
# #         }

# #     except Exception as error:

# #         print(
# #             "AI planner error:",
# #             error
# #         )

# #         raise HTTPException(

# #             status_code=500,

# #             detail=(
# #                 "Unable to generate "
# #                 "AI recommendations"
# #             )
# #         )

# # =========================================================
# # AI TRIP PLANNER
# # =========================================================

# @app.post(
#     "/api/ai/plan",
#     response_model=AITripResponse
# )
# def ai_trip_planner(
#     request: AITripRequest,
#     db: Session = Depends(get_db)
# ):

#     try:

#         # =============================================
#         # CONVERT TRAVEL DATE
#         # =============================================

#         visit_date = datetime.strptime(
#             request.travel_date,
#             "%Y-%m-%d"
#         )


#         # =============================================
#         # GENERATE AI RECOMMENDATIONS
#         # =============================================

#         recommendations = (
#             generate_recommendations(

#                 db=db,

#                 # Starting location is IMPORTANT
#                 # for distance and travel cost
#                 starting_location=
#                     request.starting_location,

#                 experience=
#                     request.experience,

#                 budget=
#                     request.budget,

#                 people=
#                     request.people,

#                 duration=
#                     request.duration,

#                 transport=
#                     request.transport,

#                 visit_date=
#                     visit_date,

#                 weather_preference=
#                     request.weather_preference,

#                 footfall_preference=
#                     request.footfall_preference
#             )
#         )


#         # =============================================
#         # RETURN RESULTS
#         # =============================================

#         return {
#             "recommendations":
#                 recommendations
#         }


#     except Exception as error:

#         print(
#             "AI planner error:",
#             error
#         )


#         raise HTTPException(

#             status_code=500,

#             detail=(
#                 "Unable to generate "
#                 "AI recommendations: "
#                 f"{str(error)}"
#             )

#         )


# # ==================================================
# # SIGN UP
# # ==================================================

# @app.post(
#     "/api/signup",
#     response_model=AuthResponse
# )
# def signup(
#     user_data: UserSignup,
#     db: Session = Depends(get_db)
# ):

#     # ------------------------------------------
#     # Check if email already exists
#     # ------------------------------------------

#     existing_user = get_user_by_email(
#         db,
#         user_data.email
#     )


#     if existing_user:

#         raise HTTPException(
#             status_code=409,
#             detail="Email already registered"
#         )


#     # ------------------------------------------
#     # Validate password
#     # ------------------------------------------

#     if len(user_data.password) < 6:

#         raise HTTPException(
#             status_code=400,
#             detail="Password must be at least 6 characters"
#         )


#     # ------------------------------------------
#     # Hash password
#     # ------------------------------------------

#     password_hash = hash_password(
#         user_data.password
#     )


#     # ------------------------------------------
#     # Create user
#     # ------------------------------------------

#     user = create_user(
#         db=db,
#         full_name=user_data.full_name,
#         email=user_data.email,
#         password_hash=password_hash
#     )


#     # ------------------------------------------
#     # Create login token
#     # ------------------------------------------

#     token = create_access_token(
#         user.id
#     )


#     return {
#         "access_token": token,
#         "token_type": "bearer"
#     }


# # ==================================================
# # LOGIN
# # ==================================================

# @app.post(
#     "/api/login",
#     response_model=AuthResponse
# )
# def login(
#     user_data: UserLogin,
#     db: Session = Depends(get_db)
# ):

#     # ------------------------------------------
#     # Find user
#     # ------------------------------------------

#     user = get_user_by_email(
#         db,
#         user_data.email
#     )


#     if not user:

#         raise HTTPException(
#             status_code=401,
#             detail="Invalid email or password"
#         )


#     # ------------------------------------------
#     # Verify password
#     # ------------------------------------------

#     if not verify_password(
#         user_data.password,
#         user.password_hash
#     ):

#         raise HTTPException(
#             status_code=401,
#             detail="Invalid email or password"
#         )


#     # ------------------------------------------
#     # Create JWT
#     # ------------------------------------------

#     token = create_access_token(
#         user.id
#     )


#     return {
#         "access_token": token,
#         "token_type": "bearer"
#     }


# # ==================================================
# # CHECK AUTHENTICATION
# # ==================================================

# @app.get("/api/check-auth")
# def check_auth(
#     current_user: User = Depends(get_current_user)
# ):

#     return {

#         "logged_in": True,

#         "user": {

#             "id": current_user.id,

#             "full_name": current_user.full_name,

#             "email": current_user.email

#         }

#     }


# # ==================================================
# # GET PROFILE
# # ==================================================

# @app.get(
#     "/api/profile",
#     response_model=UserResponse
# )
# def get_profile(
#     current_user: User = Depends(get_current_user)
# ):

#     return current_user


# # ==================================================
# # LOGOUT
# # ==================================================

# @app.post("/api/logout")
# def logout():

#     return {
#         "success": True,
#         "message": "Logged out successfully"
#     }

# # ==========================================
# # UPLOAD DIRECTORY
# # ==========================================

# UPLOAD_DIR = Path("uploads")

# UPLOAD_DIR.mkdir(
#     parents=True,
#     exist_ok=True
# )


# # Serve uploaded images
# app.mount(
#     "/uploads",
#     StaticFiles(directory="uploads"),
#     name="uploads"
# )


# # Serve frontend static files from the same origin
# FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

# app.mount(
#     "/frontend",
#     StaticFiles(directory=FRONTEND_DIR),
#     name="frontend"
# )


# # ==================================================
# # UPLOAD PROFILE PHOTO
# # ==================================================

# @app.post("/api/profile/photo")
# async def upload_profile_photo(
#     file: UploadFile = File(...),
#     current_user: User = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):

#     # ==========================================
#     # ALLOWED FILE TYPES
#     # ==========================================

#     allowed_types = {
#         "image/jpeg": ".jpg",
#         "image/png": ".png",
#         "image/webp": ".webp"
#     }


#     if file.content_type not in allowed_types:

#         raise HTTPException(
#             status_code=400,
#             detail="Only JPG, PNG and WEBP images are allowed"
#         )


#     # ==========================================
#     # CHECK FILE SIZE
#     # ==========================================

#     contents = await file.read()


#     if len(contents) > 5 * 1024 * 1024:

#         raise HTTPException(
#             status_code=400,
#             detail="Image must be smaller than 5 MB"
#         )


#     # ==========================================
#     # CREATE UNIQUE FILE NAME
#     # ==========================================

#     extension = allowed_types[
#         file.content_type
#     ]

#     filename = (
#         f"user_{current_user.id}_"
#         f"{uuid.uuid4().hex}"
#         f"{extension}"
#     )


#     file_path = UPLOAD_DIR / filename


#     # ==========================================
#     # SAVE FILE
#     # ==========================================

#     with open(file_path, "wb") as buffer:

#         buffer.write(contents)


#     # ==========================================
#     # SAVE PATH IN DATABASE
#     # ==========================================

#     current_user.profile_image = (
#         f"/uploads/{filename}"
#     )

#     db.commit()

#     db.refresh(current_user)


#     return {

#         "success": True,

#         "message": "Profile photo uploaded successfully",

#         "profile_image":
#             current_user.profile_image

#     }

import os
import uuid
from pathlib import Path
from datetime import datetime, timedelta
from urllib.parse import quote_plus
from urllib.request import Request, urlopen
import json

from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    Header,
    UploadFile,
    File,
    Query,
)
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from jose import jwt, JWTError
import bcrypt

from database import engine, get_db, Base
from models import (
    Trip,
    User,
    Destination,
    TravelCost,
    FootfallData,
    Hotel,
)
from ai_engine import generate_recommendations
from schemas import (
    TripResponse,
    UserSignup,
    UserLogin,
    UserResponse,
    AuthResponse,
    AITripRequest,
    AITripResponse,
)
from crud import (
    get_trip,
    get_all_trips,
    get_user_by_email,
    get_user_by_id,
    create_user,
)

load_dotenv()

# =========================================================
# DATABASE
# =========================================================

Base.metadata.create_all(bind=engine)

# =========================================================
# FASTAPI
# =========================================================

app = FastAPI(
    title="BengalTrail API",
    description="Backend API for BengalTrail tourism platform",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================================
# JWT
# =========================================================

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

if not SECRET_KEY:
    raise ValueError(
        "JWT_SECRET_KEY is not configured in .env"
    )

# =========================================================
# PASSWORDS
# =========================================================

def hash_password(password: str):
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt(),
    ).decode("utf-8")


def verify_password(password: str, hashed_password: str):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8"),
    )


# =========================================================
# JWT TOKEN
# =========================================================

def create_access_token(user_id: int):
    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "exp": expire,
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


# =========================================================
# CURRENT USER
# =========================================================

def get_current_user(
    authorization: str = Header(None),
    db: Session = Depends(get_db),
):
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Authentication required",
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication format",
        )

    parts = authorization.split(" ", 1)

    if len(parts) != 2 or not parts[1]:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication format",
        )

    token = parts[1]

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token",
            )

        user_id = int(user_id)

    except (JWTError, ValueError, TypeError):
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
        )

    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found",
        )

    return user


# =========================================================
# HOME
# =========================================================

@app.get("/")
def home():
    return {
        "message": "Welcome to BengalTrail API"
    }


# =========================================================
# TRIPS
# =========================================================

@app.get(
    "/api/trips",
    response_model=list[TripResponse],
)
def get_trips(
    db: Session = Depends(get_db),
):
    return get_all_trips(db)


# =========================================================
# SINGLE TRIP
# =========================================================

@app.get(
    "/api/trips/{trip_id}",
    response_model=TripResponse,
)
def get_trip_details(
    trip_id: int,
    db: Session = Depends(get_db),
):
    trip = get_trip(db, trip_id)

    if not trip:
        raise HTTPException(
            status_code=404,
            detail="Trip not found",
        )

    return trip


# =========================================================
# HOTELS FOR A TRIP
# =========================================================

@app.get("/api/trips/{trip_id}/hotels")
def get_trip_hotels(
    trip_id: int,
    db: Session = Depends(get_db),
):
    trip = (
        db.query(Trip)
        .filter(Trip.id == trip_id)
        .first()
    )

    if not trip:
        raise HTTPException(
            status_code=404,
            detail="Trip not found",
        )

    hotels = (
        db.query(Hotel)
        .filter(Hotel.trip_id == trip_id)
        .all()
    )

    return hotels


# =========================================================
# LOCATION SEARCH / VERIFICATION
#
# This is the missing endpoint in your current main.py.
#
# Frontend:
# GET /api/location/search?q=New%20Town%20Kolkata
#
# The endpoint:
# 1. Searches real locations
# 2. Restricts results to India
# 3. Rejects nonsense such as "cffweferw"
# 4. Returns exact latitude/longitude
# 5. Lets the user select the exact locality
#
# =========================================================

@app.get("/api/location/search")
def search_location(
    q: str = Query(..., min_length=3, max_length=150),
):
    query = q.strip()

    if len(query) < 3:
        raise HTTPException(
            status_code=422,
            detail="Please enter at least 3 characters.",
        )

    # Nominatim is used only for prototype location
    # verification/geocoding.
    #
    # countrycodes=in ensures that arbitrary places
    # outside India are not returned.

    params = (
        "q=" + quote_plus(query)
        + "&format=jsonv2"
        + "&addressdetails=1"
        + "&limit=5"
        + "&countrycodes=in"
        + "&accept-language=en"
    )

    url = (
        "https://nominatim.openstreetmap.org/search?"
        + params
    )

    request = Request(
        url,
        headers={
            "User-Agent": (
                "BengalTrailPrototype/1.0 "
                "(travel-planner-local-development)"
            ),
        },
    )

    try:
        with urlopen(
            request,
            timeout=10,
        ) as response:
            raw_data = response.read().decode(
                "utf-8"
            )

        places = json.loads(raw_data)

    except Exception as error:
        print(
            "Location search error:",
            repr(error),
        )

        raise HTTPException(
            status_code=503,
            detail=(
                "Location verification service is "
                "temporarily unavailable. Please try again."
            ),
        )

    results = []

    # Broad result types are kept but marked so the
    # frontend can tell the user to prefer an exact
    # locality/area for large cities.

    broad_types = {
        "city",
        "town",
        "municipality",
        "county",
        "state",
        "region",
    }

    preferred_types = {
        "suburb",
        "neighbourhood",
        "village",
        "hamlet",
        "quarter",
        "residential",
        "locality",
        "station",
        "aerodrome",
    }

    for place in places:
        try:
            latitude = float(place["lat"])
            longitude = float(place["lon"])
        except (
            KeyError,
            TypeError,
            ValueError,
        ):
            continue

        address = place.get("address") or {}

        country_code = (
            address.get("country_code")
            or ""
        ).lower()

        if country_code != "in":
            continue

        place_type = (
            place.get("type")
            or ""
        ).lower()

        precision = (
            "exact"
            if place_type in preferred_types
            else "broad"
            if place_type in broad_types
            else "standard"
        )

        results.append({
            "display_name": place.get(
                "display_name",
                query,
            ),
            "latitude": latitude,
            "longitude": longitude,
            "type": place_type,
            "precision": precision,
            "city": (
                address.get("city")
                or address.get("town")
                or address.get("municipality")
                or address.get("village")
                or ""
            ),
            "state": (
                address.get("state")
                or ""
            ),
            "country": (
                address.get("country")
                or "India"
            ),
        })

    if not results:
        raise HTTPException(
            status_code=404,
            detail=(
                "No matching Indian location was found. "
                "Try a more specific place such as "
                "'Salt Lake Kolkata', 'New Town Kolkata', "
                "'NJP', 'Siliguri', or another locality."
            ),
        )

    # Exact localities first, broad city-level results later.
    results.sort(
        key=lambda item: (
            0 if item["precision"] == "exact" else
            1 if item["precision"] == "standard" else
            2
        )
    )

    return {
        "query": query,
        "results": results[:5],
    }


# =========================================================
# AI TRIP PLANNER
# =========================================================

@app.post(
    "/api/ai/plan",
    response_model=AITripResponse,
)
def ai_trip_planner(
    request: AITripRequest,
    db: Session = Depends(get_db),
):
    try:
        # -------------------------------------------------
        # Validate date
        # -------------------------------------------------

        try:
            visit_date = datetime.strptime(
                request.travel_date,
                "%Y-%m-%d",
            )
        except ValueError:
            raise HTTPException(
                status_code=422,
                detail=(
                    "Travel date must be in "
                    "YYYY-MM-DD format."
                ),
            )

        # -------------------------------------------------
        # Coordinates are mandatory.
        #
        # They come from /api/location/search after the
        # user selects a verified location.
        # -------------------------------------------------

        starting_latitude = float(
            request.starting_latitude
        )

        starting_longitude = float(
            request.starting_longitude
        )

        # India bounds
        if not (
            6.0
            <= starting_latitude
            <= 37.5
        ):
            raise HTTPException(
                status_code=422,
                detail="Invalid starting latitude.",
            )

        if not (
            68.0
            <= starting_longitude
            <= 98.0
        ):
            raise HTTPException(
                status_code=422,
                detail="Invalid starting longitude.",
            )

        # -------------------------------------------------
        # IMPORTANT:
        # Pass coordinates directly into ai_engine.
        #
        # ai_engine.py already supports this dictionary
        # format.
        # -------------------------------------------------

        starting_location = {
            "name": request.starting_location,
            "latitude": starting_latitude,
            "longitude": starting_longitude,
        }

        print(
            "\n========================================"
        )
        print("AI TRIP PLANNER REQUEST")
        print(
            "Starting:",
            request.starting_location,
        )
        print(
            "Latitude:",
            starting_latitude,
        )
        print(
            "Longitude:",
            starting_longitude,
        )
        print(
            "Date:",
            request.travel_date,
        )
        print(
            "People:",
            request.people,
        )
        print(
            "Budget:",
            request.budget,
        )
        print(
            "Experience:",
            request.experience,
        )
        print(
            "Duration:",
            request.duration,
        )
        print(
            "Transport:",
            request.transport,
        )
        print(
            "Weather:",
            request.weather_preference,
        )
        print(
            "Footfall:",
            request.footfall_preference,
        )
        print(
            "========================================\n"
        )

        # -------------------------------------------------
        # Generate recommendations
        # -------------------------------------------------

        recommendations = generate_recommendations(
            db=db,
            starting_location=starting_location,
            experience=request.experience,
            budget=request.budget,
            people=request.people,
            duration=request.duration,
            transport=request.transport,
            visit_date=visit_date,
            weather_preference=request.weather_preference,
            footfall_preference=request.footfall_preference,
        )

        if recommendations is None:
            recommendations = []

        print(
            "AI recommendations generated:",
            len(recommendations),
        )

        return {
            "recommendations": recommendations
        }

    except HTTPException:
        raise

    except ValueError as error:
        print(
            "\nAI PLANNER VALIDATION ERROR:",
            repr(error),
            "\n",
        )

        raise HTTPException(
            status_code=422,
            detail=str(error),
        )

    except Exception as error:
        # Keep the real error visible in the terminal.
        print(
            "\n========================================"
        )
        print("AI PLANNER ERROR")
        print(
            "TYPE:",
            type(error).__name__,
        )
        print(
            "ERROR:",
            repr(error),
        )
        print(
            "========================================\n"
        )

        raise HTTPException(
            status_code=500,
            detail=(
                "AI planner failed: "
                f"{str(error)}"
            ),
        )


# =========================================================
# SIGN UP
# =========================================================

@app.post(
    "/api/signup",
    response_model=AuthResponse,
)
def signup(
    user_data: UserSignup,
    db: Session = Depends(get_db),
):
    existing_user = get_user_by_email(
        db,
        user_data.email,
    )

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already registered",
        )

    if len(user_data.password) < 6:
        raise HTTPException(
            status_code=400,
            detail=(
                "Password must be at least "
                "6 characters"
            ),
        )

    password_hash = hash_password(
        user_data.password
    )

    user = create_user(
        db=db,
        full_name=user_data.full_name,
        email=user_data.email,
        password_hash=password_hash,
    )

    token = create_access_token(
        user.id
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }


# =========================================================
# LOGIN
# =========================================================

@app.post(
    "/api/login",
    response_model=AuthResponse,
)
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db),
):
    user = get_user_by_email(
        db,
        user_data.email,
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    if not verify_password(
        user_data.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    token = create_access_token(
        user.id
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }


# =========================================================
# CHECK AUTH
# =========================================================

@app.get("/api/check-auth")
def check_auth(
    current_user: User = Depends(
        get_current_user
    ),
):
    return {
        "logged_in": True,
        "user": {
            "id": current_user.id,
            "full_name": current_user.full_name,
            "email": current_user.email,
        },
    }


# =========================================================
# PROFILE
# =========================================================

@app.get(
    "/api/profile",
    response_model=UserResponse,
)
def get_profile(
    current_user: User = Depends(
        get_current_user
    ),
):
    return current_user


# =========================================================
# LOGOUT
# =========================================================

@app.post("/api/logout")
def logout():
    return {
        "success": True,
        "message": "Logged out successfully",
    }


# =========================================================
# UPLOADS
# =========================================================

UPLOAD_DIR = Path("uploads")

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

app.mount(
    "/uploads",
    StaticFiles(
        directory="uploads"
    ),
    name="uploads",
)


# =========================================================
# FRONTEND STATIC DIRECTORY
# =========================================================

FRONTEND_DIR = (
    Path(__file__).resolve().parent.parent
    / "frontend"
)

if FRONTEND_DIR.exists():
    app.mount(
        "/frontend",
        StaticFiles(
            directory=FRONTEND_DIR
        ),
        name="frontend",
    )

    ASSETS_DIR = FRONTEND_DIR / "assets"
    if ASSETS_DIR.exists():
        app.mount(
            "/assets",
            StaticFiles(
                directory=ASSETS_DIR
            ),
            name="assets",
        )


# =========================================================
# PROFILE PHOTO
# =========================================================

@app.post("/api/profile/photo")
async def upload_profile_photo(
    file: UploadFile = File(...),
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db),
):
    allowed_types = {
        "image/jpeg": ".jpg",
        "image/png": ".png",
        "image/webp": ".webp",
    }

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=(
                "Only JPG, PNG and WEBP "
                "images are allowed"
            ),
        )

    contents = await file.read()

    if len(contents) > 5 * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail=(
                "Image must be smaller "
                "than 5 MB"
            ),
        )

    extension = allowed_types[
        file.content_type
    ]

    filename = (
        f"user_{current_user.id}_"
        f"{uuid.uuid4().hex}"
        f"{extension}"
    )

    file_path = (
        UPLOAD_DIR / filename
    )

    with open(
        file_path,
        "wb",
    ) as buffer:
        buffer.write(contents)

    current_user.profile_image = (
        f"/uploads/{filename}"
    )

    db.commit()
    db.refresh(current_user)

    return {
        "success": True,
        "message": (
            "Profile photo uploaded successfully"
        ),
        "profile_image":
            current_user.profile_image,
    }