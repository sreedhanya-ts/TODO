// Show the popup
  function showPopup(id) {
    document.getElementById(id).style.display = "flex";
  }

  // Hide the popup
  function hidePopup(id) {
    document.getElementById(id).style.display = "none";
  }

  // Hide popup if user clicks outside content box
  window.onclick = function(event) {
    ['loginPopup', 'signupPopup'].forEach(id => {
      const popup = document.getElementById(id);
      if (event.target == popup) {
        popup.style.display = "none";
      }
    });
  }
  // Close popup when escape key is pressed