# Copyright Liad Cohen & Orel Rahum
# Made for Defence-Lab course assignment in Ariel University, 2020.

import glob  # for searching .txt files inside current folder
import enchant  # for using english dictionary close-to-legitimate-words suggestions.


# All words are ASCII therefore they are some type of close to a legitimate word in english (or exactly an english word)
# Using ENCHANT, we are determining if each word in the file is a legitimate or close-to-legitimate english word.
# A close-to-legitimate word is the magic inside ENCHANT lib, which uses multiple techniques to determine words against
# the english dictionary. An encrypted word is most likely won't be even close to an english word
# hence the encryption is detected this way.

def findEncryptedWord(text_file) -> bool:
    engDict = enchant.Dict("en_US")  # ASCII english-dictionary
    currentLine = 1
    wordCountAtLine = 1
    encryptedFile = False
    for line in text_file:
        words = line.split()
        for word in words:
            suggestions = engDict.suggest(word)     # Checks for close-to-legitimate english word.
            if not suggestions:
                print("Word number " + str(wordCountAtLine) + ", At line number " + str(currentLine) +
                      ", is most likely encrypted.\n")
                encryptedFile = True
            wordCountAtLine += 1
        currentLine += 1
        wordCountAtLine = 1
    return encryptedFile


def main():
    filesToCheck = glob.glob('./*.txt')
    for file in filesToCheck:
        text_file = open(file, "r")
        print("Currently checking if the following file is encrpyted or not: " + str(file) + "\n")
        fileIsEncrypted = findEncryptedWord(text_file)
        if fileIsEncrypted:
            print("The file " + str(file) + " is most likely encrypted.")
        else:
            print("The file " + str(file) + " is not encrypted.")


if __name__ == "__main__":
    main()
