N = int(input())

for i in range(N):
    quiz = str(input())
    S, tmp = 0, 0

    for a in range(len(quiz)):
        if quiz[a] == 'O':
            tmp += 1
        else: tmp = 0

        S += tmp

    print(S)