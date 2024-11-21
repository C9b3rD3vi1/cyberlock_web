
    let posts = document.querySelectorAll(".blog-post");
    let currentPostIndex = 0;

    function autoScroll() {
        if (currentPostIndex < posts.length) {
            posts[currentPostIndex].scrollIntoView({ behavior: "smooth", block: "center" });
            currentPostIndex++;
        } else {
            currentPostIndex = 0; // Reset to the first post
        }
    }

    setInterval(autoScroll, 5000); // Scroll every 5 seconds