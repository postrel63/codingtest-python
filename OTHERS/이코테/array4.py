def main():
    n, m = map(int, input().split(' '))
    arrayA = list(map(int, input().split(' ')))
    arrayB = list(map(int, input().split(' ')))

    arrayA.sort()
    arrayB.sort(reverse=True)

    for i in range(m):
        arrayA[i] = arrayB[i]

    print(arrayA)


main()

'''
5 3
1 2 5 4 3
5 5 6 6 5
'''
