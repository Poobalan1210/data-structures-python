
def bsearch(arr,l,r,k):
    mid=l+(r-l)//2
    if r >= l:
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return bsearch(arr,l,mid-1,k)
        else:
            return bsearch(arr,mid+1,r,k)
    else:
     return 0






if __name__ =="__main__":
    print("enter the sorted array ")
    n=list(map(int,input().split()))
    print('enter the key val')
    k=int(input())
    result = bsearch(n,0,len(n)-1,k)
    if result:
        print("val is found at "+str(result))
    else:
        print("val not found")