import time

def countdown_timer():
    try:
        user_input = input("Enter time in seconds: ")
        seconds = int(user_input)
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    while seconds > 0:
        print(f"Time left: {seconds}s", end="\r")
        time.sleep(1)
        seconds -= 1

    print("\nTIME IS UP! 🔔")

if __name__ == "__main__":
    countdown_timer()
