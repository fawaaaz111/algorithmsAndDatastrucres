def linear_search(list, target):
    """
    Return the index position of the target if found, else return none
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target Found at Index", index)
    else:
        print("Target Not Found")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 12)
result2 = linear_search(numbers, 7)
verify(result)
verify(result2)