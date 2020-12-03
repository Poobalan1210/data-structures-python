def bsearchwithoutrecurrision(arr,l,r,k):
    while r >= l:
        mid=l+(r-l)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            r=mid-1
        else:
            l=mid+1
    else:
        return 0



if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = bsearchwithoutrecurrision(a, 0, len(a) - 1, 6)
    if b != 0:
        print('element is present at ' + str(b))
    else:
        print('not found')