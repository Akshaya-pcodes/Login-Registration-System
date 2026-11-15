// =================================
// LOGIN & REGISTRATION PAGE SWITCH
// =================================

const loginPage = document.getElementById("loginPage");
const registerPage = document.getElementById("registerPage");

const showRegister = document.getElementById("showRegister");
const showLogin = document.getElementById("showLogin");

// Show Registration Page
showRegister.addEventListener("click", function(event) {

    event.preventDefault();

    loginPage.style.display = "none";
    registerPage.style.display = "block";

});

// Show Login Page
showLogin.addEventListener("click", function(event) {

    event.preventDefault();

    registerPage.style.display = "none";
    loginPage.style.display = "block";

});


// =================================
// REGISTRATION FORM
// =================================

const registerForm = document.getElementById("registerForm");

registerForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const name = document.getElementById("registerName").value;
    const email = document.getElementById("registerEmail").value;
    const password = document.getElementById("registerPassword").value;

    const message = document.getElementById("registerMessage");

    try {

        const response = await fetch("/api/register", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                name: name,
                email: email,
                password: password
            })

        });

        const result = await response.json();

        message.textContent = result.message || result.error;

        if (response.ok) {
            registerForm.reset();
        }

    } catch (error) {

        message.textContent = "Unable to connect to server";

    }

});


// =================================
// LOGIN FORM
// =================================

const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const email = document.getElementById("loginEmail").value;
    const password = document.getElementById("loginPassword").value;

    const message = document.getElementById("loginMessage");

    try {

        const response = await fetch("/api/login", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                email: email,
                password: password
            })

        });

        const result = await response.json();

        message.textContent = result.message || result.error;

        if (response.ok) {
            loginForm.reset();
        }

    } catch (error) {

        message.textContent = "Unable to connect to server";

    }

});