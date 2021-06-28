# write, writelines
string1 = "hello world in the new file\n"
string2 = "and another line\n"
sequence = ["Sequence string line 1\n", "Sequence string line 2"]
file = open("newfile.txt", "w") 
file.write(string1) 
file.write(string2)
file.writelines(sequence)
file.close()


