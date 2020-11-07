import os
import glob
import random

# Import all cipher related modules
from pycipher.playfair import Playfair
from pycipher.gronsfeld import Gronsfeld
from pycipher.autokey import Autokey
from pycipher.atbash import Atbash

# The path of the folder you want to take unencrypted text from
# Note - the folder path has to end without a '/' and the output folder path has to end with a '/'
input_folder_path = "D:/Ransomware/TEXT FILES/ALL CHARS/Unencrypted" # Files encrypted with multiplication_substitution_cipher

output_folder_path = "D:/Ransomware/TEXT FILES/ALL CHARS/Encrypted/" # Files encrypted with vigenere_cipher



# Note - You can change the text-encryption-key to any string you want,  the number-encryption-key has to be a number
text_encryption_key = 'flabbergasted!'
number_encryption_key = 33

os.chdir(output_folder_path)


encryption_types = ['Autokey', 'Atbash','Playfair', 'Gronsfeld','multiplication_substitution_cipher','vigenere_cipher']

# Function to encrypt only some of the text file, in a specified position
def only_encrypt_some_of_the_text(encrypted_text, original_text, persentage_to_encrypt, percentage_to_start_from):
    end_result = []

    number_of_letters = len(original_text)

    letter_numbr_to_start_from = int(number_of_letters * percentage_to_start_from)
    number_of_letters_to_encrypt = int(number_of_letters * persentage_to_encrypt)


    list_of_encrypted_letters = [char for char in encrypted_text]
    list_of_original_letters = [char for char in original_text]



    # Go through all the text and add the encrypted text in the specified places

    for letter_pos in range(letter_numbr_to_start_from):
        end_result.append(list_of_original_letters[letter_pos])

    for letter_pos in range(letter_numbr_to_start_from, letter_numbr_to_start_from + number_of_letters_to_encrypt):
        end_result.append(list_of_encrypted_letters[letter_pos])

    for letter_pos in range(letter_numbr_to_start_from + number_of_letters_to_encrypt, number_of_letters):
        end_result.append(list_of_original_letters[letter_pos])

    return ''.join(end_result)


charecters = ''' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^'"&*()-_+=[]/|:;<>\,.?}{	'''
#charecters = ''' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!.,:'''


def multiplication_substitution_cipher( unencrypted_text ):
    global number_encryption_key

    # Separate text into lines so it will be easier to work with
    seperated_text = unencrypted_text.split('\n')

    encrypted_text = []
    encrypted_line = []

    # Goes through all the lines and encrypts them charecter by charecter
    for line in seperated_text:
        for charecter in line:
                encrypted_line.append(charecters[((charecters.index(charecter))*number_encryption_key)%len(charecters)])



        # Adds the line to the whole encrypted text and refreashes the line to encrypt the next one
        encrypted_text.append(''.join(encrypted_line))
        encrypted_line = []

    # Convert the list of encrypted_text to the original format type of a string
    final_encrypted_text = ''
    for line in encrypted_text:
        final_encrypted_text = f'{final_encrypted_text}\n{line}'


    # Return that string
    return final_encrypted_text


alphabet = charecters
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


# Encryption function
def vigenere_cipher(unencrypted_text):
    global text_encryption_key
    seperated_text = unencrypted_text.split('\n')

    encrypted_text = []
    encrypted_line = ''

    # Goes through all the lines
    for line in seperated_text:
        encrypted = ''

        # Split the message into the length of the key
        split_message = [line[i:i + len(text_encryption_key)] for i in range(0, len(line), len(text_encryption_key))]

        for each_split in split_message:
            i = 0
            for letter in each_split:
                number = (letter_to_index[letter] + letter_to_index[text_encryption_key[i]]) % len(alphabet)
                encrypted_line += index_to_letter[number]
                i += 1
        encrypted_text.append(encrypted_line)
        encrypted_line = ''

    final_encrypted_text = ''

    for line in encrypted_text:
        final_encrypted_text = f'{final_encrypted_text}\n{line}'

    return final_encrypted_text




def encrypt( original_lines, encryption_type):
    global ciphertext
    original_text =[]
    for line in original_lines:
        original_text.append(f'{line}\n')
    end_result = []
    # Encrypts all the lines, one by one
    for original_line in original_lines:


        # Checks which encryption method  to use, and encrypts the text accordingly
        if encryption_type == 'Atbash':
            ciphertext = Atbash().encipher(original_line, keep_punct = False)

        elif encryption_type == 'Autokey':

            ciphertext = Autokey('HELLO').encipher(original_line)

        elif encryption_type == 'Playfair':
            ciphertext = Playfair(key='zgptfoihmuwdrcnykeqaxvsbl').encipher(original_line)

        elif encryption_type == 'Gronsfeld':
            ciphertext = Gronsfeld([5, 4, 7, 9, 8, 5, 8, 2, 0, 9, 8, 4, 3]).encipher(original_line)

        elif  encryption_type == 'multiplication_substitution_cipher':
            return multiplication_substitution_cipher(''.join(original_text))

        elif encryption_type == 'vigenere_cipher':
            return vigenere_cipher(''.join(original_text))




        symbols = 0

    # Goes over the original and encrypted text, and only appends to the final result the symbols from the original with the same indexes
        for i in range(len(original_line)):
            if original_line[i] in """~`!@#$%^&*()-_+=}{]\[|/:"'?<>,. 1;234	567890""":
                end_result.append(original_line[i])
                symbols += 1
            else:
                if ciphertext != '':
                    end_result.append(ciphertext[i - symbols])

        # Adds line separation
        end_result.append('\n')
    end_result.pop(len(end_result)-1)
    return ''.join(end_result)






    # Goes through all the encryption types and creates a folder for each one, and encrypts all the folders
for encryption_type in encryption_types:
    new_folder = encryption_type
    os.makedirs(new_folder)


    # Goes through all the files in that folder
    for filename in glob.glob(os.path.join(input_folder_path, '*.txt')):
        


      # Read evrey file separetly
      with open(filename, 'r') as file:
          file_contents = file.read()
          #print(file.name)



        # Encrypt the text with the current encryption type


          encrytedText1 = encrypt(file_contents.split('\n'), encryption_type)

          # Randomly chooses some percentage to encrypt, and the percentage to start from accordingly
          percentage_to_encrypt = random.randint(1,19) * 5
          percentage_to_start_from = 100 - percentage_to_encrypt

          finished_encrypted_file = only_encrypt_some_of_the_text(encrytedText1, file_contents, percentage_to_encrypt/100,percentage_to_start_from/100)


          file_number=''
          for i in file.name:
              if i in '1234567890':
                  file_number += i

          print(file_number)

           #Saving the file with a formated name,
          with open(f"{output_folder_path}{encryption_type}/{file_number}-{percentage_to_encrypt}%-{percentage_to_start_from}%.txt", 'w') as output_file:
              output_file.write(finished_encrypted_file)

