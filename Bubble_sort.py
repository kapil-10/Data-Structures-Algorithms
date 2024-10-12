def bubble_sort(unsorted_list): # Takes unsorrted_list
    length = len(unsorted_list)
    for element in range (length-1): # check till last second element in the list
        swapped = False # setting up  a flag. if no swapped is performed which means the list is sorted 
        for value in range(length - 1 - element): # here - element is optional . we dont have to check the elements till the end of the list if they are sorted
            if unsorted_list[value] > unsorted_list[value + 1]:
                temp = unsorted_list[value]
                unsorted_list[value] = unsorted_list[value + 1]
                unsorted_list[value + 1] = temp
                swapped = True
        if not swapped:
            break
    return unsorted_list
                

if __name__ == '__main__':
    x = [5,2,1,9,34,67,34,88]
    print(bubble_sort(x))
