def solution(sizes):
    for size in sizes:
        size.sort()
    w, h = zip(*sizes)
    answer = max(w) * max(h)
    return answer