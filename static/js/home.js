// Wait until the DOM content is loaded
document.addEventListener("DOMContentLoaded", function() {
    let postsContainer = document.getElementById("blog-posts-list");
    let currentPosition = 0;
    let postWidth = 300; // Width of one post (adjust if needed)
    let posts = document.querySelectorAll(".col-md-4");
    let totalWidth = postWidth * posts.length; // Total width of all posts

    // Function to move the posts container
    function autoScroll() {
        if (currentPosition + postWidth >= totalWidth) {
            // Reset to the beginning if we've reached the end
            currentPosition = 0;
        } else {
            // Move the container by one post's width
            currentPosition += postWidth;
        }

        // Apply the new position with a smooth transition
        postsContainer.style.transform = `translateX(-${currentPosition}px)`;
    }

    // Scroll every 5 seconds
    setInterval(autoScroll, 5000);
});
