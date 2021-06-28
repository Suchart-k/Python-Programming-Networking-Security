# tell and seek method
file = open("README.txt", "r+")
str = file.read(10);
print ("Read String is : ", str)
# Check current position
position = file.tell();
print ("1.Current file position after read 1:", position)
# Reposition pointer at the beginning once again
position = file.seek(5, 0);
print ("2.Current file position after seek 1:", position)
str = file.read(10);
print ("Again read String is : ", str)
print ("2.Current file position after read 2:", file.tell())
# Reposition pointer at the current position
position = file.seek(0, 1);
print ("3.Current file position after seek 2:", position)
str = file.read(10);
print ("3.Again read String is : ", str)
print ("3.Current file position after read 3: ", position)
# Reposition pointer at the end of file
position = file.seek(0, 2);
print ("4.Current file position after seek 3:", position)
str = file.read(10);
print ("4.Again read String is : ", str)
print ("4.Current file position after read 4: ", position)
# Close opend file
file.close()




