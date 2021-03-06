import pprint

'''
Show Python builtin functions
'''
# dir(__builtins__)

print(all([True, 1, True]))
print(bool('0').bit_length())

'''
Create new file and insert content
'''
file_name = 'test-file.txt'
file = open(file_name, 'w')

numbers_list = [1, 2, 3]

for i in numbers_list:
    file.write(str(i) + "\n")

file.close()


'''
Edit existent file, by adding new content. (Open as: append and read mode)
'''
file = open(file_name, 'a+')
file.read()
file.seek(1)
file.write(str(2.5))
file.close()

'''
Reading file content
'''
file = open(file_name, 'r')
file_lines = file.read().splitlines()

for line in file_lines:
    print(file_name + " line: " + line)

'''
Open the file and show the fruits inside
'''
def read_fruit_file():
    file = open('fruits.txt')
    print('Opened file type: ' + str(type(file)))
    file_content = file.read()

    print("\n")

    for fruit in file_content.splitlines():
        print(fruit + ' has length of ' + str(len(fruit)))

    print("\n")

    file.close()


read_fruit_file();


'''
Convert Celcius degrees to Fahrenheit

Formula: F = C × 9/5 + 32.
'''
def celcius_to_fahrenheit(celcious):
    if type(celcious) != int and type(celcious) != float:
        print('The celcius attribute should be a number')

        return 0

    if celcious < -273.15:
        print('The minimum temperature that physical can reach is -273.15 ºC')

        return 0

    fahrenheit = celcious * 9 / 5 + 32

    return fahrenheit


temperatures = [10, -20, -289, 100]

for temperature in temperatures:
    print(celcius_to_fahrenheit(temperature))

print('35 celcius degrees is the same that ' + str(celcius_to_fahrenheit(35)) + ' fahrenheit degrees')


# this is a list
address = ['Flat Floor Street', '18', 'I will be removed']
address.pop(2)
address.append('New York')

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
This is a tuple. Tuples are immutable! 

You cannot do, for instance customer.append('Test')
'''
customer = ("John", 28, "Luxembourg")

print(type(customer))

print(
    "Customer name: ", customer[0],
    ". Age: ", customer[1],
    ". Address: ", customer[2]
)


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
