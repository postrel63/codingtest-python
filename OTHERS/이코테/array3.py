def main():
    n = int(input())
    arr = [input().split(' ') for x in range(n)]

    arr.sort(key= lambda x : x[1])
    print(arr)

main()

'''
2
홍길동 95
이순신 77
'''