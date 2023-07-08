import sys

N = int(sys.stdin.readline())
queue = [0] * N
front_idx = 0
rear_idx = 0

def push(x):
    global rear_idx
    queue[rear_idx] = x
    rear_idx = (rear_idx + 1) % N

def pop():
    global front_idx
    if front_idx == rear_idx:
        return -1
    x = queue[front_idx]
    front_idx = (front_idx + 1) % N
    return x

def size():
    return (rear_idx - front_idx + N) % N

def empty():
    return 1 if front_idx == rear_idx else 0

def front():
    return queue[front_idx] if front_idx != rear_idx else -1

def back():
    return queue[(rear_idx - 1 + N) % N] if front_idx != rear_idx else -1

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        push(int(command[1]))
    elif command[0] == "pop":
        print(pop())
    elif command[0] == "size":
        print(size())
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "front":
        print(front())
    elif command[0] == "back":
        print(back())