# Show Opening and Closing files
FilePath = "C:\\Python39\\ทดสอบอ่านไทย.txt"
try:
    f = open(FilePath, 'r', encoding='utf-8')
    if f:
        print("สามารถเปิดแฟ้ม :",FilePath, "ได้แล้ว")
        print ("Name of the file: ", f.name)
        print ("Opening mode : ", f.mode)
        str = f.readline()
        print("ข้อความในแฟ้มคือ ",str)
except IOError as err:
    print("ไม่สามารถเปิดแฟ้มได้เพราะ :",err.args)
else:
    print("ปิดแฟ้มเรียบร้อยแล้ว")
    f.close()


