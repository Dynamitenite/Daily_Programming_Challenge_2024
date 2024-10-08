def findLeaders(arr):
    leaders = []  
    max_from_right = arr[-1]  
    leaders.append(max_from_right)  

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > max_from_right:  
            leaders.append(arr[i])  
            max_from_right = arr[i]  
  
    leaders.reverse()  
    return leaders

#Test
arr = [16, 17, 4, 3, 5, 2]
print("Leaders:", findLeaders(arr))
