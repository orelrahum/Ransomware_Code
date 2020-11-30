# in this File we will make Unencrypted Text file
import glob
import random

global number_files
global name_file

# ADD all your VARS here


if __name__ == "__main__":
    commonWords = ["the", "of", "and", "a", "to", "in", "is", "you", "that", "it", "he", "was", "for", "on", "are",
                   "as", "with", "his"
        , "they", "I", "at", "be", "this", "have", "from", "or", "one", "had", "by", "word", "but", "not", "what",
                   "all", "were", "we", "when"
        , "your", "can", "said", "there", "use", "an", "each", "which", "she", "do", "how", "their", "if", "will", "up",
                   "other", "about"
        , "out", "many", "then", "them", "these", "so", "some", "her", "would", "make", "like", "him", "into", "time",
                   "has", "look", "two"
        , "more", "write", "go", "see", "number", "no", "way", "could", "people", "my", "than", "first", "water",
                   "been", "call", "who", "oil"
        , "its", "now", "find", "long", "down", "day", "did", "get", "come", "made", "may", "part"]
    print (len(commonWords))
    site="http://www.gutenberg.org/files/"
    for i in range (1,10001):
        site_temp=site+str(i)+"/"+str(i)+".txt\n"
        write_file = open("output.txt", "a+")
        write_file.write(site_temp)
        write_file.close()
