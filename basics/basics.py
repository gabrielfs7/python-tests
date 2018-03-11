import pprint

'''
Show Python builtin functions
'''
# dir(__builtins__)

print(all([True, 1, True]))
print(bool('0').bit_length())


# this is a list
address = [
    'Flat Floor Street',
    '18',
    'New York'
]

print("The address is: " + address[0] + "," + address[1] + " " + address[2])
print("The address is: " + address[-3] + "," + address[-2] + " " + address[-1])
print(type(address))
print(type(address[0]))
pprint.pprint(address)

# This is a dictionary
pins = {
    "Mike": 1234,
    "Joe": 1111,
    "Jack": 2222
}

'''
While correct user is not provided and has more tries, can go: 
'''
number_of_tries = 0
is_correct_pin = False

while number_of_tries < 10 and not is_correct_pin:
    pin = int(input("Enter your pin: "))

    number_of_tries += 1

    if pin in pins.values():
        is_correct_pin = True
    elif number_of_tries == 10:
        print("Error: You exceeded the number of 10 tries!")
    else:
        print("Error: Pin " + str(pin) + " does not exist!")
        print("Access allowed only for: ")
        for pin_name in pins.keys():
            print("- " + pin_name)


def find_in_file(f):
    myfile = open("sample.txt")
    fruits = myfile.read()
    fruits = fruits.splitlines()
    if f in fruits:
        return True
    return False


'''
While correct fruit is not supplied and has number of tries, can go.
'''
number_of_tries = 0
is_correct_fruit = False

while number_of_tries < 10 and not is_correct_fruit:
    fruit = input("Enter fruit: ")

    number_of_tries += 1

    if find_in_file(fruit):
        print("The fruit [" + str(fruit) + "] is in the list.")
        is_correct_fruit = True
    elif number_of_tries == 10:
        print("Error: You exceeded the number of 10 tries")
    else:
        print("Error: No such fruit found!")
