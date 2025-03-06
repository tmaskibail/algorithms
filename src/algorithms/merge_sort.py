def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    if right:
        result += right
    return result


def merge_sort(collection):
    if len(collection) <= 1:
        return collection

    middle = len(collection) // 2
    collection_left = collection[:middle]
    collection_right = collection[middle:]

    merged_collection_left = merge_sort(collection_left)
    merged_collection_right = merge_sort(collection_right)

    output = merge(merged_collection_left, merged_collection_right)
    return output
