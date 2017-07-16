answer = raw_input("Select a number between 1 and 100: ")

try:
    if int(answer) >= 101:
        print "Please only enter valid numbers between 1 and 100."

    else:
        number = int(answer) - 1

        while True:
            number += 1

            if (number % 3) + (number % 5) == 0:
                print "fizzbuzz"
            elif number % 3 == 0:
                print "fizz"
            elif number % 5 == 0:
                print "buzz"
            elif number >= 101:
                break
            else:
                print number

except ValueError:
     print "Please only enter valid numbers."
