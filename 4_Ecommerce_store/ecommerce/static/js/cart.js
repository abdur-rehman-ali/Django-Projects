console.log('Welcome to cart');

let cart_buttons = document.getElementsByClassName('cart-button');


for (let index = 0; index < cart_buttons.length; index++) {
    cart_buttons[index].addEventListener('click', function(){
        let product = cart_buttons[index].getAttribute('data-product');
        let action = cart_buttons[index].getAttribute('data-action');
    });
    
}

