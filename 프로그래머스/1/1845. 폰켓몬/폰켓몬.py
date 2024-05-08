def solution(nums):
    answer = 0
    setList = set(nums)
    k = len(nums) // 2
    i = len(setList)
    if i > k:
        return k
    else:
        return i
