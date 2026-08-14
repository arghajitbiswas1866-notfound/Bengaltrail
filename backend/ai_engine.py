from math import radians, sin, cos, sqrt, atan2

from sqlalchemy.orm import Session

from models import (
    Destination,
    FootfallData
)


# =========================================================
# STARTING LOCATIONS
# =========================================================

STARTING_LOCATIONS = {

    "siliguri": {
        "latitude": 26.7271,
        "longitude": 88.3953
    },

    "kolkata": {
        "latitude": 22.5726,
        "longitude": 88.3639
    },

    "durgapur": {
        "latitude": 23.5204,
        "longitude": 87.3119
    },

    "asansol": {
        "latitude": 23.6739,
        "longitude": 86.9524
    },

    "malda": {
        "latitude": 25.0108,
        "longitude": 88.1411
    }

}


# =========================================================
# TEXT MATCHING
# =========================================================

def text_match(
    user_text,
    destination_text
):

    if not user_text:
        return 0

    if not destination_text:
        return 0

    user_words = set(
        word.strip().lower()
        for word in user_text.split(",")
        if word.strip()
    )

    destination_words = set(
        word.strip().lower()
        for word in destination_text.split(",")
        if word.strip()
    )

    if not user_words:
        return 0

    matches = user_words.intersection(
        destination_words
    )

    return (
        len(matches) /
        len(user_words)
    ) * 100


# =========================================================
# STARTING LOCATION LOOKUP
# =========================================================

def get_starting_coordinates(
    starting_location
):

    if not starting_location:
        return None

    location = (
        starting_location
        .strip()
        .lower()
    )

    return STARTING_LOCATIONS.get(
        location
    )


# =========================================================
# DISTANCE CALCULATION
# =========================================================

def calculate_distance(
    lat1,
    lon1,
    lat2,
    lon2
):

    earth_radius_km = 6371

    lat1 = radians(lat1)
    lon1 = radians(lon1)

    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        sin(dlat / 2) ** 2
        +
        cos(lat1)
        *
        cos(lat2)
        *
        sin(dlon / 2) ** 2
    )

    c = 2 * atan2(
        sqrt(a),
        sqrt(1 - a)
    )

    return earth_radius_km * c


# =========================================================
# LOCATION SCORE
# =========================================================

def calculate_location_score(
    starting_location,
    destination
):

    if not starting_location:
        return 50

    location = (
        starting_location
        .strip()
        .lower()
    )

    destination_name = (
        destination.name.lower()
        if destination.name
        else ""
    )

    district = (
        destination.district.lower()
        if destination.district
        else ""
    )

    # Same destination or district
    if (
        location in destination_name
        or
        location in district
    ):
        return 100

    # Siliguri is the major North Bengal gateway
    if location == "siliguri":

        nearby_places = [
            "darjeeling",
            "kalimpong",
            "mirik",
            "chatakpur",
            "lava",
            "loleygaon"
        ]

        if destination_name in nearby_places:
            return 90

        return 65

    # Kolkata
    if location == "kolkata":

        return 60

    return 50


# =========================================================
# TRAVEL COST CALCULATION
# =========================================================

def calculate_travel_cost(
    starting_location,
    destination,
    transport
):

    start = get_starting_coordinates(
        starting_location
    )

    # -----------------------------------------------------
    # Unknown starting location
    # -----------------------------------------------------

    if not start:

        return {
            "distance_km": 0,
            "cost_per_person": (
                destination.transport_cost or 0
            )
        }


    # -----------------------------------------------------
    # Destination coordinates missing
    # -----------------------------------------------------

    if (
        destination.latitude is None
        or
        destination.longitude is None
    ):

        return {
            "distance_km": 0,
            "cost_per_person": (
                destination.transport_cost or 0
            )
        }


    # -----------------------------------------------------
    # Calculate straight-line distance
    # -----------------------------------------------------

    distance = calculate_distance(

        start["latitude"],
        start["longitude"],

        destination.latitude,
        destination.longitude

    )


    # -----------------------------------------------------
    # Prototype transport rates
    # -----------------------------------------------------

    rates = {

        "bus": {
            "base": 80,
            "per_km": 2.2
        },

        "train": {
            "base": 100,
            "per_km": 1.8
        },

        "shared car": {
            "base": 150,
            "per_km": 3.5
        },

        "private car": {
            "base": 500,
            "per_km": 12.0
        }

    }


    transport_key = (
        transport.strip().lower()
        if transport
        else "bus"
    )


    rate = rates.get(

        transport_key,

        {
            "base": 100,
            "per_km": 2.5
        }

    )


    # -----------------------------------------------------
    # Calculate estimated one-way cost
    # -----------------------------------------------------

    cost = (

        rate["base"]

        +

        distance * rate["per_km"]

    )


    # -----------------------------------------------------
    # Round to nearest ₹10
    # -----------------------------------------------------

    cost = round(
        cost / 10
    ) * 10


    return {

        "distance_km":
            round(distance, 1),

        "cost_per_person":
            round(cost)

    }


# =========================================================
# BUDGET CALCULATION
# =========================================================

def calculate_budget(
    destination,
    transport_cost,
    people,
    duration
):

    hotel_cost = (
        destination.hotel_cost_per_night
        *
        duration
    )

    food_cost = (
        destination.food_cost_per_day
        *
        duration
        *
        people
    )

    activity_cost = (
        destination.base_cost_per_person
        *
        people
    )

    transport_total = (
        transport_cost
        *
        people
    )

    total = (

        hotel_cost

        +

        food_cost

        +

        activity_cost

        +

        transport_total

    )

    return {

        "total":
            round(total),

        "hotel":
            round(hotel_cost),

        "food":
            round(food_cost),

        "activities":
            round(activity_cost),

        "transport":
            round(transport_total)

    }


# =========================================================
# BUDGET SCORE
# =========================================================

def calculate_budget_score(
    total_budget,
    user_budget
):

    if not user_budget:
        return 50

    # Within budget
    if total_budget <= user_budget:

        difference = (
            user_budget -
            total_budget
        )

        percentage_saved = (
            difference /
            user_budget
        ) * 100

        score = (
            100 -
            percentage_saved * 0.35
        )

        return round(
            max(
                65,
                min(100, score)
            )
        )


    # Over budget
    over_budget = (
        total_budget -
        user_budget
    )

    over_percentage = (
        over_budget /
        user_budget
    ) * 100

    score = (
        100 -
        over_percentage * 1.5
    )

    return round(
        max(
            0,
            min(100, score)
        )
    )


# =========================================================
# FOOTFALL SCORE
# =========================================================

def calculate_footfall_score(
    crowd_score,
    preference
):

    if not preference:
        return 50

    preference = preference.lower()


    if preference == "low":

        return max(
            0,
            100 - crowd_score
        )


    if preference == "medium":

        distance = abs(
            50 - crowd_score
        )

        return max(
            0,
            100 - distance
        )


    if preference == "high":

        return crowd_score


    return 50


# =========================================================
# WEATHER SCORE
# =========================================================

def calculate_weather_score(
    weather_preference,
    destination
):

    if not weather_preference:
        return 50

    preference = (
        weather_preference
        .strip()
        .lower()
    )

    category = (
        destination.category.lower()
        if destination.category
        else ""
    )

    tags = (
        destination.tags.lower()
        if destination.tags
        else ""
    )


    if preference == "cool":

        if (
            "mountain" in category
            or
            "mountain" in tags
            or
            "forest" in tags
        ):
            return 95

        return 60


    if preference == "warm":

        if (
            "lake" in category
            or
            "wildlife" in category
        ):
            return 75

        return 60


    if preference == "pleasant":

        return 85


    if preference == "any":

        return 70


    return 50


# =========================================================
# TRANSPORT SCORE
# =========================================================

def calculate_transport_score(
    transport
):

    if not transport:
        return 50

    # For the prototype, if the user
    # selected a supported transport type,
    # give a good score.

    supported = [
        "bus",
        "train",
        "shared car",
        "private car"
    ]

    if transport.strip().lower() in supported:
        return 100

    return 50


# =========================================================
# AI MATCH
# =========================================================

def calculate_match(

    destination,

    experience,

    budget_score,

    footfall_score,

    transport_score,

    weather_score,

    location_score

):

    experience_score = text_match(

        experience,

        destination.best_for

    )


    tag_score = text_match(

        experience,

        destination.tags

    )


    experience_final = (

        experience_score * 0.70

        +

        tag_score * 0.30

    )


    # -----------------------------------------------------
    # FINAL WEIGHTING
    # -----------------------------------------------------

    final_score = (

        experience_final * 0.30

        +

        budget_score * 0.25

        +

        footfall_score * 0.15

        +

        transport_score * 0.10

        +

        weather_score * 0.08

        +

        location_score * 0.07

        +

        (
            (destination.rating or 0)
            / 5
            * 100
        ) * 0.05

    )


    return round(
        max(
            0,
            min(
                100,
                final_score
            )
        )
    )


# =========================================================
# MAIN RECOMMENDATION FUNCTION
# =========================================================

def generate_recommendations(

    db: Session,

    starting_location,

    experience,

    budget,

    people,

    duration,

    transport,

    visit_date,

    weather_preference,

    footfall_preference

):

    # =====================================================
    # GET ALL DESTINATIONS
    # =====================================================

    destinations = (
        db.query(Destination)
        .all()
    )


    recommendations = []


    # =====================================================
    # ANALYZE EACH DESTINATION
    # =====================================================

    for destination in destinations:


        # -------------------------------------------------
        # TRAVEL
        # -------------------------------------------------

        travel_information = (
            calculate_travel_cost(

                starting_location,

                destination,

                transport

            )
        )


        transport_cost = (
            travel_information[
                "cost_per_person"
            ]
        )


        distance_km = (
            travel_information[
                "distance_km"
            ]
        )


        # -------------------------------------------------
        # BUDGET
        # -------------------------------------------------

        budget_breakdown = (
            calculate_budget(

                destination,

                transport_cost,

                people,

                duration

            )
        )


        total_budget = (
            budget_breakdown["total"]
        )


        budget_score = (
            calculate_budget_score(

                total_budget,

                budget

            )
        )


        # -------------------------------------------------
        # FOOTFALL
        # -------------------------------------------------

        footfall = (

            db.query(FootfallData)

            .filter(
                FootfallData.destination
                ==
                destination.name
            )

            .filter(
                FootfallData.visit_date
                ==
                visit_date
            )

            .first()

        )


        if footfall:

            crowd_score = (
                footfall.crowd_score
            )

            crowd_level = (
                footfall.crowd_level
            )

        else:

            crowd_score = 50

            crowd_level = "Unknown"


        footfall_score = (
            calculate_footfall_score(

                crowd_score,

                footfall_preference

            )
        )


        # -------------------------------------------------
        # WEATHER
        # -------------------------------------------------

        weather_score = (
            calculate_weather_score(

                weather_preference,

                destination

            )
        )


        # -------------------------------------------------
        # LOCATION
        # -------------------------------------------------

        location_score = (
            calculate_location_score(

                starting_location,

                destination

            )
        )


        # -------------------------------------------------
        # TRANSPORT
        # -------------------------------------------------

        transport_score = (
            calculate_transport_score(

                transport

            )
        )


        # -------------------------------------------------
        # FINAL AI SCORE
        # -------------------------------------------------

        match_score = calculate_match(

            destination,

            experience,

            budget_score,

            footfall_score,

            transport_score,

            weather_score,

            location_score

        )


        # -------------------------------------------------
        # STORE RESULT
        # -------------------------------------------------

        recommendations.append({

            "destination":
                destination.name,

            "district":
                destination.district,

            "category":
                destination.category,

            "description":
                destination.description,

            "rating":
                destination.rating,

            "image":
                destination.image,

            "ai_match":
                match_score,

            "estimated_budget":
                total_budget,

            "transport":
                transport,

            "distance_km":
                distance_km,

            "transport_cost":
                budget_breakdown[
                    "transport"
                ],

            "hotel_cost":
                budget_breakdown[
                    "hotel"
                ],

            "food_cost":
                budget_breakdown[
                    "food"
                ],

            "activity_cost":
                budget_breakdown[
                    "activities"
                ],

            "crowd_level":
                crowd_level,

            "crowd_score":
                crowd_score,

            "duration":
                duration,

            "experience_score":
                round(
                    text_match(
                        experience,
                        destination.best_for
                    )
                ),

            "budget_score":
                budget_score,

            "footfall_score":
                footfall_score,

            "weather_score":
                weather_score,

            "location_score":
                location_score

        })


    # =====================================================
    # SORT
    # =====================================================

    recommendations.sort(

        key=lambda item:
            item["ai_match"],

        reverse=True

    )


    # =====================================================
    # RETURN TOP 5
    # =====================================================

    return recommendations[:5]