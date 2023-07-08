import sys
input = sys.stdin.readline

N, M = map(int, input().split())

not_heard = set()
not_seen = set()

for _ in range(N):
    not_heard.add(input().strip())

for _ in range(M):
    not_seen.add(input().strip())

both = sorted(list(not_heard & not_seen))

print(len(both))
for person in both:
    print(person)