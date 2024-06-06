# brown + yellow = width * height
# brown = (width * 2) + (height * 2) - 4
# yellow = (width / 2) * (height / 2) 
def solution(brown, yellow):
    answer = []

    for i in range(3, brown + yellow):
        length = i
        width = int((brown + yellow) / length)
        if length * width != brown + yellow:
            continue

        if brown == (length * 2) + (width * 2) - 4:
            if yellow == (length - 2) * (width - 2):
                return [width, length]

    return answer
