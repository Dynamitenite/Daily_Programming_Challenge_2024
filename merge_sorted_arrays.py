def merge_sorted_arrays(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    for i in range(m):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
            first = arr2[0]
            j = 1
            while j < n and arr2[j] < first:
                arr2[j - 1] = arr2[j]
                j += 1
            arr2[j - 1] = first
    return arr1 + arr2  

# Test
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

result = merge_sorted_arrays(arr1, arr2)

print("Merged array:", result)
