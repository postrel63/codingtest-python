def main():
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    numbers.sort(reverse=True)
    print(numbers)

main()

'''
3
15
27
12
'''

