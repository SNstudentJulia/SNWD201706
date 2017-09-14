import random           #importiert das file aus der Python library

welcome_message = "welcome to the lottery number generator"
prompt = "Please enter how many random numbers you would like to have: "

def generate_numbers(amount):
    number_list = []
    while len(number_list)<amount:
    #for i in range(amount):
        new_number = random.randint (0,49)
        if new_number in number_list:
            continue    #springt an den Anfang der Schleife zuruck, aber ohne einen Amount dazuzufugen
        number_list.append(new_number)
    return sorted(number_list)       # wenn anstatt 'return' da 'pass' steht, printet es unten 'None'


print welcome_message
answer = raw_input(prompt)
try:
    answer = int(answer)
    print generate_numbers(answer)
    print "End"
except ValueError as e:
    print "Sorry, your input could not be parsed into a number."