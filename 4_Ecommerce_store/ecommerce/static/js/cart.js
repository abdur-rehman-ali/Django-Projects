console.log("Welcome to cart");

// Targeting cart-button class 
let cart_buttons = document.getElementsByClassName("cart-button");


// Added click event on each button with class 'cart-button' 
for (let index = 0; index < cart_buttons.length; index++) {
  cart_buttons[index].addEventListener("click", function () {
    let product_id = cart_buttons[index].getAttribute("data-product");
    let action = cart_buttons[index].getAttribute("data-action");

    // current_user attribute is declared in main.html 
    if (current_user == "AnonymousUser") {
      console.log("User is not logged in");
    } else {
      cartButtonDataToBackend(product_id,action)
    }
  });
}

// This function will use fetch API to send data to backend
function cartButtonDataToBackend(product_id,action) {
    let data_to_sent ={
        'product_id':product_id,
        'action':action,
    }

    let url = '/updateItem/';

    fetch(url, {
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify(data_to_sent),
    })
    .then(response=>  response.json() )
    .then(data=>{
        // Reload page , every time new data gets added 
        location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    
}
