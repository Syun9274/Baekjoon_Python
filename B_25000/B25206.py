import sys

score = {'A+': 4.5, 'A0': 4.0, 
         'B+': 3.5, 'B0': 3.0, 
         'C+': 2.5, 'C0': 2.0, 
         'D+': 1.5, 'D0': 1.0, 
         'F': 0.0}

K = list(score.keys())
V = list(score.values())
alltime, total = 0, 0

while True:
    try:
        n, t, a = map(str, sys.stdin.readline().split())
        
        if a == 'P':
            continue
        
        total += float(t) * float(str(V[K.index(a)]))
        alltime += float(t)
    except EOFError:
        break
    except ValueError:
        break

avg = total / alltime

sys.stdout.write(str(avg) + '\n')