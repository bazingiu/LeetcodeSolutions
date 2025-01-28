import heapq

# -------------------- 1. Finding the largest and smallest elements -------------------- #
nums = [3, 2, 1, 5, 6, 4]
k = 2

# Find the k largest elements
print("The", k, "largest elements:", heapq.nlargest(k, nums))  # Output: [6, 5]

# Find the k smallest elements
print("The", k, "smallest elements:", heapq.nsmallest(k, nums))  # Output: [1, 2]

# -------------------- 2. Using a max-heap with negative values -------------------- #
# To simulate a max-heap, negate all values and use heapq
neg_nums = [-n for n in nums]

# Convert the list into a heap (in-place transformation)
heapq.heapify(neg_nums)

# Pop the largest value (convert back to positive)
largest = -heapq.heappop(neg_nums)
print("Largest element using max-heap:", largest)  # Output: 6

# -------------------- 3. Removing elements in sorted order -------------------- #
# Transform nums into a heap
heapq.heapify(nums)  # Convert the list into a min-heap

print("\nElements in ascending order:")
while nums:
    print(heapq.heappop(nums))  # Remove and print elements in ascending order

# -------------------- 4. Handling tuples in heaps -------------------- #
# When using tuples, the heap is sorted by the first element of each tuple.
new = [(1, 2), (-1, 2)]
heapq.heapify(new)

# The smallest element (based on the first value of the tuple)
print("Smallest tuple based on the first value:", new[0])  # Output: (-1, 2)

# -------------------- 5. Priority Queue with heapq -------------------- #
# Priority queues can be implemented using a heap with tuples
priority_queue = []

# Add tasks with priorities (smaller priority number = higher priority)
heapq.heappush(priority_queue, (2, "task2"))
heapq.heappush(priority_queue, (1, "task1"))

print("\nPriority queue after insertion:", priority_queue)  # Output: [(1, 'task1'), (2, 'task2')]

# Remove the highest priority task
highest_priority_task = heapq.heappop(priority_queue)
print("Highest priority task:", highest_priority_task)  # Output: (1, 'task1')

# -------------------- 6. Merge multiple sorted iterables -------------------- #
# Merging two sorted lists into a single sorted iterator
sorted_list1 = [1, 3, 5]
sorted_list2 = [2, 4, 6]

merged = heapq.merge(sorted_list1, sorted_list2)
print("\nMerged sorted lists:", list(merged))  # Output: [1, 2, 3, 4, 5, 6]

# -------------------- 7. Replace and push-pop operations -------------------- #
# heapreplace() replaces the smallest element with a new value and maintains the heap invariant.
heap = [4, 5, 8, 9]
heapq.heapify(heap)

# Replace the smallest element with a new value
replaced = heapq.heapreplace(heap, 3)
print("\nReplaced smallest element:", replaced)  # Output: 4
print("Heap after replacement:", heap)  # Output: [3, 5, 8, 9]

# Push a new value and pop the smallest value in a single operation
popped = heapq.heappushpop(heap, 2)
print("Push-pop operation result:", popped)  # Output: 2
print("Heap after push-pop:", heap)  # Output: [3, 5, 8, 9]

# -------------------- 8. Additional Notes -------------------- #
# - heapq operations have time complexity O(log n) for push and pop.
# - Use `heapq.heapify` for in-place transformation of a list into a heap (O(n) complexity).
# - `heapq.merge` is useful for merging multiple sorted inputs without fully sorting them.

# Example of heapify and extraction
example_list = [7, 3, 5, 1, 9]
heapq.heapify(example_list)
print("\nHeapified list:", example_list)  # Min-heap: [1, 3, 5, 7, 9]

print("Extracted elements in ascending order:")
while example_list:
    print(heapq.heappop(example_list))  # Prints elements in sorted order
