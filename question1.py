def selection_sort(arr):
    
    sorted_arr = list(arr)
    
    
    for i in range(len(sorted_arr)):
        min_idx = i
        
        
        for j in range(i + 1, len(sorted_arr)):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j
        
        
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    
    return sorted_arr
