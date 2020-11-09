# in this File we will make Unencrypted Text file
import random

global number_files
global name_file

# ADD all your VARS here
file_path = "E:\\Dropbox\\Orel\\Ariel University\\פרוייקט גמר\\help files\\total - with part of symbols.txt"  # Please enter here your file name
output_path = "C:\\Users\\orelr\Desktop\\New folder"
start_random = 15
end_random = 43
number_files = 1

if __name__ == "__main__":
    num_of_lines = random.randint(start_random, end_random)
    num_total_lines = sum(1 for line in open(file_path))
    x = 0
    file = open(file_path, "r")
    for lines in file.readlines():
        if x < num_of_lines:
            name_file = output_path + "\\Unencrypted{}.txt ".format(number_files)
            write_file = open(name_file, "a+")
            write_file.write(lines)
            # print(lines)
            write_file.close()
        if x == num_of_lines:
            num_total_lines = num_total_lines - num_of_lines
            num_of_lines = random.randint(start_random, end_random)
            if num_total_lines <= num_of_lines:
                num_of_lines = num_total_lines
            number_files = number_files + 1
            x = 0
        x = x + 1
    file.close()
