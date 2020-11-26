# Copyright Orel Rahum
# ID: 316423615
import os
import glob
import re
import enchant

# ENTER YOUR VAR HERE!
# file type is Encrypted or Unencrypted
#file_type = "Encrypted"
file_type = "Unencrypted"

if __name__ == "__main__":
    with open("./check.txt", 'r') as file:
        for line in file.readlines():
            res = re.findall(r'\w+', line)
            for word in res:
                print(word)



