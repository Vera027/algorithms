# bubble sort
def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list


my_list = [2, 4, 6, 10, 3, 9, 1]
bubble_sort(my_list)
print(my_list)


# selection sort
def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


my_list1 = [2, 0, 3, 9, 10, 16, 5]
selection_sort(my_list1)
print(my_list1)


# insertion sort
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > - 1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


list2 = [2, 1, 0, 20, 39, 3, 7]
insertion_sort(list2)
print(list2)


# merge sort
def merge(my_list1, my_list2):
    combined = []
    i = 0
    j = 0
    while i < len(my_list1) and j < len(my_list2):
        if my_list1[i] < my_list2[j]:
            combined.append(my_list1[i])
            i += 1
        else:
            combined.append(my_list2[j])
            j += 1
    while i < len(my_list1):
        combined.append(my_list1[i])
        i += 1
    while j < len(my_list2):
        combined.append(my_list2[j])
        j += 1
    return combined


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list) / 2)
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left), merge_sort(right))


my_list3 = [1, 5, 8, 9, 10, 2, 4]
print(merge_sort(my_list3))


# quick sort
def swap(unsorted_list, index1, index2):
    temp = unsorted_list[index1]
    unsorted_list[index1] = unsorted_list[index2]
    unsorted_list[index2] = temp


def pivot(unsorted_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if unsorted_list[i] < unsorted_list[pivot_index]:
            swap_index += 1
            swap(unsorted_list, swap_index, i)
    swap(unsorted_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(unsorted_list, left, right):
    if left < right:
        pivot_index = pivot(unsorted_list, left, right)
        quick_sort_helper(unsorted_list, left, pivot_index - 1)
        quick_sort_helper(unsorted_list, pivot_index + 1, right)
    return unsorted_list


def quick_sort(unsorted_list):
    return quick_sort_helper(unsorted_list, 0, len(unsorted_list) - 1)


my_list4 = [1, 4, 3, 5, 19, 6]
print(quick_sort(my_list4))




            








