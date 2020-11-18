# in this File we will make Encrypted Text file
from pycipher import *
import os
import glob
import random
from Crypto.Cipher import AES


global CipherText

# ADD all your VARS here
folder_name = 'Just ASCII'
file_path = "E:\\Dropbox\\Orel\\Ariel University\\final Project\\DATASET\\" + folder_name + "\\Unencrypted"
output_path = "E:\\Dropbox\\Orel\\Ariel University\\final Project\\DATASET\\" + folder_name + "\\Encrypted"
Playfair_KEY = 'zgptfoihmuwdrcnykeqaxvsbl'
Gronsfeld_KEY = [5, 4, 7, 9, 8, 5, 8, 2, 0, 9, 8, 4, 3]
Autokey_KEY = 'HELLO'
Caesar_KEY = 4

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
        encrypt_row = Autokey(Autokey_KEY).encipher(line)

    elif encryption_type == 'Playfair':
        encrypt_row = Playfair(Playfair_KEY).encipher(line)

    elif encryption_type == 'Gronsfeld':
        encrypt_row = Gronsfeld(Gronsfeld_KEY).encipher(line)

    elif encryption_type == 'Caesar':
        encrypt_row = Caesar(Caesar_KEY).encipher(c,keep_punct=True)

    elif encryption_type == 'AES':
        obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
        encrypt_row = obj.encrypt(line)

    return encrypt_row


if __name__ == "__main__":
    #encryption_types = ['AES','Caesar','Autokey', 'Atbash', 'Playfair', 'Gronsfeld']
    encryption_types = ['AES']
    for encryption_type in encryption_types:
        make_folder(encryption_type)
        file_number = 1
        for filename in glob.glob(file_path +'\\*.txt'):
            # Read every file
            num_total_lines = sum(1 for line in open(filename))
            precent_of_encypt_line = random.randint(1, 100)
            final_text = ""
            with open(filename, 'r') as file:
                count_line = 1
                for line in file.readlines():
                    final_text = final_text + line + "\n"
                    #if 100-precent_of_encypt_line > (count_line/num_total_lines)*100 :
                    #    final_text = final_text + line+"\n"
                    #else:
                    #    encrytedText = encrypt(line, encryption_type)
                    #    final_text = final_text + encrytedText + "\n"
                    #count_line = count_line+1
            # Saving the file with a formated name,
            final_text = encrypt(final_text , encryption_type)
            with open(f"{output_path}\\{encryption_type}\\{encryption_type}-{file_number}.txt",
                      'w') as output_file:
                output_file.write(final_text)
            file_number = file_number + 1
