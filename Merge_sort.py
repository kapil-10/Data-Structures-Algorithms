def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    mid = len(unsorted_list) // 2
    left = unsorted_list[ : mid]
    right = unsorted_list[ mid : ]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_list(left,right)
def merge_two_sorted_list (sorted_list_a,sorted_list_b):
    len_a = len(sorted_list_a)
    len_b = len(sorted_list_b)
    i = j = 0 
    sorted_list = []
    while i < len_a and j < len_b: # iterate through the end of the list
        if sorted_list_a[i] <= sorted_list_b[j]:
            sorted_list.append(sorted_list_a[i])
            i += 1
        else:
            sorted_list.append(sorted_list_b[j])
            j += 1 
    while i < len_a: # add the left over elements from sorted_list_a
        sorted_list.append(sorted_list_a[i])
        i +=1
    while j < len_b: #  add the left over elements from sorted_list_b
        sorted_list.append(sorted_list_b[j])
        j +=1 

    return sorted_list

if __name__ == '__main__':
    print('using merge two sort funcation',merge_two_sorted_list([1,3,5,7,9],[2,4,6,8]))

    arr= [1,3,2,4,6,5,8,7,10,9]
    
    print ('using merge_sorf funcation :', merge_sort(arr) )
