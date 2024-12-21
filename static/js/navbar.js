document.addEventListener('DOMContentLoaded', () => {
    const toggler = document.querySelector('.navbar-toggler');
    const menu = document.querySelector('.navbar-menu');

    toggler.addEventListener('click', () => {
        menu.classList.toggle('show');
    });
});
