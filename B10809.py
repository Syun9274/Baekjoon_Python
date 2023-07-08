word = str(input())
alphabet = [-1 for _ in range(26)]

for idx in range(len(word)):
    if alphabet[ord(word[idx]) - ord('a')] == -1:
        alphabet[ord(word[idx]) - ord('a')] = idx
    else: pass

for i in alphabet:
    print(i, end=' ')