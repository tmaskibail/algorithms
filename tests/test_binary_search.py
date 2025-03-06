from algorithms.binary_search import binary_search


def truthy(value):
    return bool(value)


def falsy(value):
    return not bool(value)


def test_binary_search():
    collection = [10, 12, 13, 19, 21, 24, 28]
    search_item = 222

    assert falsy(binary_search(collection, search_item))
