def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c[0]-1, c[1]-1, c[2]-1
        print(i,j,k)
        tmp = array[i:j+1]
        tmp.sort()
        answer.append(tmp[k])
    return answer