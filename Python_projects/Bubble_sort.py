def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

lst = []
for i in range(10):
    lst.append(int(input("Enter the number: ")))

sorted_list = bubble_sort(lst)
print("The sorted list is:", sorted_list)


