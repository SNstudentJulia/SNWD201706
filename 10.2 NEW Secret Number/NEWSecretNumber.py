import random

def main():
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


if __name__ == "__main__":
            main()