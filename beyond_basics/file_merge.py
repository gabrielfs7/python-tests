import os
import glob2

"""
Merge 3 files in one
"""
with open("files_merged.txt", "w") as merged_file:
    for file_path in glob2.glob("file*.txt"):
        with open(file_path, 'r') as my_file:
            merged_file.write(my_file.read() + "\n")


temperatures = [10, -20, -289, 100]

"""
Write temperature conversion to file
"""
def c_to_f(c):
    if c >= -273.15:
        return c * 9 / 5 + 32

with open("temperatures.txt", "w") as my_file:
    for t in temperatures:
        temperature = c_to_f(t)

        if type(temperature) == int or type(temperature) == float:
            my_file.write(str(temperature) + "\n")

"""
List specific files
"""
current_files = glob2.glob('*.txt')

for file in current_files:
    print("File %s " % file)


"""
Using 'with' context:

This way, there is no need to call my_file.close()
It is better, cause if Python script breaks, the file will not remain open. 
"""
with open("example.txt", "w") as my_file:
    my_file.write("Something\n")
    my_file.write("Something else\n")

with open("example.txt", "r") as my_file:
    for line in my_file.read().splitlines():
        print("Line written: %s " % line)