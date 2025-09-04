document.addEventListener('DOMContentLoaded', () => {
    const depositBtn = document.getElementById('deposit-btn');
    const spinBtn = document.getElementById('spin-btn');
    const quitBtn = document.getElementById('quit-btn');
    
    // Simulating game state on the front end
    let balance = 0;
    
    // Function to update the balance display
    function updateBalance(newBalance) {
        balance = newBalance;
        document.getElementById('balance-display').textContent = `Current Balance: $${balance}`;
    }

    // Event listener for the Deposit button
    depositBtn.addEventListener('click', () => {
        const depositAmount = parseInt(document.getElementById('deposit-input').value);
        if (!isNaN(depositAmount) && depositAmount > 0) {
            updateBalance(balance + depositAmount);
            document.getElementById('message-area').textContent = `Deposited $${depositAmount}.`;
        } else {
            document.getElementById('message-area').textContent = "Please enter a valid deposit amount.";
        }
    });

    // Event listener for the Spin button
    spinBtn.addEventListener('click', () => {
        const lines = parseInt(document.getElementById('lines-input').value);
        const bet = parseInt(document.getElementById('bet-input').value);

        // Basic client-side validation
        if (isNaN(lines) || isNaN(bet) || lines < 1 || lines > 3 || bet < 1) {
            document.getElementById('message-area').textContent = "Please enter valid lines and bet.";
            return;
        }

        const totalBet = lines * bet;
        if (totalBet > balance) {
            document.getElementById('message-area').textContent = "You don't have enough balance.";
            return;
        }

        // In a real application, you would make a fetch() call to a Python server here
        // The server would run your logic and return the spin result, winnings, and new balance
        
        // Simulating the spin and winnings
        const simulatedWinnings = Math.floor(Math.random() * (totalBet * 3));
        const newBalance = balance - totalBet + simulatedWinnings;
        
        updateBalance(newBalance);
        document.getElementById('message-area').textContent = `You bet $${totalBet}. You won $${simulatedWinnings}!`;
    });

    // Event listener for the Quit button
    quitBtn.addEventListener('click', () => {
        document.getElementById('message-area').textContent = `Thanks for playing! Final balance: $${balance}`;
    });
});