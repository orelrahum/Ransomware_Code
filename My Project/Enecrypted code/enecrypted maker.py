# Import mudols to have aces to files and folders
import glob
import os
import random



# The path of the folder you want to take unencrypted text from
# Note - the folder path has to end without a '/' and the output folder path has to end with a '/'
folder_path = "D:/Ransomware/My Project/Enecrypted code/original files"
output_folder_path1 = "D:/Ransomware/My Project/Enecrypted code/output files/multiplication_substitution/" # Files encrypted with multiplication_substitution_cipher
output_folder_path2 = "D:/Ransomware/My Project/Enecrypted code/output files/vigenere/" # Files encrypted with vigenere_cipher


# Note - You can change the text-encryption-key to any string you want,  the number-encryption-key has to be a number
number_encryption_key = 20
text_encryption_key = 'h5.q23@#$^7&'



charecters = ''' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^'"&*()-_+=[]/|:;<>\,.?}{	'''



# Encryption function
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
def vigenere_cipher( unencrypted_text ):
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
                i+=1
        encrypted_text.append(encrypted_line)
        encrypted_line = ''

    final_encrypted_text = ''

    for line in encrypted_text:
        final_encrypted_text = f'{final_encrypted_text}\n{line}'
        
    return final_encrypted_text


# Only encrypt a certain percentage of the text, in a certain place
def only_encrypt_some_of_the_text( encrypted_text, original_text, persentage_to_encrypt, percentage_to_start_from):
    
    end_result = []
    
    number_of_letters = len(original_text)

    letter_numbr_to_start_from = int(number_of_letters * percentage_to_start_from)
    number_of_letters_to_encrypt = int(number_of_letters * persentage_to_encrypt)
    
    list_of_encrypted_letters = [char for char in encrypted_text]
    list_of_original_letters = [char for char in original_text]

    # Go through all the text and add the encrypted text in the specified places

    for letter_pos in range(letter_numbr_to_start_from):
        end_result.append(list_of_original_letters[letter_pos])
        
    for letter_pos in range(letter_numbr_to_start_from, letter_numbr_to_start_from+number_of_letters_to_encrypt):
        end_result.append(list_of_encrypted_letters[letter_pos])

    for letter_pos in range(letter_numbr_to_start_from+number_of_letters_to_encrypt, number_of_letters):
        end_result.append(list_of_original_letters[letter_pos])

    return ''.join(end_result)
    

file_number = 0


# Goes through all the files in that folder 
for filename in glob.glob(os.path.join(folder_path, '*.txt')):
    
  
  # Read evrey file separetly
  with open(filename, 'r') as file:
      file_number  += 1
      file_contents = file.read()




    # Encrypt the text in the file with a multiplication substitution cipher
      encryptedText1 = multiplication_substitution_cipher( file_contents )
      
      encryptedText2 = vigenere_cipher( file_contents )
      

      
      percentage_to_encrypt = random.randint(1,19) * 5
      percentage_to_start_from = 100 - percentage_to_encrypt
      
      finished_encrypted_file1 = only_encrypt_some_of_the_text(encryptedText1, file_contents, percentage_to_encrypt/100,percentage_to_start_from/100)
      finished_encrypted_file2 = only_encrypt_some_of_the_text(encryptedText2, file_contents, percentage_to_encrypt/100,percentage_to_start_from/100)


      # Saving the file with a formated name,
      with open(f"{output_folder_path1}MSC-{file_number}-{percentage_to_encrypt}%-{percentage_to_start_from}%.txt", 'w') as output_file:

          output_file.write(finished_encrypted_file1)
          
      with open(f"{output_folder_path2}VS-{file_number}-{percentage_to_encrypt}%-{percentage_to_start_from}%.txt", 'w') as output_file:

          output_file.write(finished_encrypted_file2)
          
          
      
