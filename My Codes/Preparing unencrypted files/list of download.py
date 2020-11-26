# in this File we will make Unencrypted Text file
import glob
import random

global number_files
global name_file

# ADD all your VARS here


if __name__ == "__main__":
    site="http://www.gutenberg.org/files/"
    for i in range (5000,10001):
        site_temp=site+str(i)+"/"+str(i)+".txt\n"
        write_file = open("output.txt", "a+")
        write_file.write(site_temp)
        write_file.close()
