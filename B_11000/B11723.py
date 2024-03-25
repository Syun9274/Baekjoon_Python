import sys

input = sys.stdin.readline

S = set()
M = int(input())

for _ in range(M):
    cmdInput = input().rstrip().split()
    cmd = [cmdInput[0]] + list(map(int, cmdInput[1:]))
    
    if cmd[0] == "all":
        S = set(range(1, 21))
    elif cmd[0] == "empty":
        S = set()
    elif cmd[0] == "add":
        S.add(cmd[1])
    elif cmd[0] == "remove":
        S.discard(cmd[1])
    elif cmd[0] == "check":
        print(1) if cmd[1] in S else print(0)
    elif cmd[0] == "toggle":
        S.remove(cmd[1]) if cmd[1] in S else S.add(cmd[1])