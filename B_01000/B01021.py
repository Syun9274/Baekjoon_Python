from collections import deque

n, m = list(map(int, input().split()))
targets = list(map(int, input().split()))

queue = deque(range(1, n + 1))
movement_count = 0

for target in targets:
    target_index = queue.index(target)

    if target_index <= len(queue) // 2:
        queue.rotate(-target_index)
        movement_count += target_index
    else:
        queue.rotate(len(queue) - target_index)
        movement_count += len(queue) - target_index

    queue.popleft()

print(movement_count)