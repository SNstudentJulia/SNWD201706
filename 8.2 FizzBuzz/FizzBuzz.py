answer = raw_input("Select a number between 1 and 100: ")
start = 0

try:
    if int(answer) >= 101:
        print "Please only enter valid numbers between 1 and 100."
    elif int(answer) == 0:
        print "Please only enter valid numbers between 1 and 100."
    else:
        number = int(answer)

        while True:
            start += 1

            if start > number:
                break
            elif (start % 3) + (start % 5) == 0:
                print "fizzbuzz"
            elif start % 3 == 0:
                print "fizz"
            elif start % 5 == 0:
                print "buzz"
            else:
                print start

except ValueError:
     print "Please only enter valid numbers."
