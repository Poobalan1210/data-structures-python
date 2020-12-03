from stack import stack



if __name__ == '__main__':
    s=stack()
    str=input()
    bo=['(','{','[']
    bc=[')','}',']']
    for char in str:
        if char in bo:
            s.push(char)
        if char in bc:
            if s.peek() == '(' and char == ')':
                s.pop()
            elif s.peek() == '{' and char == '}':
                s.pop()
            elif s.peek() == '[' and char == ']':
                s.pop()
            elif s.isempty():
                s.push(char)

    if s.isempty():
        print("it is balanced")
    else:
        print("it is unbalanced")

