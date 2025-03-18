# 소트인사이드

num = list(str(input().split()))

num = num[2 : -2]
num.sort(reverse = True)
ans = ''.join(num)

print(ans)
