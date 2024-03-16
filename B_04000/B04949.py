while True:
    string = input().rstrip()
    if string == ".":
        break

    val = True
    stack = []

    for s in string:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")" or s == "]":
            if len(stack) == 0:
                val = False
                break
            elif s == ")" and stack[-1] == "(":
                stack.pop()
            elif s == "]" and stack[-1] == "[":
                stack.pop()
            else:
                val = False
                break

    if len(stack) != 0:
        val = False

    if val:
        print("yes")
    else:
        print("no")