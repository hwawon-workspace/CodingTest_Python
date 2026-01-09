def solution(n, times):
    left = 1 # 최소 시간
    right = max(times) * n # 최대 시간
    
    answer = right # 최대로 가정
    
    while left <= right:
        mid = (left + right) // 2
        
        people = 0
        for t in times:
            people += mid // t
            if people >= n:
                break
                
        if people >= n:
            answer = mid
            right = mid - 1

        else:
            left = mid + 1
            
    return answer