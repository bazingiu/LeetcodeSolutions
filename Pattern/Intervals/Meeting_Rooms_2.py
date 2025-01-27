"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    This class provides a solution to the problem of finding the minimum number of meeting rooms required.
    Methods
    -------
    minMeetingRooms(intervals: List[Interval]) -> int
        Given a list of meeting time intervals consisting of start and end times, returns the minimum number of meeting rooms required.
    Parameters
    ----------
    intervals : List[Interval]
        A list of intervals where each interval has a start and end time.
    Returns
    -------
    int
        The minimum number of meeting rooms required to accommodate all meetings.
    Time Complexity: O(n log n), where n is the number of intervals. This is due to the sorting of start and end times.
    Space Complexity: O(n), where n is the number of intervals. This is due to the storage of start and end times.
    """
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = sorted([interval.start for interval in intervals])
        end_times = sorted([interval.end for interval in intervals])
        
        num_intervals = len(intervals)
        max_rooms = 0
        current_rooms = 0
        start_pointer = 0
        end_pointer = 0

        while start_pointer < num_intervals:
            if start_times[start_pointer] < end_times[end_pointer]:
                current_rooms += 1
                max_rooms = max(max_rooms, current_rooms)
                start_pointer += 1
            else: 
                current_rooms -= 1
                end_pointer += 1
        return max_rooms
