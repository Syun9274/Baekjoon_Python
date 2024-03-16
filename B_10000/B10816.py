from collections import Counter
import sys
input = sys.stdin.readline

N = input()
cardList = list(map(int, input().split()))
cardList = Counter(cardList)

M = int(input())
card = list(map(int, input().split()))

for num in card:
    if num in cardList:
        print(f'{cardList[num]}', end=' ')
    else:
        print(0, end=' ')