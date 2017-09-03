import random

def main():
    try:
        secret = random.randint(1, 5)
        while True:
            guess = int(raw_input("Guess the secret number 1 to 5: "))
            if guess == secret:
                print "Congratulations! You have won 1 Million Dollars!"
                break

            elif guess != secret:
                again = raw_input("Try again? (yes/no) ")
                if again.lower() in ("no", "n"):
                    print "Game Over"
                    break
        print "End"
    except ValueError as e:
        print "Please only guess numbers or you'll never win!"

if __name__ == "__main__":
            main()