print "*"*30
print "Hello there! This program will help you convert kilometers into miles!"
print "*"*30

while True:

    try:
        convert = raw_input("Please enter the kilometers you want to convert here: ")
        convert = float(convert)
        miles = convert * 0.621
        print convert, "kilometers equal", miles, "miles."
        print "*" * 30
    except ValueError:
        print "*"*30
        print "Please only use valid numbers!"

    choice = raw_input("Do you want to convert a new number? Yes/No ")
    if choice == str("Yes") or choice == str("Y") or choice == str("y") or choice == str("yes"):
        print "Wonderful!"
        print "*" * 30
    elif choice == str("No") or choice == str("N") or choice == str("n") or choice == str("no"):
        print "Thank you for your time. This program will now terminate. Goodbye!"
        print "*" * 30
        break
    else:
        print "Your entry is invalid. This program will now terminate. Goodbye!"
        print "*" * 30
        break