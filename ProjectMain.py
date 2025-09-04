import random
import time
import os

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def clear_screen():
    # Clears the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def spin_animation(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    for i in range(15):  # Number of animation frames
        clear_screen()
        temp_columns = []
        for _ in range(cols):
            column = random.choices(all_symbols, k=rows)
            temp_columns.append(column)
        print_slotMachine(temp_columns)
        time.sleep(0.05)
    clear_screen()

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        is_winning_line = True
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                is_winning_line = False
                break
        if is_winning_line:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slotMachine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        all_symbols.extend([symbol] * symbol_count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = list(all_symbols)
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            print(column[row], end=" | " if i != len(columns) - 1 else "")
        print()

def deposit():
    while True:
        amount = input("Enter your Deposit Amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("Enter your Betting Amount on each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance. Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}.")
    
    spin_animation(ROWS, COLS, symbol_count)
    
    final_slots = get_slotMachine_spin(ROWS, COLS, symbol_count)
    print_slotMachine(final_slots)

    winnings, winning_lines = check_winnings(final_slots, lines, bet, symbol_value)
    
    if winnings > 0:
        print(f"You won ${winnings}!")
        print(f"You won on line(s): {', '.join(map(str, winning_lines))}")
    else:
        print("You lost this round.")

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"\nYour current balance is ${balance}.")
        if balance <= 0:
            print("You have run out of money!")
            break

        play = input("Press Enter to spin (q to quit): ")
        if play.lower() == "q":
            break
        
        balance += spin(balance) # This line is correct. The problem is not here.

main()