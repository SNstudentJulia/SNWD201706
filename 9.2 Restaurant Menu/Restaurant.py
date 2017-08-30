print "The Daily Menu of My Restaurant"
print "*"*70

menu_dict = {}

while True:
    dish = raw_input("Please enter a daily dish: ")
    price = raw_input("What is the price of '%s'? " % dish)
    menu_dict[dish] = price
    print "Your new daily dish is: " + dish, "at " + price, "$"

    new = raw_input("Would you like to enter new dish? (yes/no) ")

    if new.lower() == "no":
        break

print "*"*70
print "The Daily Menu of My Restaurant:"

menu_file = open("menu.txt", "w+")
menu_file.write("Daily Dishes:\n")
for item in menu_dict:
    print "- " + item + ": " + menu_dict[item] + "$"
    menu_file.write("- " + "%s: %s$" % (item, menu_dict[item]) + "\n")

menu_file.write("\n")

menu_file.close()

print "END"