import time
def time_it_decorator(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print('The time it took is :',end_time - start_time)
        return result
    return wrapper


@time_it_decorator
def linear_search(list_values,target):
    for index , value in enumerate (list_values):
        if value == target:
             return print('value found at index :',index, ' The value is :',value)
    else:
        print('not found')


@time_it_decorator
def binary_search(sorted_list_values,target):
    left_pointer = 0
    right_pointer = len(sorted_list_values) - 1
    mid_pointer = 0 

    while left_pointer <= right_pointer:
        mid_pointer = (left_pointer + right_pointer) // 2
        mid_number = sorted_list_values[mid_pointer]

        if right_pointer < left_pointer:
            return -1

        elif mid_number == target:
            return print('value found at index :',mid_pointer,'the value is :',mid_number)
        
        elif target > mid_number:
            left_pointer = mid_pointer + 1
        
        else:
            if target < mid_number:
                right_pointer = mid_pointer - 1
    print('value ot found')
    return -1


@time_it_decorator
def binary_search_recurssion(sorted_list_values,target,left_pointer,right_pointer):

    mid_pointer = (left_pointer + right_pointer) // 2
    mid_number = sorted_list_values[mid_pointer]

    if mid_number == target:
        return print('value found at index :',mid_pointer,'the value is :',mid_number)

    elif target > mid_number:
        left_pointer = mid_pointer + 1

    else:
        if target < mid_number:
            right_pointer = mid_pointer - 1
    return binary_search_recurssion(sorted_list_values,target,left_pointer,right_pointer)



if __name__ == '__main__':
    arr = [23,56,89,67,44,9,35,22]
    print(linear_search(arr,35))

    arr_bs = sorted(arr)
    print(binary_search(arr_bs,89))

    print(binary_search_recurssion(arr_bs,67,0,len(arr_bs)-1))