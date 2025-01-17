def single_number(nums):
    """
    Finds the single number in a list where every other number appears twice.

    This function uses the XOR bitwise operation to find the unique number in the list.
    XOR-ing a number with itself results in 0, and XOR-ing a number with 0 results in the number itself.
    Therefore, XOR-ing all numbers in the list will cancel out the numbers that appear twice, leaving the unique number.

    :param nums: List[int] - A list of integers where every element appears twice except for one.
    :return: int - The single number that appears only once.

    Time Complexity: O(n), where n is the number of elements in the list.
    Space Complexity: O(1), as no additional space proportional to the input size is used.
    """
    result = 0
    for num in nums:
        result ^= num
    return result
