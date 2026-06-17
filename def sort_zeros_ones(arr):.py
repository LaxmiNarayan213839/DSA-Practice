def sort_zeros_ones(arr):
    count_zero = arr.count(0)

    for i in range(len(arr)):
        if i < count_zero:
            arr[i] = 0
        else:
            arr[i] = 1

    return arr


arr = [1, 0, 1, 0, 0, 1, 1, 0]
print(sort_zeros_ones(arr))