"""
Solution
Topic: Recursion & Time/Space Complexity
"""

def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])


"""
Time Complexity Analysis:

Time Complexity: O(n)
- The length of the list is n
- Each recursive call does constant time operations (accessing element at index 0)
- Therefore, overall time complexity is O(n)

""" 