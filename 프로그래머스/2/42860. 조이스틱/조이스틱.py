def solution(name):
    n = len(name)
    answer = 0

    for c in name:
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
        
    move = n - 1 

    for i in range(n):
        j = i + 1
        
        while j < n and name[j] == 'A':
            j += 1

        move = min(move, i * 2 + (n - j), (n - j) * 2 + i)

    answer += move
    return answer
