# in this File we will remove symbols

if __name__ == "__main__":
    edit_file = "original files\\total.txt"  # Please enter here your file name
    file = open(edit_file, "r")
    for lines in file.readlines():
        name_file = "original files\\total - with part of symbols.txt "
        chars = "\\`@#$%^&*()-_=+[{}];'\\/|"
        for c in chars:
            lines = lines.replace(c,"")
        write_file = open(name_file, "a+")
        write_file.write(lines)
    write_file.close()
    file.close()

