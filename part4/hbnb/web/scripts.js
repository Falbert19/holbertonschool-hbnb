/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
    // Login form submission
    const loginform = document.getElementById('login-form');
    if (loginform) {
        loginform.addEventListener('submit', handleLogin);
    }

    // fetching and display places
    const placeList = document.getElementById('place-list');
    if (placeList) {
        checkAuthentication();
        setupFilter();
    }

    // add-review form
    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        reviewForm.addEventListener('submit', handleReviewSubmit);
    }
  });

// Run after DOMContentLoaded block

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
  }
  
  function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');
    const addReviewSection = document.getElementById('add-review');
  
    if (!token) {
      if (addReviewSection) {
        addReviewSection.style.display = 'none';
      }
      if (loginLink) {
        loginLink.style.display = 'block';
      }
    } else {
      if (addReviewSection) {
        addReviewSection.style.display = 'block';
      }
      if (loginLink) {
        loginLink.style.display = 'none';
      }
    }
  
    return token;
  }
  
  function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
  }
  
  async function handleReviewSubmit(event) {
    event.preventDefault();
  
    const token = getCookie('token');
    if (!token) {
      window.location.href = 'index.html';
      return;
    }
  
    const placeId = getPlaceIdFromURL();
    const reviewText = document.getElementById('review').value.trim();
    const rating = document.getElementById('rating').value;
    const message = document.getElementById('review-message');
  
    if (!placeId || !reviewText || !rating) {
      if (message) {
        message.style.color = 'red';
        message.textContent = 'All fields are required.';
      }
      return;
    }
  
    try {
      const response = await submitReview(token, placeId, reviewText, rating);
  
      if (response.ok) {
        if (message) {
          message.style.color = 'green';
          message.textContent = 'Review submitted successfully!';
        }
        event.target.reset();
      } else {
        const errorText = await response.text();
        if (message) {
          message.style.color = 'red';
          message.textContent = 'Error: ' + errorText;
        }
      }
    } catch (err) {
      console.error(err);
      if (message) {
        message.style.color = 'red';
        message.textContent = 'Something went wrong. Try again.';
      }
    }
  }
  
  async function submitReview(token, placeId, comment, rating) {
    return await fetch('https://your-api-url/reviews', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        place_id: placeId,
        comment: comment,
        rating: parseInt(rating)
      })
    });
  }
  