from algorithms.merge_sort import merge_sort


def test_merge_sort():
    x = [1, 2, 3, 4, 5, 6]
    assert x == merge_sort([6, 5, 4, 3, 2, 1])
