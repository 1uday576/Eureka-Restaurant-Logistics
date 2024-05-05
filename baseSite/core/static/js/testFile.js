async function getMealNames() {
  try {
    let response = await fetch("http://127.0.0.1:8000/mealsNames");
    let data = await response.json();
    print(data);
    // Select all elements with class "Burger-Card"
    let burgerCards = document.querySelectorAll(".Burger-Card");

    // Loop through each card and update its name
    burgerCards.forEach((card, index) => {
      // Update the name from the data received
      card.querySelector("h3").textContent = data.names[index];
      // Get the card name
      let name = card.closest(".card").dataset.name;
      // Call getCardInfo with the name
      getCardInfo(name);
      // Add click event listener to add item to cart
      card.closest(".card").addEventListener("click", () => {
        addItemToCart(name);
      });
    });
  } catch (error) {
    console.error("Error fetching meal names:", error);
  }
}

// Call getMealNames function when DOM content is loaded
document.addEventListener("DOMContentLoaded", function () {
  getMealNames();
});

async function getCardInfo(name) {
  try {
    let response = await fetch(`http://127.0.0.1:8000/cardInfo?Name=${name}`);
    let data = await response.json();
    console.log(data);

    // Find the card element with the matching name
    let card = document.querySelector(`[data-name="${name}"]`);

    if (card) {
      // Get the existing content of the paragraph
      let paragraph = card.querySelector(".Burger-Card p");

      // Update the content with received data
      paragraph.textContent = `Cost: $${data.cost}\nIngredients: `;

      // Check if data.list is an array
      if (Array.isArray(data.list)) {
        // Display the total count of ingredients
        paragraph.textContent += `(${data.list.length} ingredients)\n`;

        // Loop through each ingredient and append it to the paragraph
        data.list.forEach((ingredient, index) => {
          // Add comma and space if it's not the first ingredient
          if (index > 0) {
            paragraph.textContent += "\n"; // Add a newline character
          }
          // Append the ingredient
          paragraph.textContent += `${ingredient}`;
        });
      } else if (typeof data.list === "object") {
        // Display the ingredients as "item: amount" pairs
        paragraph.textContent += Object.entries(data.list)
          .map(([item, amount]) => `${item}: ${amount}`)
          .join("\n"); // Add a newline character between each pair
      } else {
        // If data.list is neither an array nor an object, simply append it to the paragraph
        paragraph.textContent += data.list;
      }
    } else {
      console.error("Card not found:", name);
    }
  } catch (error) {
    console.error("Error fetching card info:", error);
  }
}

function addItemToCart(name) {
  // Get the card element with the matching name
  let card = document.querySelector(`[data-name="${name}"]`);
  if (card) {
    // Get the name and price of the item
    let itemName = card.querySelector("h3").textContent;
    let itemPrice = card
      .querySelector(".Burger-Card p")
      .textContent.split("\n")[0]
      .replace("Cost: $", "");

    // Create a new item element
    let newItem = document.createElement("div");
    newItem.classList.add("item");
    newItem.innerHTML = `
        <div class="name">${itemName}</div>
        <div class="totalPrice">$${itemPrice}</div>
      `;

    // Add the new item to the cart
    let cartTab = document.querySelector(".cartTab .listChart");
    cartTab.appendChild(newItem);
  } else {
    console.error("Card not found:", name);
  }
}
function listStock() {
  return fetch("/list_stock") // Assuming the URL for the endpoint is '/list_stock'
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      // Extract names and amounts from the JSON response
      const names = data.names;
      const amounts = data.amount;

      // Return an object with names and amounts
      return { names, amounts };
    })
    .catch((error) => {
      console.error("Error fetching stock data:", error);
      // Return an empty object or handle the error as needed
      return {};
    });
}
