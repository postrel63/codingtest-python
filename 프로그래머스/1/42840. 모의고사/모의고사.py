def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [[1, 0], [2, 0], [3, 0]]
    an = []
    
    for i, answer in enumerate(answers):
        if answer == one[i % len(one)]:
            score[0][1] += 1
        if answer == two[i % len(two)]:
            score[1][1] += 1
        if answer == three[i % len(three)]:
            score[2][1] += 1

    score.sort(key=lambda x: x[1], reverse=True)
    for i, sc in score:
        if score[0][1] == sc:
            an.append(i)

    return an