MBTI = input().rstrip()
N = int(input().rstrip())

count = 0
for _ in range(N):
    mbti = input().rstrip()
    
    if mbti == MBTI:
        count += 1
        
print(count)