"""
n만큼 배열을 생성하고, default = 1, lost는 요소는 -1, reserve는 +1 해줌
배열을 순회하면서 2를 만나면 앞 뒤 요소가 0인경우 그 요소를 1로 추가하고 자기는 -1
range 범위를 넘지 않도록 맨 앞과 맨 뒤의 예외처리를 해줘야 함( i > 0, i + 1 < n )
1번 예제 배열 예시 : [2 0 2 0 2]

n개의 배열에서 0이 아닌 경우는 모두 체육 수업을 들을 수 있는 경우.

"""

def solution(n, lost, reserve):
    students = [1] * n
    for i in lost:
        students[i - 1] -= 1
    for i in reserve:
        students[i - 1] += 1

    for i in range(n):
        if students[i] == 2:
            if i > 0 and students[i - 1] == 0:
                students[i] -= 1
                students[i - 1] += 1
            elif i + 1 < n and students[i + 1] == 0:
                students[i] -= 1
                students[i + 1] += 1

    return n - students.count(0)
