def find_duplicate(arr):
    n = len(arr) - 1  
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(arr)  #
    duplicate = actual_sum - expected_sum  
    return duplicate

# Test
arr = [3, 1, 3, 4, 2]
print("Duplicate Number:", find_duplicate(arr))
