def solution(sizes):
    for size in sizes:
        size.sort()
    w, h = zip(*sizes)
    answer = max(w) * max(h)
    return answer

# 다른 사람 풀이(같은 의미, 짧은 코드)
def solution(sizes):
    return max(max(size) for size in sizes) * max(min(size) for size in sizes)
