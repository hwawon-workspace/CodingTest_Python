def solution(n, times):
    left, right = 1, max(times)*n
    
    answer = right 
    
    while left <= right:
        mid = (left+right) // 2 # 얼마나 걸릴지 시간을 이분법으로 구하는 것

        people = 0 
        for t in times:
            people += mid // t # mid시간동안 t에서 처리할 수 있는 사람 수
            if people >= n:
                break
        
        if people >= n: # mid 안에 n명 충분히 가능
            answer = mid # 정답 후보
            right = mid - 1 # 최대값을 mid보다 작은 값으로 줄여서 다시 이분법
            
        else: # mid 안에 n명 불가능
            left = mid + 1 # 최소를 늘려보기
            
    return answer