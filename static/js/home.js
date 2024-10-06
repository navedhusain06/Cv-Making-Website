document.addEventListener('DOMContentLoaded', function() {
    const coverLetterLink = document.getElementById('coverLetterLink');
    const highlightLine = document.getElementById('highlightLine');

    // Check if the cover letter link has been clicked
    coverLetterLink.addEventListener('click', function() {
        coverLetterLink.classList.add('active');
        highlightLine.classList.add('active');
    });
    
    // If user navigates to a new template, remove the 'active' class (you need to implement navigation detection logic here)
    // Example for navigation detection:
    window.addEventListener('popstate', function() {
        coverLetterLink.classList.remove('active');
        highlightLine.classList.remove('active');
    });
});
