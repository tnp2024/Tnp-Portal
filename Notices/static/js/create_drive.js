document.addEventListener('DOMContentLoaded', function () {
    const dropdownBtn = document.querySelector('.dropdown-btn');
    const cardBody = document.querySelector('.card-body');

    dropdownBtn.addEventListener('click', function () {
        if (cardBody.style.display === 'none' || cardBody.style.display === '') {
            cardBody.style.display = 'block';
        } else {
            cardBody.style.display = 'none';
        }
    });
});