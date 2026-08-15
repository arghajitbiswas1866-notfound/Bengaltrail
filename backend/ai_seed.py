# from database import SessionLocal, engine, Base

# from models import (
#     Destination,
#     TravelCost,
#     FootfallData
# )

# from datetime import datetime


# # =========================================================
# # CREATE TABLES
# # =========================================================

# Base.metadata.create_all(bind=engine)

# db = SessionLocal()


# # =========================================================
# # DESTINATION DATA
# # =========================================================

# destinations = [

#     # -----------------------------------------------------
#     # DARJEELING
#     # -----------------------------------------------------

#     Destination(
#         name="Darjeeling",
#         district="Darjeeling",
#         category="Mountain, Nature, Tea",

#         description=(
#             "A famous Himalayan destination known for "
#             "mountain views, tea gardens and peaceful landscapes."
#         ),

#         best_for="Nature,Photography,Culture,Food",

#         tags="mountain,nature,tea,culture,photography",

#         average_stay=3,

#         base_cost_per_person=1500,

#         hotel_cost_per_night=1800,

#         food_cost_per_day=700,

#         transport_cost=500,

#         rating=4.7,

#         image="assets/img1.jpeg",

#         latitude=27.0410,
#         longitude=88.2663
#     ),


#     # -----------------------------------------------------
#     # KALIMPONG
#     # -----------------------------------------------------

#     Destination(
#         name="Kalimpong",
#         district="Kalimpong",
#         category="Mountain, Culture, Nature",

#         description=(
#             "A peaceful hill destination with monasteries, "
#             "valleys, viewpoints and local culture."
#         ),

#         best_for="Nature,Culture,Photography",

#         tags="mountain,nature,culture,monastery",

#         average_stay=2,

#         base_cost_per_person=1200,

#         hotel_cost_per_night=1400,

#         food_cost_per_day=600,

#         transport_cost=450,

#         rating=4.5,

#         image="assets/img2.jpeg",

#         latitude=27.0667,
#         longitude=88.4667
#     ),


#     # -----------------------------------------------------
#     # JALDAPARA
#     # -----------------------------------------------------

#     Destination(
#         name="Jaldapara",
#         district="Alipurduar",
#         category="Wildlife, Adventure, Nature",

#         description=(
#             "A wildlife destination famous for forests, "
#             "elephant safaris and natural landscapes."
#         ),

#         best_for="Wildlife,Adventure,Nature",

#         tags="wildlife,forest,adventure,nature,safari",

#         average_stay=2,

#         base_cost_per_person=1800,

#         hotel_cost_per_night=1600,

#         food_cost_per_day=650,

#         transport_cost=700,

#         rating=4.6,

#         image="assets/img3.jpeg",

#         latitude=26.6944,
#         longitude=89.2722
#     ),


#     # -----------------------------------------------------
#     # BUXA
#     # -----------------------------------------------------

#     Destination(
#         name="Buxa",
#         district="Alipurduar",
#         category="Wildlife, Adventure, Nature",

#         description=(
#             "A forest and mountain destination suitable "
#             "for trekking, wildlife and adventure."
#         ),

#         best_for="Adventure,Wildlife,Nature",

#         tags="forest,trekking,wildlife,adventure",

#         average_stay=2,

#         base_cost_per_person=1400,

#         hotel_cost_per_night=1200,

#         food_cost_per_day=600,

#         transport_cost=650,

#         rating=4.4,

#         image="assets/img3.jpeg",

#         latitude=26.7040,
#         longitude=89.5527
#     ),


#     # -----------------------------------------------------
#     # MIRIK
#     # -----------------------------------------------------

#     Destination(
#         name="Mirik",
#         district="Darjeeling",
#         category="Lake, Nature, Tea",

#         description=(
#             "A peaceful destination surrounded by tea gardens, "
#             "hills and a beautiful lake."
#         ),

#         best_for="Nature,Photography,Relaxation,Food",

#         tags="lake,tea,nature,photography,relaxation",

#         average_stay=2,

#         base_cost_per_person=1000,

#         hotel_cost_per_night=1200,

#         food_cost_per_day=550,

#         transport_cost=350,

#         rating=4.3,

#         image="assets/img2.jpeg",

#         latitude=26.8894,
#         longitude=88.1803
#     ),


#     # -----------------------------------------------------
#     # CHATAKPUR
#     # -----------------------------------------------------

#     Destination(
#         name="Chatakpur",
#         district="Darjeeling",
#         category="Hidden Gem, Nature, Photography",

#         description=(
#             "A quiet forest village offering mountain views "
#             "and a peaceful escape from crowded tourist spots."
#         ),

#         best_for="Nature,Photography,Relaxation",

#         tags="hidden-gem,forest,nature,mountain,photography",

#         average_stay=2,

#         base_cost_per_person=900,

#         hotel_cost_per_night=1000,

#         food_cost_per_day=500,

#         transport_cost=400,

#         rating=4.6,

#         image="assets/img1.jpeg",

#         latitude=26.9300,
#         longitude=88.3650
#     )

# ]


# # =========================================================
# # INSERT DESTINATIONS
# # =========================================================

# for destination in destinations:

#     existing = (
#         db.query(Destination)
#         .filter(
#             Destination.name == destination.name
#         )
#         .first()
#     )

#     if not existing:

#         db.add(destination)


# # =========================================================
# # TRANSPORT DATA
# # =========================================================

# transport_data = [

#     # -----------------------------------------------------
#     # DARJEELING
#     # -----------------------------------------------------

#     TravelCost(
#         destination="Darjeeling",
#         transport_type="Bus",
#         estimated_cost=250,
#         duration_hours=3.5,
#         comfort_level="Medium"
#     ),

#     TravelCost(
#         destination="Darjeeling",
#         transport_type="Shared Car",
#         estimated_cost=400,
#         duration_hours=3,
#         comfort_level="High"
#     ),

#     TravelCost(
#         destination="Darjeeling",
#         transport_type="Train",
#         estimated_cost=200,
#         duration_hours=4,
#         comfort_level="Medium"
#     ),


#     # -----------------------------------------------------
#     # KALIMPONG
#     # -----------------------------------------------------

#     TravelCost(
#         destination="Kalimpong",
#         transport_type="Bus",
#         estimated_cost=220,
#         duration_hours=3,
#         comfort_level="Medium"
#     ),

#     TravelCost(
#         destination="Kalimpong",
#         transport_type="Shared Car",
#         estimated_cost=350,
#         duration_hours=2.5,
#         comfort_level="High"
#     ),


#     # -----------------------------------------------------
#     # JALDAPARA
#     # -----------------------------------------------------

#     TravelCost(
#         destination="Jaldapara",
#         transport_type="Bus",
#         estimated_cost=350,
#         duration_hours=4,
#         comfort_level="Medium"
#     ),

#     TravelCost(
#         destination="Jaldapara",
#         transport_type="Train",
#         estimated_cost=250,
#         duration_hours=3.5,
#         comfort_level="Medium"
#     ),


#     # -----------------------------------------------------
#     # BUXA
#     # -----------------------------------------------------

#     TravelCost(
#         destination="Buxa",
#         transport_type="Bus",
#         estimated_cost=300,
#         duration_hours=4,
#         comfort_level="Medium"
#     ),

#     TravelCost(
#         destination="Buxa",
#         transport_type="Shared Car",
#         estimated_cost=450,
#         duration_hours=3.5,
#         comfort_level="High"
#     ),


#     # -----------------------------------------------------
#     # MIRIK
#     # -----------------------------------------------------

#     TravelCost(
#         destination="Mirik",
#         transport_type="Shared Car",
#         estimated_cost=300,
#         duration_hours=2.5,
#         comfort_level="High"
#     ),

#     TravelCost(
#         destination="Mirik",
#         transport_type="Bus",
#         estimated_cost=200,
#         duration_hours=3,
#         comfort_level="Medium"
#     ),


#     # -----------------------------------------------------
#     # CHATAKPUR
#     # -----------------------------------------------------

#     TravelCost(
#         destination="Chatakpur",
#         transport_type="Shared Car",
#         estimated_cost=400,
#         duration_hours=3,
#         comfort_level="High"
#     ),

#     TravelCost(
#         destination="Chatakpur",
#         transport_type="Bus",
#         estimated_cost=250,
#         duration_hours=4,
#         comfort_level="Medium"
#     )

# ]


# # =========================================================
# # INSERT TRANSPORT DATA
# # =========================================================

# for transport in transport_data:

#     existing = (
#         db.query(TravelCost)
#         .filter(
#             TravelCost.destination ==
#             transport.destination
#         )
#         .filter(
#             TravelCost.transport_type ==
#             transport.transport_type
#         )
#         .first()
#     )

#     if not existing:

#         db.add(transport)


# # =========================================================
# # FOOTFALL PROTOTYPE DATA
# # =========================================================

# destinations_names = [

#     "Darjeeling",
#     "Kalimpong",
#     "Jaldapara",
#     "Buxa",
#     "Mirik",
#     "Chatakpur"

# ]


# # =========================================================
# # GENERATE FOOTFALL DATA
# # =========================================================

# for destination_name in destinations_names:

#     for day in range(1, 31):

#         crowd_score = (
#             30 +
#             ((day * 7) % 60)
#         )


#         if crowd_score < 40:

#             crowd_level = "Low"

#         elif crowd_score < 70:

#             crowd_level = "Medium"

#         else:

#             crowd_level = "High"


#         existing = (

#             db.query(FootfallData)

#             .filter(
#                 FootfallData.destination ==
#                 destination_name
#             )

#             .filter(
#                 FootfallData.visit_date ==
#                 datetime(2026, 8, day)
#             )

#             .first()

#         )


#         if not existing:

#             db.add(

#                 FootfallData(

#                     destination=
#                         destination_name,

#                     visit_date=
#                         datetime(2026, 8, day),

#                     crowd_level=
#                         crowd_level,

#                     crowd_score=
#                         crowd_score,

#                     estimated_visitors=
#                         crowd_score * 50

#                 )

#             )


# # =========================================================
# # SAVE DATABASE
# # =========================================================

# db.commit()

# db.close()


# print(
#     "AI prototype data inserted successfully."
# )

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
#
# COST STRUCTURE
#
# base_cost_per_person
#     Local sightseeing / activities
#
# hotel_cost_per_night
#     Average budget hotel cost
#
# food_cost_per_day
#     Approximate food cost per person
#
# transport_cost
#     Approximate local/intercity transport component
#
# =========================================================

destinations = [

    # =====================================================
    # NORTH BENGAL
    # =====================================================

    Destination(
        name="Darjeeling",
        district="Darjeeling",
        category="Mountain, Nature, Tea",
        description=(
            "A famous Himalayan destination known for "
            "Kanchenjunga views, tea gardens, colonial charm "
            "and peaceful mountain landscapes."
        ),
        best_for="Nature,Photography,Culture,Food",
        tags="mountain,nature,tea,culture,photography,kanchenjunga",
        average_stay=3,
        base_cost_per_person=1800,
        hotel_cost_per_night=2200,
        food_cost_per_day=750,
        transport_cost=700,
        rating=4.7,
        image="assets/img1.jpeg",
        latitude=27.0410,
        longitude=88.2663
    ),

    Destination(
        name="Kalimpong",
        district="Kalimpong",
        category="Mountain, Culture, Nature",
        description=(
            "A peaceful Himalayan town surrounded by valleys, "
            "monasteries, viewpoints and beautiful mountain landscapes."
        ),
        best_for="Nature,Culture,Photography",
        tags="mountain,nature,culture,monastery,photography",
        average_stay=2,
        base_cost_per_person=1400,
        hotel_cost_per_night=1800,
        food_cost_per_day=650,
        transport_cost=600,
        rating=4.5,
        image="assets/img2.jpeg",
        latitude=27.0667,
        longitude=88.4667
    ),

    Destination(
        name="Jaldapara",
        district="Alipurduar",
        category="Wildlife, Adventure, Nature",
        description=(
            "A wildlife destination famous for forests, "
            "grasslands, elephant safaris and natural landscapes."
        ),
        best_for="Wildlife,Adventure,Nature",
        tags="wildlife,forest,adventure,nature,safari,elephant",
        average_stay=2,
        base_cost_per_person=1900,
        hotel_cost_per_night=1800,
        food_cost_per_day=700,
        transport_cost=750,
        rating=4.6,
        image="assets/img3.jpeg",
        latitude=26.6944,
        longitude=89.2722
    ),

    Destination(
        name="Buxa",
        district="Alipurduar",
        category="Wildlife, Adventure, Nature",
        description=(
            "A forest and mountain destination suitable for "
            "trekking, wildlife exploration and adventure."
        ),
        best_for="Adventure,Wildlife,Nature",
        tags="forest,trekking,wildlife,adventure,nature",
        average_stay=2,
        base_cost_per_person=1500,
        hotel_cost_per_night=1400,
        food_cost_per_day=600,
        transport_cost=700,
        rating=4.4,
        image="assets/img3.jpeg",
        latitude=26.7040,
        longitude=89.5527
    ),

    Destination(
        name="Mirik",
        district="Darjeeling",
        category="Lake, Nature, Tea",
        description=(
            "A peaceful hill destination surrounded by tea gardens, "
            "forests and the beautiful Mirik Lake."
        ),
        best_for="Nature,Photography,Relaxation,Food",
        tags="lake,tea,nature,photography,relaxation",
        average_stay=2,
        base_cost_per_person=1100,
        hotel_cost_per_night=1500,
        food_cost_per_day=600,
        transport_cost=450,
        rating=4.3,
        image="assets/img2.jpeg",
        latitude=26.8894,
        longitude=88.1803
    ),

    Destination(
        name="Chatakpur",
        district="Darjeeling",
        category="Hidden Gem, Nature, Photography",
        description=(
            "A quiet forest village offering spectacular mountain "
            "views and a peaceful escape from crowded destinations."
        ),
        best_for="Nature,Photography,Relaxation",
        tags="hidden-gem,forest,nature,mountain,photography",
        average_stay=2,
        base_cost_per_person=1000,
        hotel_cost_per_night=1300,
        food_cost_per_day=550,
        transport_cost=500,
        rating=4.6,
        image="assets/img1.jpeg",
        latitude=26.9300,
        longitude=88.3650
    ),

    Destination(
        name="Sandakphu",
        district="Darjeeling",
        category="Trekking, Mountain, Adventure",
        description=(
            "The highest point in West Bengal offering dramatic "
            "Himalayan views and an unforgettable trekking experience."
        ),
        best_for="Adventure,Trekking,Photography,Nature",
        tags="trekking,mountain,adventure,himalaya,sandakphu",
        average_stay=4,
        base_cost_per_person=4500,
        hotel_cost_per_night=1000,
        food_cost_per_day=600,
        transport_cost=1800,
        rating=4.8,
        image="/images/sandakphu.jpg",
        latitude=27.1050,
        longitude=88.0040
    ),

    Destination(
        name="Tinchuley",
        district="Darjeeling",
        category="Village, Nature, Tea",
        description=(
            "A peaceful mountain village surrounded by tea gardens, "
            "pine forests and panoramic Himalayan views."
        ),
        best_for="Nature,Photography,Relaxation,Couples",
        tags="village,tea,mountain,nature,photography",
        average_stay=2,
        base_cost_per_person=1200,
        hotel_cost_per_night=1700,
        food_cost_per_day=650,
        transport_cost=550,
        rating=4.5,
        image="/images/tinchuley.jpg",
        latitude=27.1000,
        longitude=88.3900
    ),

    Destination(
        name="Lepchajagat",
        district="Darjeeling",
        category="Forest, Nature, Hidden Gem",
        description=(
            "A quiet forest destination surrounded by pine and "
            "rhododendron forests with beautiful Himalayan views."
        ),
        best_for="Nature,Photography,Relaxation,Couples",
        tags="forest,pine,rhododendron,nature,hidden-gem",
        average_stay=2,
        base_cost_per_person=1000,
        hotel_cost_per_night=1400,
        food_cost_per_day=550,
        transport_cost=500,
        rating=4.4,
        image="/images/lepchajagat.jpg",
        latitude=27.0200,
        longitude=88.2400
    ),

    Destination(
        name="Pedong",
        district="Kalimpong",
        category="Mountain, Adventure, Culture",
        description=(
            "A scenic Himalayan village offering monasteries, "
            "valleys, forests and peaceful mountain experiences."
        ),
        best_for="Adventure,Nature,Culture,Photography",
        tags="mountain,village,monastery,adventure,nature",
        average_stay=2,
        base_cost_per_person=1300,
        hotel_cost_per_night=1500,
        food_cost_per_day=600,
        transport_cost=600,
        rating=4.4,
        image="/images/pedong.jpg",
        latitude=27.1800,
        longitude=88.6100
    ),

    Destination(
        name="Samsing",
        district="Jalpaiguri",
        category="Forest, Tea, Nature",
        description=(
            "A beautiful Dooars destination surrounded by tea gardens, "
            "forests, streams and rolling green hills."
        ),
        best_for="Nature,Photography,Relaxation",
        tags="dooars,tea,forest,nature,waterfall",
        average_stay=2,
        base_cost_per_person=1200,
        hotel_cost_per_night=1600,
        food_cost_per_day=600,
        transport_cost=650,
        rating=4.5,
        image="/images/samsing.jpg",
        latitude=26.8700,
        longitude=88.7800
    ),

    Destination(
        name="Neora Valley",
        district="Kalimpong",
        category="Wildlife, Forest, Adventure",
        description=(
            "A pristine Himalayan forest region known for biodiversity, "
            "trekking trails and untouched natural landscapes."
        ),
        best_for="Wildlife,Trekking,Nature,Photography",
        tags="wildlife,forest,trekking,nature,biodiversity",
        average_stay=3,
        base_cost_per_person=2500,
        hotel_cost_per_night=1600,
        food_cost_per_day=650,
        transport_cost=900,
        rating=4.7,
        image="/images/neora-valley.jpg",
        latitude=27.0200,
        longitude=88.7000
    ),


    # =====================================================
    # MEGHALAYA
    # =====================================================

    Destination(
        name="Shillong",
        district="East Khasi Hills",
        category="Mountain, Nature, Culture",
        description=(
            "The scenic capital of Meghalaya surrounded by hills, "
            "waterfalls, lakes and vibrant local culture."
        ),
        best_for="Nature,Culture,Photography,Food",
        tags="meghalaya,shillong,mountain,waterfall,culture",
        average_stay=3,
        base_cost_per_person=2200,
        hotel_cost_per_night=2500,
        food_cost_per_day=800,
        transport_cost=1000,
        rating=4.7,
        image="/images/shillong.jpg",
        latitude=25.5788,
        longitude=91.8933
    ),

    Destination(
        name="Sohra",
        district="East Khasi Hills",
        category="Waterfalls, Nature, Adventure",
        description=(
            "Formerly known as Cherrapunji, Sohra is famous for "
            "waterfalls, caves, misty valleys and dramatic landscapes."
        ),
        best_for="Nature,Adventure,Photography,Trekking",
        tags="sohra,cherrapunji,waterfall,caves,nature,trekking",
        average_stay=3,
        base_cost_per_person=2400,
        hotel_cost_per_night=2300,
        food_cost_per_day=750,
        transport_cost=1100,
        rating=4.8,
        image="/images/sohra.jpg",
        latitude=25.2700,
        longitude=91.7300
    ),

    Destination(
        name="Dawki",
        district="West Jaintia Hills",
        category="River, Adventure, Nature",
        description=(
            "A stunning border destination famous for the crystal-clear "
            "Umngot River and surrounding green hills."
        ),
        best_for="Adventure,Nature,Photography,Water",
        tags="dawki,umngot,river,boating,adventure",
        average_stay=2,
        base_cost_per_person=1800,
        hotel_cost_per_night=1800,
        food_cost_per_day=700,
        transport_cost=1200,
        rating=4.8,
        image="/images/dawki.jpg",
        latitude=25.1930,
        longitude=92.0250
    ),

    Destination(
        name="Shnongpdeng",
        district="West Jaintia Hills",
        category="Adventure, River, Nature",
        description=(
            "A riverside adventure destination known for clear water, "
            "boating, kayaking and peaceful village surroundings."
        ),
        best_for="Adventure,Water,Nature,Photography",
        tags="shnongpdeng,river,kayaking,boating,adventure",
        average_stay=2,
        base_cost_per_person=1700,
        hotel_cost_per_night=1500,
        food_cost_per_day=650,
        transport_cost=1100,
        rating=4.7,
        image="/images/shnongpdeng.jpg",
        latitude=25.1800,
        longitude=92.0400
    ),

    Destination(
        name="Mawlynnong",
        district="East Khasi Hills",
        category="Village, Nature, Culture",
        description=(
            "A picturesque Meghalaya village surrounded by lush greenery, "
            "living root bridges and peaceful countryside."
        ),
        best_for="Nature,Culture,Photography,Relaxation",
        tags="mawlynnong,village,root-bridge,nature,culture",
        average_stay=2,
        base_cost_per_person=1500,
        hotel_cost_per_night=1600,
        food_cost_per_day=650,
        transport_cost=1000,
        rating=4.6,
        image="/images/mawlynnong.jpg",
        latitude=25.2100,
        longitude=91.9200
    ),


    # =====================================================
    # ASSAM
    # =====================================================

    Destination(
        name="Kaziranga",
        district="Golaghat",
        category="Wildlife, Safari, Nature",
        description=(
            "A world-famous wildlife destination known for the "
            "greater one-horned rhinoceros, elephants and grasslands."
        ),
        best_for="Wildlife,Safari,Nature,Photography",
        tags="kaziranga,wildlife,rhino,safari,forest",
        average_stay=3,
        base_cost_per_person=2800,
        hotel_cost_per_night=2400,
        food_cost_per_day=750,
        transport_cost=1200,
        rating=4.8,
        image="/images/kaziranga.jpg",
        latitude=26.5775,
        longitude=93.1711
    ),

    Destination(
        name="Majuli",
        district="Majuli",
        category="Culture, Island, Nature",
        description=(
            "A unique river island known for Assamese culture, "
            "Satras, traditional crafts and peaceful rural landscapes."
        ),
        best_for="Culture,Nature,Photography,Food",
        tags="majuli,island,assamese,culture,satra,nature",
        average_stay=3,
        base_cost_per_person=1900,
        hotel_cost_per_night=1500,
        food_cost_per_day=600,
        transport_cost=900,
        rating=4.6,
        image="/images/majuli.jpg",
        latitude=27.0016,
        longitude=94.2243
    ),

    Destination(
        name="Manas",
        district="Baksa",
        category="Wildlife, Adventure, Nature",
        description=(
            "A spectacular national park at the foothills of Bhutan "
            "known for forests, grasslands and diverse wildlife."
        ),
        best_for="Wildlife,Adventure,Safari,Photography",
        tags="manas,wildlife,safari,forest,bhutan",
        average_stay=3,
        base_cost_per_person=2600,
        hotel_cost_per_night=2200,
        food_cost_per_day=700,
        transport_cost=1100,
        rating=4.8,
        image="/images/manas.jpg",
        latitude=26.6590,
        longitude=91.0010
    ),

    Destination(
        name="Guwahati",
        district="Kamrup Metropolitan",
        category="Culture, Food, Nature",
        description=(
            "The gateway to Northeast India, offering temples, "
            "river views, Assamese cuisine and easy access to Meghalaya."
        ),
        best_for="Culture,Food,Nature,Photography",
        tags="guwahati,assam,culture,food,brahmaputra,temple",
        average_stay=2,
        base_cost_per_person=1400,
        hotel_cost_per_night=1800,
        food_cost_per_day=650,
        transport_cost=600,
        rating=4.4,
        image="/images/guwahati.jpg",
        latitude=26.1445,
        longitude=91.7362
    )

]


# =========================================================
# INSERT DESTINATIONS WITHOUT DUPLICATES
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


db.commit()


# =========================================================
# TRAVEL COST DATA
# =========================================================
#
# Costs are prototype estimates per person.
#
# They are deliberately separated from destination's
# general transport_cost so the AI can compare transport
# options.
#
# =========================================================

transport_data = [

    # =====================================================
    # DARJEELING
    # =====================================================

    TravelCost(
        destination="Darjeeling",
        transport_type="Bus",
        estimated_cost=300,
        duration_hours=4.5,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Darjeeling",
        transport_type="Shared Car",
        estimated_cost=500,
        duration_hours=3.5,
        comfort_level="High"
    ),

    TravelCost(
        destination="Darjeeling",
        transport_type="Train",
        estimated_cost=250,
        duration_hours=5,
        comfort_level="Medium"
    ),


    # =====================================================
    # KALIMPONG
    # =====================================================

    TravelCost(
        destination="Kalimpong",
        transport_type="Bus",
        estimated_cost=250,
        duration_hours=3.5,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Kalimpong",
        transport_type="Shared Car",
        estimated_cost=450,
        duration_hours=3,
        comfort_level="High"
    ),

    TravelCost(
        destination="Kalimpong",
        transport_type="Train",
        estimated_cost=250,
        duration_hours=4.5,
        comfort_level="Medium"
    ),


    # =====================================================
    # JALDAPARA
    # =====================================================

    TravelCost(
        destination="Jaldapara",
        transport_type="Bus",
        estimated_cost=400,
        duration_hours=4.5,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Jaldapara",
        transport_type="Train",
        estimated_cost=300,
        duration_hours=4,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Jaldapara",
        transport_type="Shared Car",
        estimated_cost=550,
        duration_hours=3.5,
        comfort_level="High"
    ),


    # =====================================================
    # BUXA
    # =====================================================

    TravelCost(
        destination="Buxa",
        transport_type="Bus",
        estimated_cost=350,
        duration_hours=4.5,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Buxa",
        transport_type="Shared Car",
        estimated_cost=500,
        duration_hours=3.5,
        comfort_level="High"
    ),


    # =====================================================
    # MIRIK
    # =====================================================

    TravelCost(
        destination="Mirik",
        transport_type="Bus",
        estimated_cost=250,
        duration_hours=3,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Mirik",
        transport_type="Shared Car",
        estimated_cost=400,
        duration_hours=2.5,
        comfort_level="High"
    ),


    # =====================================================
    # CHATAKPUR
    # =====================================================

    TravelCost(
        destination="Chatakpur",
        transport_type="Shared Car",
        estimated_cost=450,
        duration_hours=3,
        comfort_level="High"
    ),

    TravelCost(
        destination="Chatakpur",
        transport_type="Bus",
        estimated_cost=300,
        duration_hours=4,
        comfort_level="Medium"
    ),


    # =====================================================
    # SANDAKPHU
    # =====================================================

    TravelCost(
        destination="Sandakphu",
        transport_type="Shared Jeep",
        estimated_cost=1800,
        duration_hours=7,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Sandakphu",
        transport_type="Trekking",
        estimated_cost=1200,
        duration_hours=8,
        comfort_level="Adventure"
    ),


    # =====================================================
    # TINCHULEY
    # =====================================================

    TravelCost(
        destination="Tinchuley",
        transport_type="Shared Car",
        estimated_cost=550,
        duration_hours=3.5,
        comfort_level="High"
    ),

    TravelCost(
        destination="Tinchuley",
        transport_type="Bus",
        estimated_cost=300,
        duration_hours=5,
        comfort_level="Medium"
    ),


    # =====================================================
    # LEPCHAJAGAT
    # =====================================================

    TravelCost(
        destination="Lepchajagat",
        transport_type="Shared Car",
        estimated_cost=500,
        duration_hours=3,
        comfort_level="High"
    ),

    TravelCost(
        destination="Lepchajagat",
        transport_type="Bus",
        estimated_cost=300,
        duration_hours=4,
        comfort_level="Medium"
    ),


    # =====================================================
    # PEDONG
    # =====================================================

    TravelCost(
        destination="Pedong",
        transport_type="Shared Car",
        estimated_cost=550,
        duration_hours=3.5,
        comfort_level="High"
    ),

    TravelCost(
        destination="Pedong",
        transport_type="Bus",
        estimated_cost=300,
        duration_hours=5,
        comfort_level="Medium"
    ),


    # =====================================================
    # SAMSING
    # =====================================================

    TravelCost(
        destination="Samsing",
        transport_type="Shared Car",
        estimated_cost=650,
        duration_hours=4,
        comfort_level="High"
    ),

    TravelCost(
        destination="Samsing",
        transport_type="Bus",
        estimated_cost=400,
        duration_hours=5,
        comfort_level="Medium"
    ),


    # =====================================================
    # NEORA VALLEY
    # =====================================================

    TravelCost(
        destination="Neora Valley",
        transport_type="Shared Car",
        estimated_cost=900,
        duration_hours=5,
        comfort_level="High"
    ),

    TravelCost(
        destination="Neora Valley",
        transport_type="Bus",
        estimated_cost=500,
        duration_hours=7,
        comfort_level="Medium"
    ),


    # =====================================================
    # SHILLONG
    # =====================================================

    TravelCost(
        destination="Shillong",
        transport_type="Shared Taxi",
        estimated_cost=600,
        duration_hours=3,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Shillong",
        transport_type="Bus",
        estimated_cost=500,
        duration_hours=4,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Shillong",
        transport_type="Flight",
        estimated_cost=3500,
        duration_hours=1.5,
        comfort_level="High"
    ),


    # =====================================================
    # SOHRA
    # =====================================================

    TravelCost(
        destination="Sohra",
        transport_type="Shared Taxi",
        estimated_cost=700,
        duration_hours=2.5,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Sohra",
        transport_type="Private Car",
        estimated_cost=1800,
        duration_hours=2,
        comfort_level="High"
    ),


    # =====================================================
    # DAWKI
    # =====================================================

    TravelCost(
        destination="Dawki",
        transport_type="Shared Taxi",
        estimated_cost=900,
        duration_hours=3.5,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Dawki",
        transport_type="Private Car",
        estimated_cost=2200,
        duration_hours=3,
        comfort_level="High"
    ),


    # =====================================================
    # SHNONGPDENG
    # =====================================================

    TravelCost(
        destination="Shnongpdeng",
        transport_type="Shared Taxi",
        estimated_cost=900,
        duration_hours=4,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Shnongpdeng",
        transport_type="Private Car",
        estimated_cost=2200,
        duration_hours=3.5,
        comfort_level="High"
    ),


    # =====================================================
    # MAWLYNNONG
    # =====================================================

    TravelCost(
        destination="Mawlynnong",
        transport_type="Shared Taxi",
        estimated_cost=800,
        duration_hours=3.5,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Mawlynnong",
        transport_type="Private Car",
        estimated_cost=2000,
        duration_hours=3,
        comfort_level="High"
    ),


    # =====================================================
    # KAZIRANGA
    # =====================================================

    TravelCost(
        destination="Kaziranga",
        transport_type="Bus",
        estimated_cost=500,
        duration_hours=4.5,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Kaziranga",
        transport_type="Train",
        estimated_cost=350,
        duration_hours=4,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Kaziranga",
        transport_type="Shared Car",
        estimated_cost=900,
        duration_hours=3.5,
        comfort_level="High"
    ),


    # =====================================================
    # MAJULI
    # =====================================================

    TravelCost(
        destination="Majuli",
        transport_type="Bus",
        estimated_cost=450,
        duration_hours=5,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Majuli",
        transport_type="Train",
        estimated_cost=350,
        duration_hours=4,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Majuli",
        transport_type="Ferry",
        estimated_cost=100,
        duration_hours=1.5,
        comfort_level="Medium"
    ),


    # =====================================================
    # MANAS
    # =====================================================

    TravelCost(
        destination="Manas",
        transport_type="Bus",
        estimated_cost=500,
        duration_hours=4,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Manas",
        transport_type="Shared Car",
        estimated_cost=900,
        duration_hours=3,
        comfort_level="High"
    ),


    # =====================================================
    # GUWAHATI
    # =====================================================

    TravelCost(
        destination="Guwahati",
        transport_type="Bus",
        estimated_cost=400,
        duration_hours=5,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Guwahati",
        transport_type="Train",
        estimated_cost=350,
        duration_hours=4,
        comfort_level="Medium"
    ),

    TravelCost(
        destination="Guwahati",
        transport_type="Flight",
        estimated_cost=3000,
        duration_hours=1.5,
        comfort_level="High"
    )

]


# =========================================================
# INSERT TRANSPORT DATA WITHOUT DUPLICATES
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
# FOOTFALL DESTINATIONS
# =========================================================

destinations_names = [

    "Darjeeling",
    "Kalimpong",
    "Jaldapara",
    "Buxa",
    "Mirik",
    "Chatakpur",
    "Sandakphu",
    "Tinchuley",
    "Lepchajagat",
    "Pedong",
    "Samsing",
    "Neora Valley",
    "Shillong",
    "Sohra",
    "Dawki",
    "Shnongpdeng",
    "Mawlynnong",
    "Kaziranga",
    "Majuli",
    "Manas",
    "Guwahati"

]


# =========================================================
# GENERATE FOOTFALL DATA
# =========================================================
#
# Prototype data.
# This should NOT be presented as live visitor statistics.
#
# =========================================================

for destination_name in destinations_names:

    for day in range(1, 31):

        # Different destinations get slightly different
        # crowd patterns.

        destination_factor = (
            sum(ord(char) for char in destination_name)
            % 20
        )

        crowd_score = (
            25 +
            ((day * 7 + destination_factor) % 70)
        )

        crowd_score = min(crowd_score, 95)


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
                    destination=destination_name,
                    visit_date=datetime(2026, 8, day),
                    crowd_level=crowd_level,
                    crowd_score=crowd_score,
                    estimated_visitors=crowd_score * 50
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

print(
    "Destinations:",
    len(destinations)
)

print(
    "Travel cost options:",
    len(transport_data)
)

print(
    "Footfall destinations:",
    len(destinations_names)
)