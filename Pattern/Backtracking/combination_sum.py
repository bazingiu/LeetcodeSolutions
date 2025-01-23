from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start: int, current_combination: List[int], current_sum: int):
            if current_sum == target:
                result.append(current_combination[:])
                return
            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(i, current_combination, current_sum + candidates[i])
                current_combination.pop()

        candidates.sort()
        result = []
        backtrack(0, [], 0)
        return result

# Time Complexity: at each level we can choose the same element multiple times or move to the next one
# each combination can have up to target/min(candidates) elements
# at each level we have n choices
# O(n^(target/min(candidates)))
# each time we need to copy the list which takes k time where k is <= target/min(candidates)
# O(n^(target/min(candidates)) * k)

# Space Complexity: O(target/min(candidates)) for the combination list
# we need to store the combination list and the partial combination list

            
    