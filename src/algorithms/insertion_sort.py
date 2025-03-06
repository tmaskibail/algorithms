def insertion_sort(collection: list[int]) -> list[int]:
    local_collection = collection.copy()
    i = 0
    while i < len(local_collection):
        j = i
        x = local_collection[i]

        while (j > 0) and (local_collection[j - 1] > x):
            local_collection[j] = local_collection[j - 1]
            j = j - 1

        local_collection[j] = x
        i = i + 1

    return local_collection
