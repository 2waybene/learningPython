#import re
import counter



cnt = counter.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word.lower()] += 1
print(cnt.most_common())




'''
interests = [(0,"Hadoop"),(0,"Spark"),(0,"Hbase"),(0,"Storm"),(0,"Java"),
(1,"Hadoop"),(1,"SAS"),(1,"Hbase"),(1,"Perl"),(1,"Java"),
(2,"Hadoop"),(2,"Spark"),(2,"R"),(2,"Perl"),(2,"Java"),
(3,"Hadoop"),(3,"Spark"),(3,"R"),(3,"Storm"),(3,"Java"),
(4,"Hadoop"),(4,"SAS"),(4,"R"),(4,"Perl"),(4,"Java")
             ]

words_and_counts = counter.Counter(word
                           for user, interest in interests
                           for word in interest.lower().split()
                            )

for word, count in words_and_counts.most_common():
    if count > 1:
        print word, count

'''

def countOccruence (aList):
    cnt = counter.Counter()
    for word in aList:
        cnt[word] += 1
    return (cnt)





myWords = ["Java","Hadoop","Spark","Hbase","Storm", "Java"]
print(myWords)



countW = countOccruence(myWords)
print (countW)



