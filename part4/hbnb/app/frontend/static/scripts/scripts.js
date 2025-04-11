/* 
  Implements login, place listing, place details and
  review forms 
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
        const token = checkAuthentication();
        fetchPlaces(token);
        setupFilter();
    }

    // Place details
    const placeDetails = document.getElementById('place-details');
    if (placeDetails) {
        const token = getCookie('token');
        const placeId = getPlaceIdFromURL();
        if (token) {
          const loginLink = document.getElementById('login-link');
          const reviewSection = document.getElementById('add-review');
          if (loginLink) loginLink.style.display = 'none';
          if (reviewSection) reviewSection.style.display = 'block';
        }
        fetchPlaceDetails(token, placeId);
    }

    // add-review form
    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        const token = checkAuthentication();
        const placeId = getPlaceIdFromURL;
        if (!placeId) {
            window.location.href = 'index.html'
        }
        reviewForm.addEventListener('submit', (event) =>
            handleReviewSubmit(event, token, placeId)
        );
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

  /* handlers */

  async function handleLogin(event) {
    event.preventDefault();

    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const error = document.getElementById('login-error');

    try {
        const res = await fetch('http://127.0.0.1:5000/api/v1/login', {
          method: 'POST'
          headers: {'Content-Type': 'aplication/json'},
          body: JSON.stringify({email, password})
        });

        if (res.ok) {
            const data = await res.json();
            document.cookie = `token=${data.access_token}; path=/; SameSite=Lax`;
            window.location.href = 'index.html';
        } else {
            const msg = await res.text();
            error.textContent = 'Login failed: ' + msg;
        }
      } catch (err) {
        error.textContent = 'An error occured. Try again.';
      }
  }

  async function fetchPlaces(token) {
    const res = await fetch('http://127.0.0.1:5000/api/v1/places', {
      headers: token ? { Authorization: `Bearer ${token}` } : {}
    });
    const places = await res.json();
    displayPlaces(places);
  }
  
  function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
  }

  async function fetchPlaceDetails(token, placeId) {
    if (!placeId) return;
    const res = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
      headers: token ? { Authorization: `Bearer ${token}` } : {} 
    });
    const place = await res.json();
    displayPlaceDetails(place);
  }

  function displayPlaceDetails(place) {
    const container = document.getElementById('place-details');
    container.innerHTML = `
      <div class="place-info">
        <h2>${place.name}</h2>
        <p><strong>Price:</strong> $${place.price}</p>
        <p><strong>Description:</strong> ${place.description}</p>
        <p><strong>Amenities:</strong> ${place.amenities.join(', ')}</p>
        <h3>Reviews:</h3>
      </div>
    `;
  
    const reviews = place.reviews || [];
    reviews.forEach((review) => {
      const reviewEl = document.createElement('div');
      reviewEl.className = 'review-card';
      reviewEl.innerHTML = `
        <p>${review.comment}</p>
        <p><strong>- ${review.user}</strong></p>
        <p>Rating: ${review.rating}/5</p>
      `;
      container.appendChild(reviewEl);
    });
  }
  
  async function handleReviewSubmit(event, token, placeId) {
    event.preventDefault();
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
    return await fetch('https://http://127.0.0.1:5000/api/v1//reviews', {
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
