
def binary_search(arr, low, high, x):
    if len(arr) == 1:
        if arr[0] < x:
            return 1
        return 0

    if high >= low:
        mid = (high + low) // 2
        if mid == high:
            if high == 0:
                return mid if arr[mid] >= x else mid + 1
            return mid if arr[mid] >= x else mid + 1
        if arr[mid] <= x and x <= arr[mid + 1]:
            return mid if arr[mid] == x else mid + 1
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, high, x)
    return low


def insert(arr, x):
    index = binary_search(arr, 0, len(arr) - 1, x)
    arr.insert(index, x)
    return arr


if __name__ == '__main__':
    arr = [1, 3, 9, 34]
    low = 0
    high = len(arr) - 1
    x = 35
    print(insert(arr=arr, x=x))
