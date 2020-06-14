

with open("fileProject.txt", "r") as fp:
  for i in range(10000):
    line = fp.readline()
    nameFile= "file{}.txt ".format(i)
    writeFile = open(nameFile, "a")
    writeFile.write(line)

     #writeFile.write(fp.readline())
writeFile.close()

#open and read the file after the appending:
# f = open("fileProject.txt", "r")
# print(f.read())