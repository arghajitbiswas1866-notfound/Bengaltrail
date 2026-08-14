const menuBtn = document.getElementById("menu-btn");
const navLinks = document.getElementById("nav-links");
const menuBtnIcon = menuBtn.querySelector("i");

menuBtn.addEventListener("click", (e) => {
  navLinks.classList.toggle("open");

  const isOpen = navLinks.classList.contains("open");
  menuBtnIcon.setAttribute("class", isOpen ? "ri-close-line" : "ri-menu-line");
});

navLinks.addEventListener("click", (e) => {
  navLinks.classList.remove("open");
  menuBtnIcon.setAttribute("class", "ri-menu-line");
});

const scrollRevealOption = {
  origin: "bottom",
  distance: "50px",
  duration: 1000,
};

ScrollReveal().reveal(".header__image img", {
  ...scrollRevealOption,
  origin: "right",
});
ScrollReveal().reveal(".header__content p", {
  ...scrollRevealOption,
  delay: 500,
});
ScrollReveal().reveal(".header__content h1", {
  ...scrollRevealOption,
  delay: 1000,
});
ScrollReveal().reveal(".header__btns", {
  ...scrollRevealOption,
  delay: 1500,
});

ScrollReveal().reveal(".destination__card", {
  ...scrollRevealOption,
  interval: 500,
});

ScrollReveal().reveal(".showcase__image img", {
  ...scrollRevealOption,
  origin: "left",
});
ScrollReveal().reveal(".showcase__content h4", {
  ...scrollRevealOption,
  delay: 500,
});
ScrollReveal().reveal(".showcase__content p", {
  ...scrollRevealOption,
  delay: 1000,
});
ScrollReveal().reveal(".showcase__btn", {
  ...scrollRevealOption,
  delay: 1500,
});

ScrollReveal().reveal(".banner__card", {
  ...scrollRevealOption,
  interval: 500,
});

ScrollReveal().reveal(".discover__card", {
  ...scrollRevealOption,
  interval: 500,
});

const swiper = new Swiper(".swiper", {
  slidesPerView: 3,
  spaceBetween: 20,
  loop: true,
});

// Add click event listener to the "TRIP" button //
const tripLink = document.getElementById("tour");

if (tripLink) {
  tripLink.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = "index.html";
  });
}

// Add click event listener to the "BOOK TRIP" button //
const booktripBtn = document.getElementById("booktrip-btn");

if (booktripBtn) {
  booktripBtn.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = "index.html";
  });
}


const booktripBtn2 = document.getElementById("booktrip-btn-2");

if (booktripBtn2) {
  booktripBtn2.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = "index.html";
  });
}

//PROFILE BTN
// document.addEventListener("DOMContentLoaded", () => {

//     const profileBtn = document.getElementById("profileBtn");

//     if (!profileBtn) return;

//     profileBtn.addEventListener("click", async () => {

//         try {

//             const response = await fetch(
//                 "http://127.0.0.1:8000/api/check-auth"
//             );

//             const data = await response.json();

//             if (data.logged_in) {

//                 // User is already logged in
//                 window.location.href = "profile.html";

//             } else {

//                 // User is not logged in
//                 window.location.href = "auth.html";

//             }

//         } catch (error) {

//             console.error(
//                 "Authentication check failed:",
//                 error
//             );

//             // If backend isn't responding
//             // send user to authentication page
//             window.location.href = "auth.html";
//         }

//     });

// });

const FALLBACK_API_URL = "http://127.0.0.1:8000";

const API_URL = window.location.protocol.startsWith("http")
    ? `${window.location.protocol}//${window.location.hostname}${window.location.port ? ":" + window.location.port : ""}`
    : FALLBACK_API_URL;

const FRONTEND_BASE_URL = `${API_URL}/frontend`;

document.addEventListener("DOMContentLoaded", () => {

    const profileBtn =
        document.getElementById("profileBtn");

    if (!profileBtn) return;


    profileBtn.addEventListener(
        "click",
        async (event) => {

            event.preventDefault();


            const token =
                localStorage.getItem(
                    "bengaltrail_token"
                );


            // ==================================
            // USER IS NOT LOGGED IN
            // ==================================

            if (!token) {

                window.location.href =
                    `${FRONTEND_BASE_URL}/auth.html`;

                return;
            }


            // ==================================
            // VERIFY TOKEN
            // ==================================

            try {

                const response =
                    await fetch(
                        "http://127.0.0.1:8000/api/check-auth",
                        {
                            method: "GET",

                            headers: {
                                "Authorization":
                                    `Bearer ${token}`
                            }
                        }
                    );


                // ==================================
                // TOKEN IS VALID
                // ==================================

                if (response.ok) {

                    window.location.href =
                        `${FRONTEND_BASE_URL}/profile.html`;

                    return;
                }


                // ==================================
                // TOKEN EXPIRED / INVALID
                // ==================================

                localStorage.removeItem(
                    "bengaltrail_token"
                );

                window.location.href =
                    "auth.html";


            } catch (error) {

                console.error(
                    "Authentication check failed:",
                    error
                );

            }

        }
    );

});