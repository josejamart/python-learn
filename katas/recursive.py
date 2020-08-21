def BinarySearch(value, list):
    print(f"v: {value}")
    return BinarySearchInternal(0, len(list), value, list)

def BinarySearchInternal(start, end, value, list):
    print(f"s: {start} e:{end}")
    middle = int(((end - start) / 2) + start)
    print(middle)
    if start > end or start < 0 or end >= len(list):
        return -1

    if value == list[middle]:
        return middle
    elif value < list[middle]:
        return BinarySearchInternal(start, middle-1, value, list)
    else:
        return BinarySearchInternal(middle+1, end, value, list)
    return -1