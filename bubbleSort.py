
##Bubble sort algorithm

def bbsort(arr):
    for xindex in range(len(arr)-1):
        for yindex in range(xindex+1, len(arr)):
            if(arr[xindex]>arr[yindex]):
                tmp = arr[xindex]
                arr[xindex]=arr[yindex]
                arr[yindex]= tmp
    return arr

arr = [2, 1, 5, 6, 3, 4, 9, 8, 11, 7, 10]
sort = bbsort(arr)
print(sort)