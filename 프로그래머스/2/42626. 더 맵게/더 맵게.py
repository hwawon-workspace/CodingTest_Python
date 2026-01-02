from heapq import heapify, heappush, heappop

def solution(scoville, K):
    heapify(scoville)
    cnt = 0
    while len(scoville) >= 2:
        if scoville[0] >= K:
            return cnt
        heappush(scoville, heappop(scoville)+heappop(scoville)*2)
        cnt += 1
    if scoville[0] >= K:
        return cnt
    else:
        return -1