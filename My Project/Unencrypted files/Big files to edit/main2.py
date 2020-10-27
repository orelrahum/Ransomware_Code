

def create_file():
    global name_file
    name_file = "total.txt"
    write_file = open(name_file, "w+")
    write_file.close()


if __name__ == "__main__":
    edit_file = "Big files to edit\\alice29.txt"  # Please enter here your file name
    num_of_lines = random.randint(50, 100)
    print(num_of_lines)
    num_total_lines = sum(1 for line in open(edit_file))
    print(num_total_lines)
    global number_files
    number_files = 1
    x = 0