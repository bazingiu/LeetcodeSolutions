import heapq

class Solution:
    """
    A class used to find the k closest points to the origin.
    Methods
    -------
    calculate_distance(point)
        Calculates and returns the squared Euclidean distance of a point from the origin.
    k_closest(points, k)
        Returns the k closest points to the origin from a list of points using a max-heap.
    Complexity:
    - The time complexity of the k_closest method is O(N log k), where N is the number of points.
    - The space complexity is O(k) for storing the heap.
    """
    def calculate_distance(self, point):
        return point[0]**2 + point[1]**2

    def k_closest(self, points, k):
        # Step 1: Create a max-heap with the first k points
        max_heap = [(-self.calculate_distance(point), point) for point in points[:k]]
        # Time complexity: O(k) for creating the list
        
        heapq.heapify(max_heap)
        # Time complexity: O(k) for heapifying the list

        # Step 2: Iterate through the remaining points
        for point in points[k:]:
            distance = self.calculate_distance(point)
            # Time complexity: O(1) for calculating the distance
            if -distance > max_heap[0][0]:
                heapq.heappushpop(max_heap, (-distance, point))
                # Time complexity: O(log k) for heappushpop operation

        # Step 3: Extract the k closest points from the heap
        return [point for _, point in max_heap]
        # Time complexity: O(k) for creating the final list

