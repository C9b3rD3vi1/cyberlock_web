
document.addEventListener('DOMContentLoaded', function() {
    // Function to fade out and remove messages after 4.5 seconds
    const messages = document.querySelectorAll('.messages li');

    messages.forEach(function(message) {
        // Set a timeout for fading out
        setTimeout(function() {
            message.style.animation = 'fadeOut 1s forwards'; // Apply fade-out animation
        }, 4500);  // 4.5 seconds before fading out

        // Remove the message from the DOM after it fades out
        setTimeout(function() {
            message.remove();
        }, 5000);  // After 5.0 seconds (1 second after fade-out)
    });
});

// Password strength meter
document.addEventListener("DOMContentLoaded", function () {
    let passwordField = document.getElementById("id_password1");
    let strengthText = ["Very Weak", "Weak", "Fair", "Good", "Strong"];
    let strengthIndicator = document.getElementById("password-strength");

    passwordField.addEventListener("input", function () {
        let strength = zxcvbn(passwordField.value).score;
        strengthIndicator.textContent = "Password Strength: " + strengthText[strength];

        // Color feedback based on strength
        let colors = ["#ff0000", "#ff4500", "#ffa500", "#008000", "#006400"];
        strengthIndicator.style.color = colors[strength];
    });
});

// Username availability check
document.getElementById("id_username").addEventListener("input", function () {
    let username = this.value;
    if (username.length > 3) {
        fetch(`/check-username?username=${username}`)
            .then(response => response.json())
            .then(data => {
                let message = document.getElementById("username-check");
                if (data.available) {
                    message.textContent = "✅ Username available";
                    message.style.color = "green";
                } else {
                    message.textContent = "❌ Username taken";
                    message.style.color = "red";
                }
            });
    }
});
