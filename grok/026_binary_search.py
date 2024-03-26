from typing import TypeVar

T = TypeVar('T')


def binary_search(li: list[T], value: T) -> bool:
    """
    Сложность O(log(n))
    """
    low, high = 0, len(li) - 1
    while low <= high:
        print(f'{low} -> {high}: {li[low:high + 1]}')
        new_index = (low + high) // 2
        if li[new_index] == value:
            return True
        if li[new_index] < value:
            low = new_index + 1
        else:
            high = new_index - 1
    return False


print(binary_search([1, 2, 4, 6, 9, 12, 45, 56, 88, 98], 7))
# False

print(binary_search([1, 2, 4, 6, 9, 12, 45, 56, 88, 98], 6))
# True
