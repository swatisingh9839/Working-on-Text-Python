


def analyseText():
 
        textFile = open(r"textfile.txt","r+")
        print("The text file has this text: \n")
        textList = textFile.read()
        words=textList.split(' ')
        textFile.close()
        print('The no of words in a text file are:',len(words))
        print(textList)

def unique_words():
    
        textFile = open(r"textfile.txt","r+")
        print("The text file has these many unique words text: \n")
        textList = textFile.read()
        newlist = textList.split()
        uniqueWords=set(newlist)
        print(len(uniqueWords))
        print(uniqueWords)
   
def inputText(m):
        newText = m.split()
        print(len(newText))
        uniqueWords = set(newText)
        print(len(uniqueWords))
        print(uniqueWords)

def common_words(num,uniqueWords):
        commonwords = {}
        for x in uniqueWords:
            if  commonwords[x] >= num:
                commonwords.update({x:uniqueWords[x]})
        return len(commonwords)



analyseText()
print()
unique_words()
uniqueWords = {}
uniqueWords = unique_words()
print()
inputText('swati singh is a student student')
print()
common_words(4,uniqueWords)

'''
textFile = open(r"textfile.txt","r+")
print("The text file has these many common words text: \n")
textList = textFile.read()
newlist = textList.split()
Counter = Counter(newlist) 
print(newlist)'''





'''uniqueWords=set(newlist)
    for x in uniqueWords:
        if x in commonwords >= num:
            commonwords.update({x:uniqueWords[x]})
    return len(commonwords) '''  

    


#n = int(input('Enter the no for which u want first nth common words:\n'))
#commonWords()
'''new = sorted(commonwords.items()) 
for l in new:
        print(f'{new[0]}:{new[1]}\n')   '''  
