// JavaScript to detect scroll and add 'visible' class
const cards = document.querySelectorAll('.card');
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, { threshold: 0.3 }); // Add class when 30% of the card is visible

cards.forEach(card => observer.observe(card));
