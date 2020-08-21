def BinarySearch(value, list):
    start = 0
    end = len(list)
    while start < (end -1):
        print(f"s: {start} e:{end}")
        middle = int(((end - start) / 2) + start)
        if value == list[middle]:
            return middle

        if value < list[middle]:
            end = middle
        else:
            start = middle
    return -1

