# Testing read, readline(s) mothod
FilePath = "C:\Python39\README.txt"
try:
    f = open(FilePath)    
    #Testing read method 
    str = f.read()
    print(str)
    '''#Testing readlines method
    f = open(FilePath)
    str = f.readlines(15)
    print(str)    
    #Testing readline method'''
    '''f = open(FilePath)
    while 1:
        line = f.readline()
        if len(line):
            print(line)
        else: break'''
except IOError as err: 
   print("Cann't open file because :",err.args)
else:
    print("This file was closed!")
    f.close()

