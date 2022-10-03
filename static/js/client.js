var stripe = Stripe('pk_test_51Loj3zGcmIEJkd8GkvF5TVTbygrzhW1B1zhnnNqz4kTcMRc9D4NtFBLc3EppKvjzq5KqOqRSyEmhFJo44sgpidma00N7Dbbdrv');
var elements = stripe.elements();

var style = {

  theme: 'stripe',

  variables: {
    colorPrimary: '#0570de',
    colorBackground: '#ffffff',
    colorText: '#30313d',
    colorDanger: '#df1b41',
    fontFamily: 'Ideal Sans, system-ui, sans-serif',
    spacingUnit: '2px',
    borderRadius: '4px',
    // See all possible variables below
  }
  
};
  
  // Create an instance of the card Element.
var card = elements.create('card', {style: style});
  
  // Add an instance of the card Element into the `card-element` <div>.
  card.mount('#card-element');


var form = document.getElementById('payment-form');
  form.addEventListener('submit', function(event) {
    event.preventDefault();
  
    stripe.createToken(card).then(function(result) {
      if (result.error) {
        // Inform the customer that there was an error.
        var errorElement = document.getElementById('card-errors');
        errorElement.textContent = result.error.message;
      } else {
        // Send the token to your server.
        stripeTokenHandler(result.token);
      }
    });
  });

function stripeTokenHandler(token) {
    // Insert the token ID into the form so it gets submitted to the server
    var form = document.getElementById('payment-form');
    var hiddenInput = document.createElement('input');
    hiddenInput.setAttribute('type', 'hidden');
    hiddenInput.setAttribute('name', 'stripeToken');
    hiddenInput.setAttribute('value', token.id);
    form.appendChild(hiddenInput);
  
    // Submit the form
    form.submit();
  }