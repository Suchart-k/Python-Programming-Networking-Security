import sys
import os

if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(filename + " does not exist.")
        exit(0)
if os.access(filename, os.R_OK):
    print(filename + " read only.")
    exit(0)


