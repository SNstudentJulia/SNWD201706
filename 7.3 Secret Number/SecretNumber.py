secret = 42
guess = int(raw_input ("Guess the secret number: "))

if guess == secret:
    print "Congratulations! You have won 1 Million Dollars!"
else:
    print "Sorry, try again!"