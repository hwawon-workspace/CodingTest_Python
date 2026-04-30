def solution(n, lost, reserve): # 전체 학생 수, 도난 번호, 여벌 번호    
    answer = 0 # 체육복 있는 학생 최댓값
    lost, reserve = set(lost), set(reserve)
    no_spare = lost & reserve
    lost -= no_spare
    reserve -= no_spare
    
    remain = lost
    for l in list(lost):
        if l-1 in reserve:
            remain.remove(l)
            reserve.remove(l-1)
        elif l+1 in reserve:
            remain.remove(l)
            reserve.remove(l+1)
    answer = n - len(remain)
    return answer