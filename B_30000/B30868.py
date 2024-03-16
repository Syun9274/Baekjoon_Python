T = int(input())

for i in range(T):
    vote = int(input())
    
    five = vote // 5
    one = vote % 5
    
    print("++++ " * five + "|" * one)