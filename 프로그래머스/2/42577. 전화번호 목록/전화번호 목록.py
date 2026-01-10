# hash map 풀이
def solution(phone_book): 

    hash_map = {} 
    for nums in phone_book: 
        hash_map[nums] = 1 
    
    for nums in phone_book: 
        prefix = "" 
        for num in nums: 
            prefix += num
    
            if prefix in hash_map and prefix != nums:       
                return False 
                
    return True

# sorting -> startswith 사용 풀이
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
