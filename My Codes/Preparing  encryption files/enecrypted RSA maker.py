# in this File we will make Encrypted Text file
from pycipher import *
import os
import glob
import random

global CipherText

# ADD all your VARS here
#folder_name = 'all ASCII'
#folder_name ="only english chars"
#folder_name ="only english chars + numbers"
file_path = "E:\\Dropbox\\Orel\\Ariel University\\final Project\\DATASET 12000 files\\Unencrypted"
output_path = "E:\\Dropbox\\Orel\\Ariel University\\final Project\\DATASET 12000 files\\Encrypted"
rsa_file= "E:\\Dropbox\\Orel\\Ariel University\\final Project\\ransomware_detection\\My Codes\\Preparing  encryption files\\RSA FILE.txt"

def make_folder(encryption_type):
    new_folder = "\\" + encryption_type
    path = output_path + new_folder
    if os.path.isdir(path) is False:
        os.makedirs(path)


if __name__ == "__main__":
    make_folder("RSA")
    file_number = 1
    for filename in glob.glob(file_path +'\\*.txt'):
        print (filename)
        # Read every file
        num_total_lines = sum(1 for line in open(filename))
        precent_of_encypt_line= random.randint(30, 100)
        encypt_line=num_total_lines *(precent_of_encypt_line/100)
        # print("num of total lines :"+str(num_total_lines) )
        # print("precent_of_encypt_line:" + str(precent_of_encypt_line))
        # print("encypt_line :" + str(encypt_line))
        final_text = ""
        with open(filename, 'r') as file:
            t=0
            for line in file.readlines():
                if t < 4:
                    final_text = final_text + line
                t=t+1
        with open(rsa_file,'rb') as rsa:
            x = 0
            for line in rsa.readlines():
                x = x + 1
                if x < encypt_line:
                    final_text = final_text + str(line) + "\n"

        # Saving the file with a formated name,
        with open(f"{output_path}\\RSA\\RSA-{file_number}"
                  f"-{precent_of_encypt_line}%.txt",'w') as output_file:
            output_file.write(final_text)
        file_number = file_number + 1
