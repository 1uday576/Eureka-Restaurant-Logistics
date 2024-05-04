// Get the input element
const searchInput = document.getElementById("searchInput");

// Get all the card elements
const cards = document.querySelectorAll(".card");

// Add event listener for input changes
searchInput.addEventListener("input", function () {
  const searchTerm = searchInput.value.toLowerCase(); // Convert input value to lowercase for case-insensitive search

  // Loop through each card
  cards.forEach((card) => {
    const cardName = card.querySelector("h3").innerText.toLowerCase(); // Get the card name

    // Check if the card name includes the search term
    if (cardName.includes(searchTerm)) {
      card.style.display = "block"; // Show the card
    } else {
      card.style.display = "none"; // Hide the card
    }
  });
});
