import random           #importiert das file aus der Python library

welcome_message = "welcome to the lottery number generator"
prompt = "Please enter how many random numbers you would like to have: "

random.sample(range(50),6)

def generate_numbers(amount):
    number_list = []
    while len(number_list)<amount:
    #for i in range(amount):
        new_number = random.randint (0,49)
        if new_number not in number_list:
            number_list.append(new_number)
    return sorted(number_list)       # wenn anstatt 'return' da 'pass' steht, printet es unten 'None'


print welcome_message
answer = raw_input(prompt)
try:
    answer = int(answer)
    print sorted(random.sample(range(1,50),answer))
    print "End"
except ValueError as e:
    print "Sorry, your input could not be parsed into a number."