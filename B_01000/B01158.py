# 요세푸스 문제

def baekjoon_1158(n, k):
    people = list(range(1, n + 1))
    result = []
    index = 0

    while people:
        index = (index + k - 1) % len(people)
        result.append(people.pop(index))

    return result

N, K = map(int, input().split())

print("<" + ", ".join(map(str, baekjoon_1158(N, K))) + ">")
