def recursion_max(arr, i):
    # if the current element is the last
    if i >= len(arr) - 1:
        # return the current/last
        return arr[i]
    else:
        # get the maximum of the next the current array except the current
        max_in_sub = recursion_max(arr, i + 1)
        # if the maximum in the is greater than the current
    if max_in_sub > arr[i]:
        return max_in_sub
        # if the maximum in the sub array is smaller than the current element, return the non sub array
    else:
        return arr[i]

#runner code
arr = [42, 0, 9, 45, 7, -20]
print('List: ', arr)
print('Largest Element: ', recursion_max(arr, 0))