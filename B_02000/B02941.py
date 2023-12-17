S = str(input())
n = len(S)

for i in range(1, len(S)):
    if S[i] == '=' or S[i] == '-':
        n -= 1
        if S[i - 1] == 'z' and i - 1 != 0 and S[i - 2] == 'd':
            n -= 1
        else: pass
    elif S[i] == 'j':
        if S[i - 1] == 'l' or S[i - 1] == 'n':
            n -= 1
        else: pass
    else: pass

print(n)