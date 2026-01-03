def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c[0]-1, c[1]-1, c[2]-1
        print(i,j,k)
        tmp = array[i:j+1]
        tmp.sort()
        answer.append(tmp[k])
    return answer

# 다른 사람 풀이: lambda 사용
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
