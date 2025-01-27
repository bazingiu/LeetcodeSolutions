def house_robber(houses):
    prev_max, curr_max = 0, 0
    for house_value in houses:
        new_max = max(prev_max + house_value, curr_max)
        prev_max = curr_max
        curr_max = new_max
    return curr_max

# Time: O(N)
# Space: O(1)


    