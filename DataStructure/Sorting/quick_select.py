# Time complexity: O(N) (O(n^2) baddest casr)
# Space complexity: O(N)
def quick_select(nums, k):
    if not nums:
        return None  # Gestione dei casi limite
    
    # Scegliamo un pivot (qui usiamo il valore centrale)
    pivot = nums[len(nums) // 2]
    
    # Partizioniamo l'array in un unico passaggio
    low, middle, high = [], [], []
    for num in nums:
        if num < pivot:
            low.append(num)
        elif num == pivot:
            middle.append(num)
        else:
            high.append(num)
    
    # Seleziona il gruppo giusto
    if k < len(low):
        return quick_select(low, k)
    elif k < len(low) + len(middle):
        return pivot  # Il pivot è il k-esimo elemento
    else:
        return quick_select(high, k - len(low) - len(middle))
