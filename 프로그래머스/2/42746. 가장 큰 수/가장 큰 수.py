#     arr.sort(key=lambda x: x.ljust(4, x[-1]), reverse=True)

def solution(numbers):
    answer = ''
    arr = [str(i) for i in numbers]
    arr.sort(key=lambda x: x*3, reverse=True)
    for i in arr:
        answer += i

    return str(int(answer))