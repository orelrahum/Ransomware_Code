# in this File we will remove symbols

if __name__ == "__main__":
    edit_file = "total.txt"  # Please enter here your file name
    final_lines=""
    file = open(edit_file, "r")
    for lines in file.readlines():
        name_file = "=total - just ASCI.txt "
        chars = "\\`:!@#$%^&*()-_=+[{}];'\\.,/|1234567890"
        for c in chars:
            lines = lines.replace(c,"")
        final_lines = final_lines + lines + "\n"
    write_file = open(name_file, "a+")
    write_file.write(final_lines)
    write_file.close()
    file.close()

