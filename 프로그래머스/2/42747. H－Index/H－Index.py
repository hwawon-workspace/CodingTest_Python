def solution(citations):
    citations.sort(reverse=True)

    for idx, h in enumerate(citations):
        if h < idx + 1:
            return idx
    return len(citations)