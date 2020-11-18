# Copyright Orel Rahum
# ID: 316423615
import os
import glob
import re
import enchant

begin_ascii_uppercase = 65
end_ascii_uppercase = 90
begin_ascii_lowercase = 97
end_ascii_lowercase = 122
# 1 its mean encrypted and 0 its mean uncrypted , 0 its mean Uncrypted
result = 0

# ENTER YOUR VAR HERE!
file_path = "E:\\Dropbox\\Orel\\Ariel University\\Final Project\\DATASET_MARGE\\Unencrypted"




# Second feature , will check how much word on start on Big CHAR/Small Char!

def feature2(word) -> bool:
    for c in range(1):
        if (begin_ascii_uppercase <= ord(word[0]) <= end_ascii_uppercase) or (
                begin_ascii_lowercase <= ord(word[0]) <= end_ascii_lowercase):
            return True
    return False


# Second feature , will check how much middle on word  with only Small Char!
def feature3(word) -> bool:
    for c in range(1, len(word) - 1):
        if not (begin_ascii_lowercase <= ord(word[c]) <= end_ascii_lowercase):
            return False
    return True


def feature4(word) -> bool:
    if word.isnumeric() or len(word) == 1 :
        return True
    return False


def feature5(word) -> bool:
    en_US = enchant.Dict("en_US")
    if en_US.check(word):
        return True
    return False


def create_file_result():
    with open("./DATASET.csv", "w+") as f:
        f.write("name of file ,feature 1 , feature 2 , feature 3 , feature 4 ,feature 5 , result\n")


def write_for_result(filename, feature1_count , feature2_count , feature3_count,
                     feature4_count , feature5_count , result):

    with open("./DATASET.csv", "a+") as f:
        f.write(filename + "," + str(feature1_count) + "," + str(feature2_count) + "," + str(feature3_count)
                + "," + str(feature4_count) + ","+ str(feature5_count) + "," + str(result) + "\n")



if __name__ == "__main__":
    count_files=0
    create_file_result()
    for filename in glob.glob(file_path + '\\**\\*.txt', recursive=True):
        # Read every file
        with open(filename, 'r') as file:
            filename = filename.replace(file_path + "\\", "")
            print("The File name is : " + filename +"The number checked file is :"+ str(count_files))
            feature1_count = 0
            feature2_count = 0
            feature3_count = 0
            feature4_count = 0
            feature5_count = 0
            for line in file.readlines():
                res = re.findall(r'\w+', line)
                for word in res:
                    feature1_count = feature1_count + 1

                    if feature2(word):
                        feature2_count = feature2_count+1

                    if feature3(word) :
                        feature3_count = feature3_count+1

                    if feature4(word):
                        feature4_count = feature4_count+1

                    if feature5(word):
                          feature5_count = feature4_count + 1



        write_for_result(filename, feature1_count, feature2_count, feature3_count, feature4_count ,feature5_count, result)
