// Khalti payment function
function initiatePayment(event) {
    event.preventDefault(); // Prevent default form submission

    const form = event.target; // Get the form element

    const name = form.querySelector("#name").value;
    const phone = form.querySelector("#phone").value;
    const email = form.querySelector("#email").value;
    const amount = form.querySelector("#amount").value;

    fetch("/initiate_khalti_payment/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            phone: phone,
            email: email,
            amount: amount
        })
    })
        .then(response => response.json())
        .then(data => {
            // Handle the response data, e.g., redirect to the payment page
            console.log(data);
            // You might want to redirect the user to the payment page using data.redirect_url
        })
        .catch(error => {
            console.error("Error initiating payment:", error);
        });
}

// Look and feel function
function updateMembershipDetails() {
    const membershipType = document.getElementById('membership_type').textContent;
    const membershipDuration = document.getElementById('membership_duration').textContent;
    const money = document.getElementById('money');
    const amount = document.getElementById('amount');

    const membershipTypeElement = document.getElementById('membership_type');
    const membershipDurationElement = document.getElementById('membership_duration');

    if (membershipType === 'is_new') {
        membershipTypeElement.textContent = 'New Membership';
    } else if (membershipType === 'is_renew') {
        membershipTypeElement.textContent = 'Renew Membership';
    }

    if (membershipDuration === 'is_oneyear') {
        membershipDurationElement.textContent = 'One-Year Duration';
        money.textContent = 'Rs 150';
        amount.value = '15000';
    } else if (membershipDuration === 'is_fouryears') {
        membershipDurationElement.textContent = 'Four-Year Duration';
        money.textContent = 'Rs 500';
        amount.value = '50000';
    }
}

document.addEventListener("DOMContentLoaded", function () {
    updateMembershipDetails();

    const paymentGateways = document.querySelector(".payment_gateways");
    const cardsGateways = document.querySelector(".payment_cards");
    const banksGateways = document.querySelector(".payment_banks");

    const firstBox = document.getElementById("first-box");
    const secondBox = document.getElementById("second-box");
    const thirdBox = document.getElementById("third-box");
    const fourthBox = document.getElementById("fourth-box");

    const gatewayImages = paymentGateways.querySelectorAll("img");
    const bankImages = banksGateways.querySelectorAll("img");
    const cardsImages = cardsGateways.querySelectorAll("img");

    gatewayImages.forEach(image => {
        image.addEventListener("click", function () {
            secondBox.style.display = "flex";
            firstBox.style.display = "none";
        });
    });

    bankImages.forEach(image => {
        image.addEventListener("click", function () {
            thirdBox.style.display = "flex";
            firstBox.style.display = "none";
        });
    });

    cardsImages.forEach(image => {
        image.addEventListener("click", function () {
            fourthBox.style.display = "flex";
            firstBox.style.display = "none";
        });
    });
}); // root