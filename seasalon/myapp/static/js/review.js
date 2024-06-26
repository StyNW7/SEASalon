// script.js

const reviewForm = document.getElementById('review-form');
const reviewList = document.getElementById('review-list');

reviewForm.addEventListener('submit', function(event) {
    event.preventDefault();
    
    const customerName = document.getElementById('customer-name').value;
    const starRating = document.getElementById('star-rating').value;
    const comment = document.getElementById('comment').value;

    if (!customerName || !starRating || !comment) {
        alert('Please fill in all fields.');
        return;
    }

    const reviewItem = document.createElement('div');
    reviewItem.classList.add('review-item');
    reviewItem.innerHTML = `
        <h3>${customerName}</h3>
        <p><strong>Rating:</strong> ${starRating} stars</p>
        <p><strong>Comment:</strong> ${comment}</p>
    `;

    reviewList.appendChild(reviewItem);

    // Reset form fields after submission
    reviewForm.reset();
});
