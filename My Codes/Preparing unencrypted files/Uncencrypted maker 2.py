# in this File we will make Unencrypted Text file
import glob
import os
import random

global number_files
global name_file

# ADD all your VARS here
text_name = 'total.txt'
folder_output_name = 'total'
file_path = "E:\\Dropbox\\Orel\\Ariel University\\final Project\\DATASET 24.11\\Unencrypted"
output_path = "E:\\Dropbox\\Orel\\Ariel University\\final Project\\DATASET 24.11\\output\\"
start_random = 94
end_random = 241
number_files = 88923

if __name__ == "__main__":
    for filename in glob.glob(file_path + '\\**\\*.txt', recursive=True):
        # Read every file
        print(filename)
        try:
            with open(filename, 'r') as file:
                for lines in file.readlines():
                    pass
            num_total_lines = sum(1 for line in open(filename))
        except:
            print("prbolem file")
            os.remove(filename)

