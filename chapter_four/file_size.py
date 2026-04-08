def sum_nested_list(lst):
    total = 0

    for item in lst:
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):
            total += sum_nested_list(item)
        else:
            raise TypeError(f"Unsupported item type: {type(item).__name__}")

    return total
