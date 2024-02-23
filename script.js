document.getElementById('readMoreBtn').addEventListener('click', function() {
    var extraContent = document.getElementById('extraContent');
    if (extraContent.style.display === 'none' || extraContent.style.display === '') {
      extraContent.style.display = 'block'; // Show the extra content
      extraContent.parentNode.insertBefore(this, extraContent.nextSibling); // Move the button after the extra content
      this.textContent = 'Read Less'; // Optionally change button text to "Read Less"
    } else {
      extraContent.style.display = 'none'; // Hide the extra content
      extraContent.parentNode.insertBefore(this, extraContent); // Move the button back before the extra content
      this.textContent = 'Read More'; // Change button text back to "Read More"
    }
  });
  