def sort(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
    
#Test Case 1
arr1 = [0, 1, 2, 1, 0, 2, 1, 0]
sorted_arr1 = sort(arr1)
print(sorted_arr1)

#Test Case 2:
arr2 = [2, 2, 2, 2]
sorted_arr2 = sort(arr2)
print(sorted_arr2)

#Test Case 3:
arr3 = [0, 0, 0, 0]
sorted_arr3 = sort(arr3)
print(sorted_arr3)

