

document.addEventListener('DOMContentLoaded', () => {
    // Array of colors for changing text color
    const colors = ['#4c6ef5', '#00c6ff', '#f54291']; // Array of colors for each string

    new Typed('.display-4', {
        strings: ['Welcome to Cyberlock Technologies Blog', 'Explore Our Latest Posts', 'Stay Updated!'],
        typeSpeed: 100, // Typing speed in milliseconds
        backSpeed: 30, // Backspacing speed in milliseconds
        loop: true,    // Loops through the strings
        showCursor: true, // Display typing cursor
        cursorChar: '|', // Character used as the cursor
        onStringTyped: (arrayPos) => {
            // Change color when each string finishes typing
            const element = document.querySelector('.display-4');
            element.style.color = colors[arrayPos % colors.length];
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.blog').classList.add('loaded');
});
