from database import SessionLocal, engine, Base

from models import (
    Destination,
    TravelCost,
    FootfallData
)

from datetime import datetime


# =========================================================
# CREATE TABLES
# =========================================================

Base.metadata.create_all(bind=engine)

db = SessionLocal()


# =========================================================
# DESTINATION DATA
# =========================================================

destinations = [

    # -----------------------------------------------------
    # DARJEELING
    # -----------------------------------------------------

    Destination(
        name="Darjeeling",
        district="Darjeeling",
        category="Mountain, Nature, Tea",

        description=(
            "A famous Himalayan destination known for "
            "mountain views, tea gardens and peaceful landscapes."
        ),

        best_for="Nature,Photography,Culture,Food",

        tags="mountain,nature,tea,culture,photography",

        average_stay=3,

        base_cost_per_person=1500,

        hotel_cost_per_night=1800,

        food_cost_per_day=700,

        transport_cost=500,

        rating=4.7,

        image="assets/img1.jpeg",

        latitude=27.0410,
        longitude=88.2663
    ),


    # -----------------------------------------------------
    # KALIMPONG
    # -----------------------------------------------------

    Destination(
        name="Kalimpong",
        district="Kalimpong",
        category="Mountain, Culture, Nature",

        description=(
            "A peaceful hill destination with monasteries, "
            "valleys, viewpoints and local culture."
        ),

        best_for="Nature,Culture,Photography",

        tags="mountain,nature,culture,monastery",

        average_stay=2,

        base_cost_per_person=1200,

        hotel_cost_per_night=1400,

        food_cost_per_day=600,

        transport_cost=450,

        rating=4.5,

        image="assets/img2.jpeg",

        latitude=27.0667,
        longitude=88.4667
    ),


    # -----------------------------------------------------
    # JALDAPARA
    # -----------------------------------------------------

    Destination(
        name="Jaldapara",
        district="Alipurduar",
        category="Wildlife, Adventure, Nature",

        description=(
            "A wildlife destination famous for forests, "
            "elephant safaris and natural landscapes."
        ),

        best_for="Wildlife,Adventure,Nature",

        tags="wildlife,forest,adventure,nature,safari",

        average_stay=2,

        base_cost_per_person=1800,

        hotel_cost_per_night=1600,

        food_cost_per_day=650,

        transport_cost=700,

        rating=4.6,

        image="assets/img3.jpeg",

        latitude=26.6944,
        longitude=89.2722
    ),


    # -----------------------------------------------------
    # BUXA
    # -----------------------------------------------------

    Destination(
        name="Buxa",
        district="Alipurduar",
        category="Wildlife, Adventure, Nature",

        description=(
            "A forest and mountain destination suitable "
            "for trekking, wildlife and adventure."
        ),

        best_for="Adventure,Wildlife,Nature",

        tags="forest,trekking,wildlife,adventure",

        average_stay=2,

        base_cost_per_person=1400,

        hotel_cost_per_night=1200,

        food_cost_per_day=600,

        transport_cost=650,

        rating=4.4,

        image="assets/img3.jpeg",

        latitude=26.7040,
        longitude=89.5527
    ),


    # -----------------------------------------------------
    # MIRIK
    # -----------------------------------------------------

    Destination(
        name="Mirik",
        district="Darjeeling",
        category="Lake, Nature, Tea",

        description=(
            "A peaceful destination surrounded by tea gardens, "
            "hills and a beautiful lake."
        ),

        best_for="Nature,Photography,Relaxation,Food",

        tags="lake,tea,nature,photography,relaxation",

        average_stay=2,

        base_cost_per_person=1000,

        hotel_cost_per_night=1200,

        food_cost_per_day=550,

        transport_cost=350,

        rating=4.3,

        image="assets/img2.jpeg",

        latitude=26.8894,
        longitude=88.1803
    ),


    # -----------------------------------------------------
    # CHATAKPUR
    # -----------------------------------------------------

    Destination(
        name="Chatakpur",
        district="Darjeeling",
        category="Hidden Gem, Nature, Photography",

        description=(
            "A quiet forest village offering mountain views "
            "and a peaceful escape from crowded tourist spots."
        ),

        best_for="Nature,Photography,Relaxation",

        tags="hidden-gem,forest,nature,mountain,photography",

        average_stay=2,

        base_cost_per_person=900,

        hotel_cost_per_night=1000,

        food_cost_per_day=500,

        transport_cost=400,

        rating=4.6,

        image="assets/img1.jpeg",

        latitude=26.9300,
        longitude=88.3650
    )

]


# =========================================================
# INSERT DESTINATIONS
# =========================================================

for destination in destinations:

    existing = (
        db.query(Destination)
        .filter(
            Destination.name == destination.name
        )
        .first()
    )

    if not existing:

        db.add(destination)


# =========================================================
# TRANSPORT DATA
# =========================================================

transport_data = [

    # -----------------------------------------------------
    # DARJEELING
    # -----------------------------------------------------

    TravelCost(
        destination="Darjeeling",
        transport_type="Bus",
        estimated_cost=250,
        duration_hours=3.5,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Darjeeling",
        transport_type="Shared Car",
        estimated_cost=400,
        duration_hours=3,
        comfort_level="High"
    ),

    TravelCost(
        destination="Darjeeling",
        transport_type="Train",
        estimated_cost=200,
        duration_hours=4,
        comfort_level="Medium"
    ),


    # -----------------------------------------------------
    # KALIMPONG
    # -----------------------------------------------------

    TravelCost(
        destination="Kalimpong",
        transport_type="Bus",
        estimated_cost=220,
        duration_hours=3,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Kalimpong",
        transport_type="Shared Car",
        estimated_cost=350,
        duration_hours=2.5,
        comfort_level="High"
    ),


    # -----------------------------------------------------
    # JALDAPARA
    # -----------------------------------------------------

    TravelCost(
        destination="Jaldapara",
        transport_type="Bus",
        estimated_cost=350,
        duration_hours=4,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Jaldapara",
        transport_type="Train",
        estimated_cost=250,
        duration_hours=3.5,
        comfort_level="Medium"
    ),


    # -----------------------------------------------------
    # BUXA
    # -----------------------------------------------------

    TravelCost(
        destination="Buxa",
        transport_type="Bus",
        estimated_cost=300,
        duration_hours=4,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Buxa",
        transport_type="Shared Car",
        estimated_cost=450,
        duration_hours=3.5,
        comfort_level="High"
    ),


    # -----------------------------------------------------
    # MIRIK
    # -----------------------------------------------------

    TravelCost(
        destination="Mirik",
        transport_type="Shared Car",
        estimated_cost=300,
        duration_hours=2.5,
        comfort_level="High"
    ),

    TravelCost(
        destination="Mirik",
        transport_type="Bus",
        estimated_cost=200,
        duration_hours=3,
        comfort_level="Medium"
    ),


    # -----------------------------------------------------
    # CHATAKPUR
    # -----------------------------------------------------

    TravelCost(
        destination="Chatakpur",
        transport_type="Shared Car",
        estimated_cost=400,
        duration_hours=3,
        comfort_level="High"
    ),

    TravelCost(
        destination="Chatakpur",
        transport_type="Bus",
        estimated_cost=250,
        duration_hours=4,
        comfort_level="Medium"
    )

]


# =========================================================
# INSERT TRANSPORT DATA
# =========================================================

for transport in transport_data:

    existing = (
        db.query(TravelCost)
        .filter(
            TravelCost.destination ==
            transport.destination
        )
        .filter(
            TravelCost.transport_type ==
            transport.transport_type
        )
        .first()
    )

    if not existing:

        db.add(transport)


# =========================================================
# FOOTFALL PROTOTYPE DATA
# =========================================================

destinations_names = [

    "Darjeeling",
    "Kalimpong",
    "Jaldapara",
    "Buxa",
    "Mirik",
    "Chatakpur"

]


# =========================================================
# GENERATE FOOTFALL DATA
# =========================================================

for destination_name in destinations_names:

    for day in range(1, 31):

        crowd_score = (
            30 +
            ((day * 7) % 60)
        )


        if crowd_score < 40:

            crowd_level = "Low"

        elif crowd_score < 70:

            crowd_level = "Medium"

        else:

            crowd_level = "High"


        existing = (

            db.query(FootfallData)

            .filter(
                FootfallData.destination ==
                destination_name
            )

            .filter(
                FootfallData.visit_date ==
                datetime(2026, 8, day)
            )

            .first()

        )


        if not existing:

            db.add(

                FootfallData(

                    destination=
                        destination_name,

                    visit_date=
                        datetime(2026, 8, day),

                    crowd_level=
                        crowd_level,

                    crowd_score=
                        crowd_score,

                    estimated_visitors=
                        crowd_score * 50

                )

            )


# =========================================================
# SAVE DATABASE
# =========================================================

db.commit()

db.close()


print(
    "AI prototype data inserted successfully."
)