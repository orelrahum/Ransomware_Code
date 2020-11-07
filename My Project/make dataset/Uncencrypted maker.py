# in this File we will make Unencrypted Text file
import random
global number_files
global name_file
if __name__ == "__main__":
    global number_files
    start_random = 15
    end_random = 920
    edit_file = "original files\\total.txt"  # Please enter here your file name
    num_of_lines = random.randint(start_random, end_random)
    num_total_lines = sum(1 for line in open(edit_file))
    number_files = 3844
    x = 0
    file = open(edit_file, "r")
    for lines in file.readlines():
        name_file = "output files\\ALL\\Unencrypted{}.txt ".format(number_files)
        if x < num_of_lines:
            write_file = open(name_file, "a+")
            write_file.write(lines)
            #print(lines)
            write_file.close()
        if x == num_of_lines:
            num_total_lines = num_total_lines - num_of_lines
            num_of_lines = random.randint(start_random , end_random)
            if num_total_lines <= num_of_lines:
                num_of_lines = num_total_lines
            number_files = number_files + 1
            x = 0
        x = x+1
    file.close()

