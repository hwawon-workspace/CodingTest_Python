def solution(n, lost, reserve):
    lost, reserve = set(lost), set(reserve)
    
    # 여벌 있는 학생
    spare = lost & reserve
    lost -= spare
    reserve -= spare
    
    # 빌려주기
    for r in sorted(reserve):
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
        continue

    answer = n - len(lost)
    return answer