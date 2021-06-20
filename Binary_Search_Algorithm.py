# Muskan Gupta


def binary_search(arr, low, high, x):

    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)

    else:

        return -1


Arr = input('Enter the elements of array: ')
arr_i = Arr.split(' ')
arr = []
for i in arr_i:
    arr.append(int(i))
key = int(input('Enter the value of key to be found: '))
arr.sort()
print('Sorted Array:')
print(arr)


index = binary_search(arr, 0, len(arr)-1, key)

if index != -1:
    print(f"Successfully!! Element is present in the array at index {index}")
else:
    print("Element is not present in array!!")






