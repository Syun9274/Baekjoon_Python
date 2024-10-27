n = int(input())
arr = list(map(int, input().split()))

if n <= 4:
    print("YES")
    exit(0)

stacks = [[] for _ in range(4)]

for num in arr:
    for stack in stacks:
        if len(stack) == 0 or num >= stack[-1]:
            stack.append(num)
            break
    else:
        print("NO")
        exit(0)

print("YES")