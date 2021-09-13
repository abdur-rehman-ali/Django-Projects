console.log("Welcome to cart");

// Targeting cart-button class 
let cart_buttons = document.getElementsByClassName("cart-button");


// Added click event on each button with class 'cart-button' 
for (let index = 0; index < cart_buttons.length; index++) {
  cart_buttons[index].addEventListener("click", function () {
    let product = cart_buttons[index].getAttribute("data-product");
    let action = cart_buttons[index].getAttribute("data-action");

    // current_user attribute is declared in main.html 
    if (current_user == "AnonymousUser") {
      console.log("User is not logged in");
    } else {
      console.log("User is logged in");
    }
  });
}
