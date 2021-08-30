# Copyright Orel Rahum
import os
import glob
import random
import re


#ENTER YOUR VAR HERE!
file_path = "E:\\Dropbox\\Orel\\Ariel University\\final Project\\DATASET\\Just ASCII\\Encrypted\\Caesar"
output_path = "E:\\Dropbox\\Orel\\Ariel University\\final Project\\DATASET\\Just ASCII\\Encrypted"


# First, scan (monitoring) the current folder ./ , watching for all changes appearing on .txt files only.
# Once triggered, i.e, a text file is changed, an algorithm to determine how likely an encryption happened
# in the txt file has occurred will be run.
# The result, for each change in text file, will be printed into the command line.

# First feature , will check if its template for real word!
def realWordOrNum (word) -> bool:
    begin_ascii_uppercase = 65
    end_ascii_uppercase = 90
    begin_ascii_lowercase = 97
    end_ascii_lowercase = 122
    if word.isnumeric():
        return True
    if len(word) == 1:
        return True
    for c in range(1):
        if not (begin_ascii_uppercase <= c <= end_ascii_uppercase) and (
                begin_ascii_lowercase <= c <= end_ascii_lowercase):
            return False
    for c in range(1, len(word) - 1):
        if not (begin_ascii_lowercase <= ord(word[c]) <= end_ascii_lowercase):
            return False
    return True


def create_file_result():
    with open("./results.csv", "w+") as f:
        f.write("name of file , result\n")


def write_for_result(file_name , result):
    with open("./results.csv", "a+") as f:
        f.write(file_name + "," + str(result) +"\n")


if __name__ == "__main__":
    create_file_result()
    print("Started Monitoring..")
    for filename in glob.glob(file_path + '\\*.txt'):
        # Read every file
        num_total_lines = sum(1 for line in open(filename))
        precent_of_encypt_line = random.randint(1, 100)
        final_text = ""
        with open(filename, 'r') as file:
            count = 0
            for line in file.readlines():
                res = re.findall(r'\w+', line)
                for word in res :
                    #print(word)
                    if not realWordOrNum(word):
                        count = count+1


        # Saving the file with a formated name,
        result = True
        if count > 100:
            result = False
        filename = filename.replace(file_path + "\\", "")
        write_for_result(filename, result)

