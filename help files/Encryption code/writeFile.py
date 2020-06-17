def main():
    for i in range(150):
        nameFile= "{}.txt ".format(i)
        writeFile = open(nameFile, "w")
        writeFile.close()


if __name__ == "__main__":
    main()
