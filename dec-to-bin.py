from stack import  stack

def convert_int_to_bin(dec_num):
    while dec_num >0:
        d=dec_num%2
        s.push(int(d))
        dec_num=dec_num//2


if __name__ =="__main__":
    dec=int(input())
    s=stack()
    convert_int_to_bin(dec)
    #print(s.print())
    str1=""
    for i in range(len(s.items)):
        x=s.pop()
        str1 += str(x)
    print(str1)

