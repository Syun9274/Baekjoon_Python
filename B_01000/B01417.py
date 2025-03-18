# 국회의원 선거

n = int(input())
vote = []

for i in range(n):
    number = int(input())
    vote.append(number)

if n == 1:
    print(0)
else:
    people = 0

    while True:
        max_vote = max(vote[1:])
        if vote[0] > max_vote:
            break
        
        vote[0] += 1
        max_idx = vote[1:].index(max_vote) + 1
        vote[max_idx] -= 1
        people += 1

    print(people)
