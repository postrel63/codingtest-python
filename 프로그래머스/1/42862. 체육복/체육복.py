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
