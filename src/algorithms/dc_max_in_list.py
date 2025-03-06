def max_in_list(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    else:
        return max(max_in_list(lst[:len(lst) // 2]), max_in_list(lst[len(lst) // 2:]))
    