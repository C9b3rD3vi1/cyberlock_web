// Initialize Swiper Carousel
const swiper = new Swiper('.swiper-container', {
    loop: true,
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