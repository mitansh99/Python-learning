import random  # For generating random numbers

# List of emojis used in the wheel
emojis = ["🎮", "🕹️", "🏆", "💥", "👾"]

# Function to spin the wheel and return 3 random emojis
def spin_wheel():
    wheel_result = [random.choice(emojis) for _ in range(3)]
    print(f"\n{wheel_result}\n")
    return wheel_result

# Function to calculate balance change based on wheel result and bid amount
def calculate_balance(wheel_result, bid_amount):
    # Win if all three emojis are the same
    if wheel_result[0] == wheel_result[1] == wheel_result[2]:
        return bid_amount * 10
    # Lose the bid amount otherwise
    return -bid_amount

def main():
    current_balance = 100
    print("\n---------- Welcome to Fun Arcade ----------\n")

    while current_balance > 0:
        print(f"Current Balance: {current_balance}")

        # Get bid amount from user
        bid_amount = input("Bid Amount: ")
        if not (bid_amount.isdigit() and int(bid_amount) <= current_balance and int(bid_amount) > 0):
            print("Enter a valid number or check your balance.")
            continue

        # Ask user to spin the wheel
        start_flag = input("Spin the wheel? (y/n): ").strip().lower()
        if start_flag != "y":
            print("Spin cancelled. Exiting game.")
            break

        # Spin the wheel and update balance
        wheel_result = spin_wheel()
        current_balance += calculate_balance(wheel_result, int(bid_amount))

    print("Game over! Your balance is 0.")

if __name__ == "__main__":
    main()
