import sys
input = sys.stdin.readline

def push(stackArray, num):
    stackArray.append(num)
    return stackArray

def pop(stackArray):
    if len(stackArray) == 0:
        print(-1)
    else:
        print(stackArray[-1])
        del(stackArray[-1])
        return stackArray
    
def size(stackArray):
    print(len(stackArray))

def empty(stackArray):
    if len(stackArray) == 0:
        print(1)
    else: 
        print(0)

def top(stackArray):
    if len(stackArray) == 0:
        print(-1)
    else:
        print(stackArray[-1])

N = int(input())
stack = []

for i in range(N):
    cmd = list(map(str, input().split()))

    if cmd[0] == "push":
        push(stack, int(cmd[1]))
    elif cmd[0] == "pop":
        pop(stack)
    elif cmd[0] == "size":
        size(stack)
    elif cmd[0] == "empty":
        empty(stack)
    elif cmd[0] == "top":
        top(stack)