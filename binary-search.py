def binsearch(arr,l,r,k):
    if r >= l:
        mid = l+(r-l)//2
        if arr[mid] == k:
            return  mid
        elif arr[mid] > k:
            return binsearch(arr,l,mid-1,k)
        else:
            return binsearch(arr,mid+1,r,k)
    else:
        return 0

a=[1,2,3,4,5,6,7,8,9]
b=binsearch(a,0,len(a)-1,10)
if b != 0:
    print('element is present at '+str(b))
else:
    print('not found')