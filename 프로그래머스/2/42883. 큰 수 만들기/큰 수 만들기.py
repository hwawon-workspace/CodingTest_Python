def solution(number, k):
    stack = []

    for num in number:
        # stack[-1](이전에 채택된 앞 숫자)가 현재 num보다 작으면 제거
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1

        # 현재 숫자 추가
        stack.append(num)

    # k개 소진 못했다면(내림차순 배열 등) 뒤에서 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)