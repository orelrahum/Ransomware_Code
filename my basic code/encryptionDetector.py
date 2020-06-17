# Copyright Liad Cohen & Orel Rahum
# ID:  316602630 , 316423615

# !/usr/bin/python
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


# First, scan (monitoring) the current folder ./ , watching for all changes appearing on .txt files only.
# Once triggered, i.e, a text file is changed, an algorithm to determine how likely an encryption happened
# in the txt file has occurred will be run.
# The result, for each change in text file, will be printed into the command line.


class MyHandler(PatternMatchingEventHandler):
    def __init__(self):
        PatternMatchingEventHandler.__init__(self, patterns=['*.txt'],
                                             ignore_directories=True, case_sensitive=False)

    def on_modified(self, event):
        if event.event_type == "modified":
            print(f'File at path: {event.src_path}, Triggered event type: {event.event_type} \n'
                  f'Checking if encryption happened, please wait... ')
            f = open("./results.csv", "a+")
            text_file = open(f'{event.src_path}', "r")
            fileIsEncrypted = findEncryptedWord(text_file)
            if fileIsEncrypted:
                print("YES! File " + f'{event.src_path},' + " is most likely encrypted,\n")
                f.write(f'{event.src_path}' + " ,yes\n")
            else:
                print("NO! File " + f'{event.src_path}' + " is not encrypted.\n")
                f.write(f'{event.src_path}' + " ,no\n")
            f.close()


def findEncryptedWord(text_file) -> bool:
    words_count = 0
    No_English_count = 0
    Percent_correct_words = 0
    encryptedFile = False
    for line in text_file:
        words = line.split()
        for word in words:
            words_count += 1
            if not realWordOrNum(word):
                No_English_count += 1
    if words_count > 0:
        Percent_correct_words = (No_English_count / words_count) * 100
    if Percent_correct_words > 1:
        encryptedFile = True
    return encryptedFile


def realWordOrNum(word) -> bool:
    begin_ascii_uppercase = 65
    end_ascii_uppercase = 90
    begin_ascii_lowercase = 97
    end_ascii_lowercase = 122
    if word.isnumeric():
        return True
    if len(word) == 1:
        return True
    for c in range(1):
        if not (begin_ascii_uppercase <= c <= end_ascii_uppercase) and (
                begin_ascii_lowercase <= c <= end_ascii_lowercase):
            return False
    for c in range(1, len(word) - 1):
        if not (begin_ascii_lowercase <= ord(word[c]) <= end_ascii_lowercase):
            return False
    return True

def Open_result_file():
    f = open("./results.csv", "w+")
    f.write("name of file , Is encrypted?\n")

if __name__ == "__main__":
    Open_result_file()
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='./', recursive=False)
    observer.start()
    print("Started Monitoring..")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
