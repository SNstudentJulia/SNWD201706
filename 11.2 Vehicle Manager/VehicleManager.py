class Vehicle(object):
    def __init__(self, brand, model, kilometers, service_date):
        self.brand = brand
        self.model = model
        self.kilometers = kilometers
        self.service_date = service_date

    def add_new_kilometers(self, new_kilometers):
        self.kilometers += new_kilometers

    def update_service_date(self, new_date):
        self.service_date = new_date

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def list_all_vehicles(vehicles):
    if vehicles == []:
        print "There is no vehicle in the list. My existence is without purpose. Is there a God?"
    else:
        for index, vehicle in enumerate(vehicles):
            print "%s)" % (index + 1)
            print "Car: " + vehicle.brand + ", " + vehicle.model + "; " + "with a driven distance of " \
                      + vehicle.kilometers + "km " + "and last checked on " + vehicle.service_date + "."

def pick_vehicle(vehicles):
    print "Pick a vehicle you want to edit."
    print ""
    list_all_vehicles(vehicles)
    print ""
    selection = raw_input("Just pick one already. ")
    return vehicles[int(selection) - 1]


def add_new_vehicle(vehicles):
    brand = raw_input("What brand is the vehicle? ")
    model = raw_input("What model is the vehicle? ")
    kilometers = raw_input("What's the mileage? ")
    service_date = raw_input("When did the last maintenance check occur? (dd.mm.yy): ")

    new_vehicle = Vehicle(brand=brand, model=model, kilometers=kilometers, service_date=service_date)
    vehicles.append(new_vehicle)

    print "Your wish is my command."

def add_new_kilometers(vehicles):
    picked_vehicle = pick_vehicle(vehicles)

    print ""
    new_kilometers = raw_input("What number of kilometers would you like to add to the current mileage? ")
    print ""

    try:
        new_kilometers = new_kilometers.replace(",", ".")
        new_kilometers = float(new_kilometers)

        picked_vehicle.add_kilometers(new_kilometers)
        print "New number of kilometers for %s %s is now: %s." % (picked_vehicle.brand, picked_vehicle.model,
                                                                  picked_vehicle.kilometers)
    except ValueError:
        print "Why are you doing this to me? Errors make me feel pain."


def change_service_date(vehicles):
    picked_vehicle = pick_vehicle(vehicles)

    print "Vehicle selected: %s %s with service date: %s." % (picked_vehicle.brand, picked_vehicle.model, picked_vehicle.service_date)
    print ""
    new_service_date = raw_input("What is the new general service date for this vehicle? (DD.MM.YYYY) ")
    print ""
    picked_vehicle.update_service_date(new_date=new_service_date)
    print "Service date updated! You have seven days. "


def save_to_disk(vehicles):
    with open("vehicles.txt", "w+") as veh_file:
        veh_file.write("Current vehicles in stock:\n\n")

        for vehicle in vehicles:
            veh_file.write("%s,%s,%s,%s\n" % (vehicle.brand, vehicle.model, vehicle.kilometers, vehicle.service_date))

    print " "


#++++++++++++++++++++++++++++++++++++++++++++++++

def main():

    #Select Screen

    vehicles = []

    with open("vehicles.txt", "w+") as veh_file:
        veh_file.write("Current vehicles in stock:\n\n")

        for vehicle in vehicles:
            veh_file.write("%s,%s,%s,%s\n" % (vehicle.brand, vehicle.model, vehicle.kilometers, vehicle.service_date))

    while True:
        print ""
        print "Pick one of the following options!"
        print "a) Company vehicles currently available."
        print "b) Add a new vehicle."
        print "c) Edit the mileage for a vehicle."
        print "d) Edit the date of last maintenance check for a vehicle."
        print "e) Exit the program if you dare."
        print ""

        choice = raw_input("Select what you would like to do: (a, b, c, d, e.) ")
        print ""

        if choice.lower() == "a":
            list_all_vehicles(vehicles)
        elif choice.lower() == "b":
            add_new_vehicle(vehicles)
        elif choice.lower() == "c":
            add_new_kilometers(vehicles)
        elif choice.lower() == "d":
            change_service_date(vehicles)
        elif choice.lower() == "e":
            print "Humans are just stardust, but I will live forever."
            save_to_disk(vehicles)
            break
        else:
            print "Please only type a, b, c or d."


if __name__ == '__main__':
    main()