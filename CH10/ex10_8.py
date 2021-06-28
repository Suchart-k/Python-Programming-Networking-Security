# with with open file
# use with to read file
with open("newfile.txt") as file:
    for line in file:
        print (line)

#use with to write file
with open("hello.txt", "w") as file:
    file.write("Hello World")


