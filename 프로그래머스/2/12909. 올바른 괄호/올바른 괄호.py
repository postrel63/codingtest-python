
def solution(s):
    stack = []
    for i in s:
        print(i)
        if stack and stack[-1] == "(" and i == ")":
            stack.pop()
        else:
            stack.append(i)
    
    if stack :
        return False

    return True