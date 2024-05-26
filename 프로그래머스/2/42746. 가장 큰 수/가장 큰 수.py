#     arr.sort(key=lambda x: x.ljust(4, x[-1]), reverse=True)
# 일의 자리수 늘려서 자릿수 맞추는 방식은 12, 1213 해결 X

def solution(numbers):
    answer = ''
    arr = [str(i) for i in numbers]
    arr.sort(key=lambda x: x*3, reverse=True)
    for i in arr:
        answer += i

    return str(int(answer))