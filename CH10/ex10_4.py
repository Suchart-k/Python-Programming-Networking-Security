# read file in line by line
import linecache
FilePath = "C:\Python39\README.txt"
for line in range(5):
    print(linecache.getline(FilePath, line))
linecache.clearcache()


