def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    left, right = 1, distance
    
    while left <= right:
        mid = (left + right) // 2
        removed, prev = 0, 0
        for r in rocks: # 제거할 바위 찾기
            gap = r - prev
            if gap < mid: # gap이 mid보다 작으면 없애기
                removed += 1
            else:
                prev = r # 다음 비교로 넘어가기
        
        if removed <= n: # 최솟값이 mid보다 커도 괜찮음
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
                
    return answer