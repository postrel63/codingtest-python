def solution(nums):
    setList = set(nums)
    k = len(nums) // 2
    i = len(setList)
    if i > k:
        return k
    else:
        return i
