from algorithms.insertion_sort import insertion_sort


def test_insertion_sort():
    collection = [23, 1, 34, 2]
    sorted_collection = insertion_sort(collection)

    assert [1, 2, 23, 34] == sorted_collection
