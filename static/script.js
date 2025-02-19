// Function to handle currency conversion
function convertCurrency() {
    let fromCurrency = document.getElementById("fromCurrency").value;
    let toCurrency = document.getElementById("toCurrency").value;
    let amount = document.getElementById("amount").value;
    let resultText = document.getElementById("result");

    // Validate input
    if (!amount || amount <= 0) {
        resultText.innerText = "Please enter a valid amount.";
        resultText.style.color = "red";
        return;
    }

    // Fetch API data
    fetch(`/convert?from=${fromCurrency}&to=${toCurrency}&amount=${amount}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultText.innerText = "Error: " + data.error;
                resultText.style.color = "red";
            } else {
                resultText.innerText = 
                    `${data.amount} ${data.from} = ${data.converted_amount} ${data.to}`;
                resultText.style.color = "#0072ff";
            }
        })
        .catch(error => {
            resultText.innerText = "Conversion failed.";
            resultText.style.color = "red";
        });
}
