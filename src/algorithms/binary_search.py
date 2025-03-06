def binary_search(collection: list[int], search_item: int) -> bool:
    """ Run time :: O(log n) vs O(n) when searched against n items"""

    low = 0
    high = len(collection) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = collection[middle]

        if search_item < guess:
            high = middle - 1
        elif search_item > guess:
            low = middle + 1
        else:
            return True

    return False
