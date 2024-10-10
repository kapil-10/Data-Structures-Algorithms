import random # import random module to generate random numbers

input_list = []

for value in range(10):
    random_num = random.randint(1,100)
    input_list.append(random_num)
print ('The list before performing insertio sort ',input_list)

def insertion_sort(input_list):
    for index in range(1,len(input_list)):
        i = input_list[index]
        j = index - 1 # set j to index - 1 to get the previous element's index

        while j >= 0 and i < input_list[j]: #  (while j>=0 ) ensures we do not try to access invalid negative indices when comparing elements in the list
            input_list[j+1] = input_list[j]
            j -= 1 # j is now -1. This is valid in Python, but it indicates that you have gone past the start of the list. The loop condition (j >= 0) is now false, so you exit the loop
        input_list[j+1] = i
    return print('The list after performing insertion sort ',input_list)

if __name__ == '__main__':
    insertion_sort(input_list)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6] ]
    for elements in tests:
        insertion_sort(elements)