def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    iterations = 0

    while left <= right:
        mid = (left + right) // 2
        iterations += 1

        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            return iterations, arr[mid]

    if right >= 0 and right < len(arr):
        upper_bound = arr[right]
    else:
        upper_bound = None

    return iterations, upper_bound

arr_numbers = [1.0, 2.5, 3.7, 5.2, 7.3, 8.1, 10.0]
x_value = 6.0

result = binary_search(arr_numbers, x_value)
print(result)
