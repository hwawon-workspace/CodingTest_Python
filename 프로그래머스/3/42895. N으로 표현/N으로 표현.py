def solution(N, number):
    if number == 1:
        return 1
    set_list = []
    
    for i in range(1, 9):
        set_tmp = set()
        set_tmp.add(int(str(N)*i))
        for j in range(i-1):
            for arg in set_list[j]:
                for arg2 in set_list[-j-1]:
                    set_tmp.add(arg+arg2)
                    set_tmp.add(arg-arg2)
                    set_tmp.add(arg*arg2)
                    if arg2 != 0:
                        set_tmp.add(arg/arg2)
        if number in set_tmp:
            return i
        set_list.append(set_tmp)
    return -1