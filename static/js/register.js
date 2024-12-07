
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
