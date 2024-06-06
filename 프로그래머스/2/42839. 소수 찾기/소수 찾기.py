from itertools import permutations


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    nums = set()
    result = 0
    for i in range(1, len(numbers) + 1):
        p = permutations(numbers, i)
        for pe in p:
            num = int(''.join(pe))
            nums.add(num)
    
    for num in nums:
        if is_prime(num):
            result = result+ 1
    
    return result