def swap(a, b, arr):
    if a <= b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def partition(input_list, start, end):
    pivot = start
    pivot_element = input_list[pivot]

    while start < end:
        while start < len(input_list) and input_list[start] <= pivot_element:
            start += 1

        while input_list[end] > pivot_element:
            end -= 1

        if start < end:
            swap(start, end, input_list)

    swap(pivot, end, input_list)

    return end

def quick_sort(elements, start, end):
    if start < end:
        p = partition(elements, start, end)
        quick_sort(elements, start, p - 1)
        quick_sort(elements, p + 1, end)

if __name__ == '__main__':
    arr = [11, 9, 29, 7, 2, 15, 18]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')