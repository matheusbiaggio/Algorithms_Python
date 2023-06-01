def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)
    sort_first_string = merge_sort(first_string)
    sort_second_string = merge_sort(second_string)
    if len(first_string) != len(second_string):
        return ("".join(sort_first_string), "".join(sort_second_string), False)

    for i in range(len(sort_first_string)):
        if sort_first_string[i] != sort_second_string[i]:
            return (
                "".join(sort_first_string),
                "".join(sort_second_string),
                False,
            )

    return ("".join(sort_first_string), "".join(sort_second_string), True)


teste = is_anagram("aaadepr", "aaadepra")
print(teste)
