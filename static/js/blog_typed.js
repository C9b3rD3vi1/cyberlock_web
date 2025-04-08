document.addEventListener('DOMContentLoaded', () => {
    // Typing sound setup
    const typingSound = new Audio("{% static 'graphics/typing-keyboard-sound.mp3' %}");  // Make sure the path is correct
    
    // Array of colors for each sentence
    const colors = ['#4c6ef5', '#00c6ff', '#f54291'];

    // Initialize Typed.js
    const typed = new Typed('.display-4', {
        strings: ['Welcome to Our Blog', 'Explore Our Latest Posts', 'Stay Updated!'],
        typeSpeed: 100,   // Speed of typing
        backSpeed: 30,    // Speed of backspacing
        backDelay: 1000,  // Delay before backspacing starts
        startDelay: 500,  // Delay before typing starts
        loop: true,       // Loop the typing effect
        showCursor: true, // Show typing cursor
        cursorChar: '|',  // Set the cursor character

        // Play typing sound when a character is typed
        preStringTyped: function(pos, self) {
            typingSound.play();
        },

        // Change color when each string finishes typing
        onStringTyped: (arrayPos) => {
            const element = document.querySelector('.display-4');
            element.style.color = colors[arrayPos % colors.length];
        },

        onComplete: (self) => {
            self.start();
        }
    });
});
