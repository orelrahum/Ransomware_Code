# in this File we will make Encrypted Text file
from pycipher import *
import os
import glob
import random

global CipherText

# ADD all your VARS here
file_path = "C:\\Users\\orelr\\Desktop\\check\\input"
output_path = "C:\\Users\\orelr\\Desktop\\check\\output"
Playfair_KEY = 'zgptfoihmuwdrcnykeqaxvsbl'
Gronsfeld_KEY = [5, 4, 7, 9, 8, 5, 8, 2, 0, 9, 8, 4, 3]
Autokey_KEY = 'HELLO'


def make_folder(encryption_type):
    new_folder = "\\" + encryption_type
    path = output_path + new_folder
    if os.path.isdir(path) is False:
        os.makedirs(path)


def encrypt(line, encryption_type):
    # Checks which encryption method  to use, and encrypts the text accordingly
    encrypt_row = ""
    if encryption_type == 'Atbash':
        encrypt_row = Atbash().encipher(line, keep_punct=False)

    elif encryption_type == 'Autokey':
        encrypt_row = Autokey(Autokey_KEY).decipher()(line)

    elif encryption_type == 'Playfair':
        encrypt_row = Playfair(Playfair_KEY).encipher(line)

    elif encryption_type == 'Gronsfeld':
        encrypt_row = Gronsfeld(Gronsfeld_KEY).encipher(line)

    return encrypt_row




if __name__ == "__main__":
    encryption_types = ['Autokey', 'Atbash', 'Playfair', 'Gronsfeld']
    for encryption_type in encryption_types:
        make_folder(encryption_type)
        file_number = 1
        for filename in glob.glob(os.path.join(file_path, '*.txt')):
            # Read every file
            num_total_lines = sum(1 for line in open(filename))
            random_encrypt_row = random.randint(num_total_lines-1, num_total_lines)
            final_text = ""
            with open(filename, 'r') as file:
                for line in file.readlines():
                    if random_encrypt_row < num_total_lines - random_encrypt_row:
                        final_text = final_text + line+"\n"
                    else:
                        encrytedText = encrypt(line, encryption_type)
                        final_text = final_text + encrytedText + "\n"

            # Saving the file with a formated name,
            with open(f"{output_path}\\{encryption_type}\\{encryption_type}-{file_number}-{random_encrypt_row}.txt",
                      'w') as output_file:
                output_file.write(final_text)
                file_number = file_number + 1
