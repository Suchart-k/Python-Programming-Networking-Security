# read file in word by word
FilePath = "C:\Python39\README.txt"
wordTemp = []
wordCount = 0
file = open(FilePath, 'r')
for line in file:
    for word in line.split():
        wordTemp.append(word)
        wordCount = wordCount + 1
print(wordTemp)
print("The number of word count in this file =", wordCount)


