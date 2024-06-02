def solution(sizes):
    max_w = 0
    max_y = 0
    for sublist in sizes:
        sublist.sort(reverse=True)
    sizes.sort(key = lambda x : x[0], reverse=True)
    max_w = sizes[0][0]
    sizes.sort(key = lambda x : x[1], reverse=True)
    max_h = sizes[0][1]

    return max_w * max_h


