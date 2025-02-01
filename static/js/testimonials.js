// Initialize Swiper Carousel with Auto-Scroll
const swiper = new Swiper('.swiper-container', {
    loop: true,
    autoplay: {
        delay: 4000, // Auto-scroll every 4 seconds
        disableOnInteraction: false, // Continue auto-scroll even after user interaction
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});

// Filter Testimonials by Rating
document.querySelectorAll('.filter-btn').forEach(button => {
    button.addEventListener('click', () => {
        const rating = button.getAttribute('data-filter');
        document.querySelectorAll('.testimonial').forEach(testimonial => {
            if (rating === 'all' || testimonial.getAttribute('data-rating') === rating) {
                testimonial.style.display = 'block';
            } else {
                testimonial.style.display = 'none';
            }
        });
    });
});