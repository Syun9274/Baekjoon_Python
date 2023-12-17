count = 1

def recursion(string):
    global count
    l = len(string)
    
    if l <= 1:
        return print(1, count)
    elif string[0] != string[-1]:
        return print(0, count)
    else:
        count += 1
        recursion(string[1:-1])

T = int(input())

for _ in range(T):
    test = input()
    count = 1
    recursion(test)