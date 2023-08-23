from collections import Counter
import sys
input = sys.stdin.readline

def strcount(string, counter):
    while string:
        if counter['s'] == counter['t']:
            print(string)
            return string

        string = string[1:]
        counter = Counter(string)

N = int(input())
string = str(input().rstrip())

strcount(string, Counter(string))