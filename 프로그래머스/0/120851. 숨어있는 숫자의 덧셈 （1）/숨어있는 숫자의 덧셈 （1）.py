def solution(my_string):
    answer = 0
    for i in my_string:
        if 48 <= ord(i) <= 57:
            answer += int(i)
    return answer