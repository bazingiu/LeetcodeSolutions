# Time complexity: O (n^2)
def tre_sum(nums):
    result = []
    
    nums.sort() # O(nlogn)
    
    for index, num in enumerate(nums):  # O(n)
        # Skip duplicate values
        if index > 0 and nums[index] == nums[index - 1]:
            continue
        
        # Two pointers for the remaining part of the array
        start = index + 1
        end = len(nums) - 1
        while start < end: #O(N)
            current_sum = num + nums[start] + nums[end]
            if current_sum == 0:
                # Add the triplet to the result list
                result.append([num, nums[start], nums[end]])
                # Move the pointers and skip duplicates
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1
            elif current_sum < 0:
                # Move the start pointer to increase the sum
                start += 1
            else:
                # Move the end pointer to decrease the sum
                end -= 1
    
    return result
    
    