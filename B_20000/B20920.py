import sys
input = sys.stdin.readline

words, wordLen = map(int, input().split())
wordList = {}

for _ in range(words):
    word = str(input().rstrip())
        
    if len(word) < wordLen:
        continue
    
    if word not in wordList:
        wordList[word] = 1
    else: wordList[word] += 1
    
sortList = sorted(wordList.items(), key= lambda k: (-k[1], -len(k[0]), k[0]))
    
for item in sortList:
    print(item[0])