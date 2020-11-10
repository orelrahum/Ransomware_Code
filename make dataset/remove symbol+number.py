# in this File we will remove symbols

if __name__ == "__main__":
    edit_file = "original files\\total.txt"  # Please enter here your file name
    file = open(edit_file, "r")
    for lines in file.readlines():
        name_file = "original files\\total - just ASCI.txt "
        chars = "\\`:!@#$%^&*()-_=+[{}];'\\.,/|1234567890"
        for c in chars:
            lines = lines.replace(c,"")
        write_file = open(name_file, "a+")
        write_file.write(lines)
    write_file.close()
    file.close()

