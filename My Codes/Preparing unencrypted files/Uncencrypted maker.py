# in this File we will make Unencrypted Text file
import random

global number_files
global name_file

# ADD all your VARS here
text_name = 'Just ASCII.txt'
folder_output_name = 'Just ASCII'
file_path = "E:\\Dropbox\\Orel\\Ariel University\\final Project\\gish\\Texts Backup\\" + text_name
output_path = "E:\\Dropbox\\Orel\\Ariel University\\final Project\\DATASET\\" + folder_output_name + "\\Unencrypted"
start_random = 94
end_random = 1550
number_files = 9976

if __name__ == "__main__":
    num_of_lines = random.randint(start_random, end_random)
    num_total_lines = sum(1 for line in open(file_path))
    x = 0
    final_text = ""
    file = open(file_path, "r")
    for lines in file.readlines():
        if x < num_of_lines:
            final_text = final_text + lines + "\n"
            #print(lines)
        if x == num_of_lines:
            name_file = output_path + "\\Unencrypted{}.txt ".format(number_files)
            write_file = open(name_file, "a+")
            write_file.write(final_text)
            write_file.close()
            num_total_lines = num_total_lines - num_of_lines
            num_of_lines = random.randint(start_random, end_random)
            if num_total_lines <= num_of_lines:
                num_of_lines = num_total_lines
            number_files = number_files + 1
            x = 0
            final_text = ""
        x = x + 1
    file.close()
