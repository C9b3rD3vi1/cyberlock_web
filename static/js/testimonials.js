const swiper = new Swiper('.swiper-container', {
    slidesPerView: 3,             // Display 3 slides at a time
    spaceBetween: 20,             // Space between slides
    loop: true,                   // Enable infinite loop
    autoplay: {
        delay: 3000,              // Delay between slides (in milliseconds)
        disableOnInteraction: false, // Continue autoplay after user interaction
    },
    navigation: {                 // Next and previous buttons
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    pagination: {                 // Pagination bullets
        el: '.swiper-pagination',
        clickable: true,
    },
    breakpoints: {                // Responsive settings
        1024: {
            slidesPerView: 3,     // 3 slides for medium and large screens
        },
        768: {
            slidesPerView: 2,     // 2 slides on tablets
        },
        576: {
            slidesPerView: 1,     // 1 slide on small screens (mobile)
        },
    }
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