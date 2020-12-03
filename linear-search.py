print('enter the array elements')
arr=list(map(int,input().split()))
print('enter the key')
key=int(input())
'''if key not in arr:
    print("val not present")
else:
    print("val present at {}".format(arr.index(key)))'''

'''alter'''

for i in range(len(arr)):
    if arr[i] == key:
        print("value found at "+str(i))

    print("value not found")