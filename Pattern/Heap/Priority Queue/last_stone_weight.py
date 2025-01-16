import heapq

def last_stone_weight(stones):
    """
    Calculate the weight of the last stone after smashing the two heaviest stones repeatedly.

    :param stones: List[int] - List of stone weights.
    :return: int - Weight of the last remaining stone, or 0 if all stones are destroyed.

    Steps:
    1. Convert stones to a max-heap by negating their weights.
    2. Extract the two largest stones repeatedly and smash them.
    3. If a stone remains, reinsert it into the heap.
    4. Return the last stone's weight or 0 if no stones remain.

    Time Complexity:
    - Building the heap: O(n)
    - Each extraction and insertion: O(log n)
    - Total for n stones: O(n log n)

    Space Complexity:
    - The heap requires O(n) space for the list of stones.

    Example:
    last_stone_weight([2, 7, 4, 1, 8, 1]) -> 1
    """
    # Step 1: Convert all stones to negative to simulate a max-heap
    stones = [-stone for stone in stones]
    heapq.heapify(stones)  # O(n) to create the heap

    # Step 2: Smash stones until one or none are left
    while len(stones) > 1:
        # Extract the two heaviest stones (most negative values)
        heaviest = heapq.heappop(stones)  # O(log n)
        second_heaviest = heapq.heappop(stones)  # O(log n)

        # Step 3: If there's a difference, reinsert the new stone
        if heaviest != second_heaviest:
            heapq.heappush(stones, heaviest - second_heaviest)  # O(log n)

    # Step 4: Return the last remaining stone (invert sign back) or 0
    return -stones[0] if stones else 0
