T = int(input())

for _ in range(T):
    arr = list(input().split())
    num = 0

    for i in range(len(arr)):
        if(i == 0):
            num += float(arr[0])
        elif(arr[i] == '@'):
            num *= 3
        elif(arr[i] == '%'):
            num += 5
        elif(arr[i] == '#'):
            num -= 7
            
    print(f'{num:.2f}')