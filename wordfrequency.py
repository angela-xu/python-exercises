"""
This is a function to display the most frequent words in a file.
"""

def wordfreq(filepath, n):

    file = open(filepath, "r+")
    dic = {}

    for word in file.read().split():
        word = word.lower()
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1

    sortedList = sorted(dic.items(), key=lambda x : x[1], reverse = True)   # sort dic by values in descending order

    for i in range(n):
        print('Word: ' +  sortedList[i][0] + '   Count:' + str(sortedList[i][1]))

testfile = '/home/angelaxu/Xcode/exercise/testfile.txt'

wordfreq(testfile, 10)
print('\n')
print('\n') 
wordfreq(testfile, 5)
