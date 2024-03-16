import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    string = input()
    stack = []
    VPS = True
    
    for STR in string:
        if STR == "(":
            stack.append(1)
        elif STR == ")":
            if len(stack) == 0:
                VPS = False
                break
            else:
                stack.pop()
                
    if VPS == False or len(stack) != 0:
        print("NO")
    elif VPS == True:
        print("YES")   