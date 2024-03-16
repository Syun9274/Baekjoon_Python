import sys
input = sys.stdin.readline
output = sys.stdout.write

document = input().strip()
find = input().strip()
count = 0

while(True):
    try:
        index = document.index(find)
        count += 1
        document = document[index + len(find):]
        
    except ValueError:
        break

print(str(count))
