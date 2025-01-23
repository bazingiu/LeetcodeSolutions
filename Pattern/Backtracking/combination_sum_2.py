def combination_sum_2(candidates, target):
    results = []
    candidates.sort()
    
    def backtrack(start_index, current_combination, current_sum):
        print(f"Start Index: {start_index}, Current Combination: {current_combination}, Current Sum: {current_sum}")
        if current_sum == target:
            results.append(current_combination[:])
            print(f"Found combination: {current_combination}")
            return

        for i in range(start_index, len(candidates)):
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue
            if current_sum + candidates[i] > target:
                break
            current_combination.append(candidates[i])
            backtrack(i + 1, current_combination, current_sum + candidates[i])
            current_combination.pop()

    backtrack(0, [], 0)
    return results

# Esempio di chiamata alla funzione
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combination_sum_2(candidates, target))
# Time complexity: O(2^n), where n is the number of candidates. In the worst case, each candidate can be included or excluded.
# Space complexity: O(n), where n is the number of candidates. This is due to recursion and storing the current combinations.
