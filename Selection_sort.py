def find_min_number(input_list):
    length = len(input_list)
    min = 1000
    for value in range (length):
        if input_list[value] < min :
            min = input_list[value]
    return min


def selection_sort(unsorted_list):
    length = len(unsorted_list)
    for i in range(length):# [4,9,29,17,21,25,11,32,28]
        min_index = i # currently 2
        for j in range (min_index + 1 , length): # currently pointing at index 3
            if unsorted_list[j] < unsorted_list[min_index]: # found 11
                min_index = j # 
        temp = unsorted_list[i] # 29
        unsorted_list[i] = unsorted_list[min_index] # 11
        unsorted_list[min_index] = temp
    return unsorted_list

if __name__ == '__main__':
    check = [1,2,3,4,5,6,7,8,9]
    print( find_min_number(check))

    tests = [
    [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
    [],
    [1,5,8,9],
    [234,3,1,56,34,12,9,12,1300],
    [78, 12, 15, 8, 61, 53, 23, 27],
    [5]
]
    for test in tests:
        print( selection_sort(test))
