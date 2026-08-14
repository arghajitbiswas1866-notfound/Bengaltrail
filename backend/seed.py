# from database import SessionLocal, engine, Base
# from models import Trip , Hotel


# Base.metadata.create_all(bind=engine)


# db = SessionLocal()


# trips = [

#     Trip(
#         title="Hidden Gems Explorer",

#         category="North Bengal",

#         route="Chatakpur → Takdah → Lamahatta",

#         image="/images/north-bengal.jpg",

#         rating=4.5,

#         reviews=245,

#         price=500,

#         duration="5 Days / 4 Nights",

#         difficulty="Easy",

#         description=(
#             "Explore the hidden beauty of North Bengal through "
#             "peaceful mountains, tea gardens, forests and "
#             "lesser-known villages."
#         ),

#         tags="Nature,Photography,Guide",

#         recommended_for="Nature Lovers, Couples, Photographers",

#         ai_match=96
#     ),


#     Trip(
#         title="Tea Garden Trails",

#         category="Tea Gardens",

#         route="Kurseong → Mirik → Darjeeling",

#         image="/images/chatakpur.jpg",

#         rating=4.7,

#         reviews=182,

#         price=450,

#         duration="4 Days / 3 Nights",

#         difficulty="Easy",

#         description=(
#             "Experience beautiful tea gardens, mountain views "
#             "and peaceful trails across North Bengal."
#         ),

#         tags="Tea Gardens,Nature,Photography",

#         recommended_for="Nature Lovers, Photographers, Beauty",

#         ai_match=94
#     ),


#     Trip(
#         title="Wildlife Escape",

#         category="Wildlife",

#         route="Jaldapara → Buxa → Jayanti",

#         image="/images/jaldapara.jpg",

#         rating=4.8,

#         reviews=156,

#         price=650,

#         duration="5 Days / 4 Nights",

#         difficulty="Moderate",

#         description=(
#             "Discover the wildlife and forests of North Bengal "
#             "with guided nature experiences."
#         ),

#         tags="Wildlife,Nature,Adventure",

#         recommended_for="Wildlife Lovers, Families",

#         ai_match=91
#     )

# ]


# for trip in trips:

#     existing = (
#         db.query(Trip)
#         .filter(Trip.title == trip.title)
#         .first()
#     )

#     if not existing:

#         db.add(trip)


# db.commit()

# db.close()

# print("Trips inserted successfully.")

# new_trips = [

#     Trip(
#         title="Dooars Forest Escape",
#         category="Wildlife",
#         route="Lataguri → Jaldapara → Buxa",
#         image="assets/img4.jpeg",
#         rating=4.7,
#         reviews=140,
#         price=7200,
#         duration="4 Days / 3 Nights",
#         difficulty="Moderate",
#         description="Explore the forests, wildlife and rivers of Dooars.",
#         tags="Wildlife,Nature,Adventure",
#         recommended_for="Nature Lovers, Families",
#         ai_match=92
#     ),

#     Trip(
#         title="Kalimpong Mountain Escape",
#         category="Mountains",
#         route="Siliguri → Kalimpong → Lava",
#         image="assets/img5.jpeg",
#         rating=4.6,
#         reviews=118,
#         price=6800,
#         duration="4 Days / 3 Nights",
#         difficulty="Easy",
#         description="Enjoy peaceful mountain landscapes and beautiful Himalayan views.",
#         tags="Mountains,Photography,Nature",
#         recommended_for="Couples, Photographers",
#         ai_match=90
#     ),

#     Trip(
#         title="Digha Coastal Escape",
#         category="Beach",
#         route="Kolkata → Digha → Mandarmani",
#         image="assets/img6.jpeg",
#         rating=4.4,
#         reviews=210,
#         price=5200,
#         duration="3 Days / 2 Nights",
#         difficulty="Easy",
#         description="Relax beside the sea and explore the beautiful coastal side of Bengal.",
#         tags="Beach,Relaxation,Food",
#         recommended_for="Families,Couples",
#         ai_match=88
#     ),

#     Trip(
#         title="Sundarbans Adventure",
#         category="Wildlife",
#         route="Kolkata → Gosaba → Sundarbans",
#         image="assets/img7.jpeg",
#         rating=4.8,
#         reviews=175,
#         price=8500,
#         duration="4 Days / 3 Nights",
#         difficulty="Moderate",
#         description="Experience mangrove forests, rivers and unique wildlife in the Sundarbans.",
#         tags="Wildlife,Nature,Adventure",
#         recommended_for="Adventure Lovers,Wildlife Lovers",
#         ai_match=95
#     )

# ]

# db.add_all(new_trips)
# db.commit()
# db.close()

# Hotels =[
#     Hotel(
#         trip_id=4,
#         name="Dooars Retreat",
#         location="Lataguri",
#         image="assets/hotel1.jpeg",
#         rating=4.5,
#         price_per_night=2500,
#         room_type="Deluxe Room",
#         facilities="WiFi,Breakfast,Parking,AC",
#         available_rooms=5,
#         description="Comfortable stay surrounded by the forests of Dooars."
#     ),
#     Hotel(
#         trip_id=4,
#         name="Forest View Resort",
#         location="Lataguri",
#         image="assets/hotel2.jpeg",
#         rating=4.7,
#         price_per_night=3200,
#         room_type="Premium Room",
#         facilities="WiFi,Pool,Breakfast,Parking",
#         available_rooms=3,
#         description="A peaceful resort with beautiful forest views."
#     )
# ]

# db.add_all(Hotels)
# db.commit()
# db.close()

from database import SessionLocal, engine, Base
from models import Trip, Hotel


# =========================================================
# CREATE TABLES
# =========================================================

Base.metadata.create_all(bind=engine)


# =========================================================
# OPEN DATABASE SESSION
# =========================================================

db = SessionLocal()


try:

    # =====================================================
    # ORIGINAL TRIPS
    # =====================================================

    trips = [

        Trip(
            title="Hidden Gems Explorer",
            category="North Bengal",
            route="Chatakpur → Takdah → Lamahatta",
            image="/images/north-bengal.jpg",
            rating=4.5,
            reviews=245,
            price=500,
            duration="5 Days / 4 Nights",
            difficulty="Easy",
            description=(
                "Explore the hidden beauty of North Bengal through "
                "peaceful mountains, tea gardens, forests and "
                "lesser-known villages."
            ),
            tags="Nature,Photography,Guide",
            recommended_for="Nature Lovers, Couples, Photographers",
            ai_match=96
        ),

        Trip(
            title="Tea Garden Trails",
            category="Tea Gardens",
            route="Kurseong → Mirik → Darjeeling",
            image="/images/chatakpur.jpg",
            rating=4.7,
            reviews=182,
            price=450,
            duration="4 Days / 3 Nights",
            difficulty="Easy",
            description=(
                "Experience beautiful tea gardens, mountain views "
                "and peaceful trails across North Bengal."
            ),
            tags="Tea Gardens,Nature,Photography",
            recommended_for="Nature Lovers, Photographers, Beauty",
            ai_match=94
        ),

        Trip(
            title="Wildlife Escape",
            category="Wildlife",
            route="Jaldapara → Buxa → Jayanti",
            image="/images/jaldapara.jpg",
            rating=4.8,
            reviews=156,
            price=650,
            duration="5 Days / 4 Nights",
            difficulty="Moderate",
            description=(
                "Discover the wildlife and forests of North Bengal "
                "with guided nature experiences."
            ),
            tags="Wildlife,Nature,Adventure",
            recommended_for="Wildlife Lovers, Families",
            ai_match=91
        )
    ]


    # =====================================================
    # INSERT ORIGINAL TRIPS
    # =====================================================

    for trip in trips:

        existing = (
            db.query(Trip)
            .filter(
                Trip.title == trip.title
            )
            .first()
        )

        if not existing:
            db.add(trip)


    db.commit()


    # =====================================================
    # ADDITIONAL TRIPS
    # =====================================================

    new_trips = [

        Trip(
            title="Dooars Forest Escape",
            category="Wildlife",
            route="Lataguri → Jaldapara → Buxa",
            image="assets/img4.jpeg",
            rating=4.7,
            reviews=140,
            price=7200,
            duration="4 Days / 3 Nights",
            difficulty="Moderate",
            description=(
                "Explore the forests, wildlife and rivers of Dooars."
            ),
            tags="Wildlife,Nature,Adventure",
            recommended_for="Nature Lovers, Families",
            ai_match=92
        ),

        Trip(
            title="Kalimpong Mountain Escape",
            category="Mountains",
            route="Siliguri → Kalimpong → Lava",
            image="assets/img5.jpeg",
            rating=4.6,
            reviews=118,
            price=6800,
            duration="4 Days / 3 Nights",
            difficulty="Easy",
            description=(
                "Enjoy peaceful mountain landscapes and "
                "beautiful Himalayan views."
            ),
            tags="Mountains,Photography,Nature",
            recommended_for="Couples, Photographers",
            ai_match=90
        ),

        Trip(
            title="Digha Coastal Escape",
            category="Beach",
            route="Kolkata → Digha → Mandarmani",
            image="assets/img6.jpeg",
            rating=4.4,
            reviews=210,
            price=5200,
            duration="3 Days / 2 Nights",
            difficulty="Easy",
            description=(
                "Relax beside the sea and explore the beautiful "
                "coastal side of Bengal."
            ),
            tags="Beach,Relaxation,Food",
            recommended_for="Families,Couples",
            ai_match=88
        ),

        Trip(
            title="Sundarbans Adventure",
            category="Wildlife",
            route="Kolkata → Gosaba → Sundarbans",
            image="assets/img7.jpeg",
            rating=4.8,
            reviews=175,
            price=8500,
            duration="4 Days / 3 Nights",
            difficulty="Moderate",
            description=(
                "Experience mangrove forests, rivers and unique "
                "wildlife in the Sundarbans."
            ),
            tags="Wildlife,Nature,Adventure",
            recommended_for="Adventure Lovers,Wildlife Lovers",
            ai_match=95
        )
    ]


    # =====================================================
    # INSERT ADDITIONAL TRIPS WITHOUT DUPLICATES
    # =====================================================

    for trip in new_trips:

        existing = (
            db.query(Trip)
            .filter(
                Trip.title == trip.title
            )
            .first()
        )

        if not existing:
            db.add(trip)


    db.commit()


    # =====================================================
    # FIND DOOARS TRIP
    # =====================================================

    dooars = (
        db.query(Trip)
        .filter(
            Trip.title == "Dooars Forest Escape"
        )
        .first()
    )


    if not dooars:

        raise Exception(
            "Dooars Forest Escape was not found."
        )


    print(
        "Dooars trip ID:",
        dooars.id
    )


    # =====================================================
    # DOOARS HOTELS
    # =====================================================

    dooars_hotels = [

        Hotel(
            trip_id=dooars.id,
            name="Dooars Retreat",
            location="Lataguri",
            image="assets/hotel1.jpeg",
            rating=4.5,
            price_per_night=2500,
            room_type="Deluxe Room",
            facilities="WiFi,Breakfast,Parking,AC",
            available_rooms=5,
            description=(
                "Comfortable stay surrounded by "
                "the forests of Dooars."
            )
        ),

        Hotel(
            trip_id=dooars.id,
            name="Forest View Resort",
            location="Lataguri",
            image="assets/hotel2.jpeg",
            rating=4.7,
            price_per_night=3200,
            room_type="Premium Room",
            facilities="WiFi,Pool,Breakfast,Parking",
            available_rooms=3,
            description=(
                "A peaceful resort with beautiful "
                "forest views."
            )
        )

    ]


    # =====================================================
    # INSERT HOTELS WITHOUT DUPLICATES
    # =====================================================

    for hotel in dooars_hotels:

        existing = (
            db.query(Hotel)
            .filter(
                Hotel.name == hotel.name,
                Hotel.trip_id == hotel.trip_id
            )
            .first()
        )


        if not existing:
            db.add(hotel)


    db.commit()


    print(
        "Trips and hotels inserted successfully."
    )


# =========================================================
# ERROR HANDLING
# =========================================================

except Exception as error:

    db.rollback()

    print(
        "Seed failed:",
        error
    )

    raise


# =========================================================
# CLOSE DATABASE
# =========================================================

finally:

    db.close()