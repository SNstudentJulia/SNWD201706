secret = 42
guess = raw_input ("Guess the secret number: ")

try:
    if int(guess) == secret:
        print "Congratulations! You have won 1 Million Dollars!"
    else:
        print "Sorry, try again!"

except ValueError as e:
     print "Please only guess numbers or you'll never win!"