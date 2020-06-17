# Copyright Liad Cohen & Orel Rahum
# Made for Defence-Lab course assignment in Ariel University, 2020.

import glob  # for searching .txt files inside current folder
import os
import string
import sys

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
    words_count = 0
    No_English_count = 0
    Percent_correct_words = 0
    encryptedFile = False
    for line in text_file:
        words = line.split()
        for word in words:
            words_count += 1
            if not RealWordOrNum(word):
                No_English_count += 1
    if words_count > 0:
        Percent_correct_words = (No_English_count/words_count)*100
    if Percent_correct_words > 1:
        encryptedFile = True
        return encryptedFile
        #     suggestions = engDict.suggest(word)  # Checks for close-to-legitimate english word.
        #     if not suggestions:
        #         print("Word number " + str(wordCountAtLine) + ", At line number " + str(currentLine) +
        #               ", is most likely encrypted.\n")
        #         encryptedFile = True
        #     wordCountAtLine += 1
        # currentLine += 1
        # wordCountAtLine = 1
    return encryptedFile


def RealWordOrNum(word) -> bool:
    begin_ascii_uppercase = 65
    end_ascii_uppercase = 90
    begin_ascii_lowercase = 97
    end_ascii_lowercase = 122
    if word.isnumeric():
        return True
    if len(word) == 1:
        return True
    for c in range(1):
        if not (begin_ascii_uppercase <= c <= end_ascii_uppercase) and (begin_ascii_lowercase <= c <= end_ascii_lowercase):
            return False
    for c in range(1, len(word) - 1):
        if not (begin_ascii_lowercase <= ord(word[c]) <= end_ascii_lowercase):
            return False
    return True


def main():
    filesToCheck = glob.glob('./*.txt')
    f = open("result.txt", "w+")
    for file in filesToCheck:
        text_file = open(file, "r")
        print("Currently checking if the following file is encrpyted or not: " + str(file))
        fileIsEncrypted = findEncryptedWord(text_file)
        if fileIsEncrypted:
            print("The file " + str(file) + " is most likely encrypted.\n")
            f.write("The file " + str(file) + " is most likely encrypted!!!\n")
        else:
            print("The file " + str(file) + " is not encrypted.\n")
            f.write("The file " + str(file) + " is not encrypted.\n")

    f.close()


if __name__ == "__main__":
    main()
