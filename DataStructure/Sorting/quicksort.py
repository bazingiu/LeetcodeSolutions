def quicksort(nums):
    if len(nums) <= 1:  # Caso base: array vuoto o con un solo elemento
        return nums
    
    # Scelta del pivot (ad esempio il primo elemento)
    pivot = nums[0]
    
    # Partiziona l'array in base al pivot
    left = [num for num in nums[1:] if num <= pivot]  # Elementi minori o uguali al pivot
    right = [num for num in nums[1:] if num > pivot]  # Elementi maggiori del pivot
    
    # Ricorsione su left e right
    return quicksort(left) + [pivot] + quicksort(right)

# Array di esempio
arra = [1, 65, 2, 3, 243]
print(quicksort(arra))
