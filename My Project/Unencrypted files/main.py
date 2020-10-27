# in this File we will make Unencrypted Text file
import random
global number_files
global name_file


def create_file():
    global name_file
    name_file = "output files\\Unencrypted{}.txt ".format(number_files)
    write_file = open(name_file, "w+")
    write_file.close()


if __name__ == "__main__":
    total = 0
    edit_file = "Big files to edit\\alice29.txt"  # Please enter here your file name
    num_of_lines = random.randint(50, 100)
    print(num_of_lines)
    num_total_lines = sum(1 for line in open(edit_file))
    print(num_total_lines)
    global number_files
    number_files = 1
    x = 0
    file = open(edit_file, "r")
    for lines in file:
        create_file()
        if x < num_of_lines:
            write_file = open(name_file, "a+")
            write_file.write(lines)
        if x == num_of_lines:
            num_total_lines = num_total_lines - num_of_lines
            num_of_lines = random.randint(50, 100)
            total = total+num_of_lines
            print(total)
            if num_total_lines <= num_of_lines:
                num_of_lines = num_total_lines
            number_files = number_files + 1
            x = 0
        x = x + 1
    file.close()

