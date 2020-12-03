from stack import stack

if __name__ =="__main__":
    st=input()
    s=stack()
    for char in st:
        s.push(char)

    str="".join([c for i in range(len(st)) c=s.pop()])
    '''for i in range(len(st)):
        if s.isempty():
            print("no string")
        c = s.pop()
        str +=c'''

    print(str)
