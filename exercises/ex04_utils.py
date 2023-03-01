"""EX04 - lists."""

__author__ = "730384690"

def all(input: list[int], number: int) -> bool:
    """Check if integer is in list"""
    count: int = 0
    if len(input) == 0:
        return False
    while count < len(input):
        if number != input[count]:
            return False
        count += 1
    return True

def max(input: list[int]) -> int:
    """Given a list of integers return the max."""
    max: int = input[0]
    count: int = 1
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while count < len(input):
        if max < input[count]:
            max = input[count]
        count += 1
    return max

def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Comparison of indexes of the two lists"""
    count: int = 0
    if len(list_one) != len(list_two):
        return False
    while count < len(list_one):
        if list_one[count] == list_two[count]:
            count = count + 1
        else:
            return False
        return True
    