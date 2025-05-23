
document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.messages li');
    
    messages.forEach(function(message) {
        setTimeout(function() {
            message.style.opacity = '0';  // Begin fade-out
        }, 4000);  // 4.5 seconds before fading out
        
        setTimeout(function() {
            message.remove();  // Remove the message from the DOM after it fades
        }, 4500);  // After 5 seconds (fade-out duration)
    });
});
