# in this File we will remove symbols
if __name__ == "__main__":
    edit_file = "total2.txt"  # Please enter here your file name
    final_lines=""
    file = open(edit_file, "r")
    for lines in file.readlines():
        name_file = "total - half chars.txt "
        chars = "\\`@#$%^&*()-_=+[{}];'\\/|"
        for c in chars:
            lines = lines.replace(c,"")
        final_lines = final_lines + lines + "\n"
    write_file = open(name_file, "a+")
    write_file.write(final_lines)
    write_file.close()
    file.close()
