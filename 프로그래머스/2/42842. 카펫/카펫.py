# brown + yellow = width * height
# brown = (width * 2) + (height * 2) - 4
# yellow = (width / 2) * (height / 2) 
def solution(brown, yellow):
    answer = []
    total = brown + yellow

    for i in range(3, total):

        length = i
        width = int(total / length)
        if length * width != total:
            continue

        if brown == (length * 2) + (width * 2) - 4:
            if yellow == (length - 2) * (width - 2):
                return [width, length]

    return answer
