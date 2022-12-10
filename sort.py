# bubble sort
def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = my_list[j]
        return my_list


list1 = [2, 4, 6, 10, 3, 9, 1]
bubble_sort(list1)
print(list1)

# selection sort
