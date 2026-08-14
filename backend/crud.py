from sqlalchemy.orm import Session

from models import Trip, User


# ==========================================
# TRIP FUNCTIONS
# ==========================================

def get_trip(db: Session, trip_id: int):

    return (
        db.query(Trip)
        .filter(Trip.id == trip_id)
        .first()
    )


def get_all_trips(db: Session):

    return (
        db.query(Trip)
        .order_by(Trip.id)
        .all()
    )


# ==========================================
# USER FUNCTIONS
# ==========================================

def get_user_by_email(
    db: Session,
    email: str
):

    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def get_user_by_id(
    db: Session,
    user_id: int
):

    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


def create_user(
    db: Session,
    full_name: str,
    email: str,
    password_hash: str
):

    user = User(
        full_name=full_name,
        email=email,
        password_hash=password_hash
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user

