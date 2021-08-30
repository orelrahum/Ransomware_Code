# Copyright Orel Rahum
import os
import glob
import re
import enchant
from random import randint

# ENTER YOUR VAR HERE!
# file type is Encrypted or Unencrypted
#file_type = "Encrypted"
file_type = "Unencrypted"


#ASCII_type ="all ASCII"
#ASCII_type ="only english chars"
#ASCII_type ="only english chars + numbers"

file_path = "E:\\Dropbox\\Orel\\Ariel University\\final Project\\DATASET_Small\\" + file_type
ouptup_csv = "./DATASET_ChecckAllWord.csv"
# 1 its mean encrypted and 0 its mean uncrypted , 0 its mean Uncrypted
if file_type == "Unencrypted":
    result = 0
if file_type == "Encrypted":
    result = 1


begin_ascii_uppercase = 65
end_ascii_uppercase = 90
begin_ascii_lowercase = 97
end_ascii_lowercase = 122
commonWords = ["the","of","and","a","to","in","is","you","that","it","he","was","for","on","are","as","with","his"
    ,"they","I","at","be","this","have","from","or","one","had","by","word","but","not","what","all","were","we","when"
    ,"your","can","said","there","use","an","each","which","she","do","how","their","if","will","up","other","about"
    ,"out","many","then","them","these","so","some","her","would","make","like","him","into","time","has","look","two"
    ,"more","write","go","see","number","no","way","could","people","my","than","first","water","been","call","who","oil"
    ,"its","now","find","long","down","day","did","get","come","made","may","part"]


# Second feature , will check how much word on start on Big CHAR/Small Char! + if its number + if its only 1 char|


def feature2(word) -> bool:
    if (begin_ascii_uppercase <= ord(word[0]) <= end_ascii_uppercase):
        return True
    if not (begin_ascii_lowercase <= ord(word[0]) <= end_ascii_lowercase):
        return True
    return False

# third feature , check spam word!!
def feature3(word) -> bool:
    if len(word) > 8 :
        return True
    for c in range(2, len(word) - 1):
        if  (begin_ascii_uppercase <= ord(word[c]) <= end_ascii_uppercase):
            return True
    for c in range(2, len(word) - 1):
        if not (begin_ascii_lowercase <= ord(word[c]) <= end_ascii_lowercase):
            return True
    return False



#check if its real word
def feature4(word) -> bool:
    for commonWord in commonWords :
        if word == commonWord:
            return True
    return False

#check if its real word
def feature5(word) -> bool:
    en_US = enchant.Dict("en_US")
    if en_US.check(word):
        return True
    return False

def create_file_result():
    with open(ouptup_csv, "w+") as f:
        f.write("name of file ,feature 1 , feature 2 , feature 3 , feature 4, feature 5, feature 6, result\n")


def write_for_result(filename, feature1_count , feature2_count , feature3_count,
                     feature4_count ,feature5_count ,feature6_count , result):

    with open(ouptup_csv, "a+") as f:
        f.write(filename + "," + str(feature1_count) + "," + str(feature2_count) + "," + str(feature3_count)
                + "," + str(feature4_count)  + "," +str(feature5_count)  + ","+str(feature6_count) + "," + str(result) + "\n")



if __name__ == "__main__":
    count_files=0
    if not os.path.isfile(ouptup_csv):
        create_file_result()
    for filename in glob.glob(file_path + '\\*.txt', recursive=True):
        # Read every file
        with open(filename, 'r') as file:
            filename = filename.replace(file_path + "\\", "")
            print("The File name is : " + filename +"The number checked file is :"+ str(count_files))
            count_files = count_files+1
            feature1_count = 0
            feature2_count = 0
            feature3_count = 0
            feature4_count = 0
            feature5_count = 0
            feature6_count = 0
            for line in file.readlines():
                feature6_count = feature6_count + 1
                res = re.findall(r'\w+', line)
                x=0
                if len(res)>1:
                    x = randint(0,len(res)-1)
                count=0
                for word in res:
                    feature1_count = feature1_count + 1

                    if feature2(word):
                        feature2_count = feature2_count+1

                    if feature3(word) :
                        feature3_count = feature3_count+1

                    if feature4(word):
                        feature4_count = feature4_count+1
                    if x == count:
                        if feature5(word):
                            feature5_count = feature5_count + 1
                    count = count+1



        write_for_result(filename, feature1_count, feature2_count, feature3_count, feature4_count,
                         feature5_count,feature6_count,result)
