def cantore(N):
    Line = "-" * (3 ** N)
    
    if N == 0:
        return Line
    
    Line = list(Line)
    Line[3 ** (N - 1) : 3 ** (N - 1) * 2] = [" "] * (3 ** (N - 1))
    Line[:3 ** (N - 1)] = cantore(N - 1)
    Line[3 ** (N - 1) * 2:] = cantore(N - 1)
    return "".join(Line)

while True:
    try:
        N = int(input())
        print(cantore(N))
    except:
        break