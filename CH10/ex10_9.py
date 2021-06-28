# file and directory management
import os
# Rename a file from test1.txt to test2.txt
os.rename("test1.txt", "test2.txt")
# Delete file test2.txt
os.remove("test2.txt")
# Create a directory "test"
os.mkdir("TEST_DIR")
# Changing a directory to "test1"
os.chdir("TEST_DIR")
# This would give location of the current directory
print("Current directory is:",os.getcwd())
# This would  remove "test1"  directory.



