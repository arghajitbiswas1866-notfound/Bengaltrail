const API_URL =
    "http://127.0.0.1:8000";


const form =
    document.getElementById(
        "aiPlannerForm"
    );


const loading =
    document.getElementById(
        "loading"
    );


const resultsSection =
    document.getElementById(
        "resultsSection"
    );


const resultsContainer =
    document.getElementById(
        "resultsContainer"
    );


const generateBtn =
    document.getElementById(
        "generateBtn"
    );



form.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        // =========================================
        // GET USER INPUT
        // =========================================

        const startingLocation =
            document.getElementById(
                "startingLocation"
            ).value.trim();


        const travelDate =
            document.getElementById(
                "travelDate"
            ).value;


        const people =
            Number(
                document.getElementById(
                    "people"
                ).value
            );


        const budget =
            Number(
                document.getElementById(
                    "budget"
                ).value
            );


        const experience =
            document.getElementById(
                "experience"
            ).value;


        const duration =
            Number(
                document.getElementById(
                    "duration"
                ).value
            );


        const transport =
            document.getElementById(
                "transport"
            ).value;


        const weatherPreference =
            document.getElementById(
                "weatherPreference"
            ).value;


        const footfallPreference =
            document.getElementById(
                "footfallPreference"
            ).value;



        // =========================================
        // SHOW LOADING
        // =========================================

        loading.classList.remove(
            "hidden"
        );

        resultsSection.classList.add(
            "hidden"
        );

        resultsContainer.innerHTML = "";

        generateBtn.disabled = true;



        try {

            // =========================================
            // SEND TO FASTAPI
            // =========================================

            const response =
                await fetch(
                    `${API_URL}/api/ai/plan`,
                    {

                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body:
                            JSON.stringify({

                                starting_location:
                                    startingLocation,

                                travel_date:
                                    travelDate,

                                people:
                                    people,

                                budget:
                                    budget,

                                experience:
                                    experience,

                                duration:
                                    duration,

                                transport:
                                    transport,

                                weather_preference:
                                    weatherPreference,

                                footfall_preference:
                                    footfallPreference

                            })

                    }
                );



            const data =
                await response.json();


            if (!response.ok) {

                throw new Error(
                    data.detail ||
                    "AI planner failed"
                );

            }


            // =========================================
            // DISPLAY RESULTS
            // =========================================

            displayResults(
                data.recommendations
            );


        } catch (error) {

            console.error(
                "AI planner error:",
                error
            );


            alert(
                error.message ||
                "Unable to generate recommendations."
            );

        } finally {

            loading.classList.add(
                "hidden"
            );

            generateBtn.disabled =
                false;

        }

    }
);



// =========================================
// DISPLAY RESULTS
// =========================================

function displayResults(
    recommendations
) {

    resultsContainer.innerHTML = "";


    if (
        !recommendations ||
        recommendations.length === 0
    ) {

        resultsContainer.innerHTML = `

            <p>
                No suitable destinations
                were found.
            </p>

        `;

        resultsSection.classList.remove(
            "hidden"
        );

        return;
    }


    recommendations.forEach(
        (place, index) => {

            const image =
                place.image ||
                "assets/img1.jpeg";


            const card =
                document.createElement(
                    "article"
                );


            card.className =
                "result-card";


            card.innerHTML = `

                <img
                    class="result-image"
                    src="${image}"
                    alt="${place.destination}"
                >


                <div class="result-content">

                    <span class="match">

                        ${place.ai_match}% AI MATCH

                    </span>


                    <h3>
                        ${index + 1}.
                        ${place.destination}
                    </h3>


                    <p class="category">

                        ${place.category}

                    </p>


                    <p class="result-description">

                        ${place.description}

                    </p>


                    <div class="result-stats">


                        <div class="stat">

                            <small>
                                Estimated Budget
                            </small>

                            <strong>
                                ₹${Math.round(
                                    place.estimated_budget
                                )}
                            </strong>

                        </div>


                        <div class="stat">

                            <small>
                                Rating
                            </small>

                            <strong>
                                ⭐ ${place.rating}
                            </strong>

                        </div>


                        <div class="stat">

                            <small>
                                Transport
                            </small>

                            <strong>
                                ${place.transport}
                            </strong>

                        </div>


                        <div class="stat">

                            <small>
                                Crowd
                            </small>

                            <strong>
                                ${place.crowd_level}
                            </strong>

                        </div>

                        



                    </div>

                    <button class="result-book-now-btn">
                            Book Now
                    </button>

                </div>

            `;


            resultsContainer.appendChild(
                card
            );

        }
    );


    resultsSection.classList.remove(
        "hidden"
    );


    resultsSection.scrollIntoView({
        behavior: "smooth"
    });

}