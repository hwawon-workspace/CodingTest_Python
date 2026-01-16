def solution(s):
    stack = []

    if s[0] == ')' or not s:
        return False

    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0