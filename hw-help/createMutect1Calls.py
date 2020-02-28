
import os
print(os.getcwd())

os.chdir("X:\\project2017\\exomeSeq\\doc")
print(os.getcwd())

mySecretStoryFile = open("Mouse_HCC_ExomeSeq_expinfo.csv", "r", encoding="utf-8")
allSecretStory = mySecretStoryFile.readlines()

for sentence in allSecretStory:
    print(sentence)
    #aDecodedLine = deEncrytStory(keyList, sentence)
    #myClearStoryFile.write(aDecodedLine+"\n")

genderDict = {}

import csv
with open('Mouse_HCC_ExomeSeq_expinfo.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(row)
        print (', '.join(row))
    #    genderDict[row[7]]=row[2]

