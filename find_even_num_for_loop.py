
list_number = [2, 3, 4, 7, 8, 9]
list_evn = []
def func_get_even(lst_num):
    for i in lst_num:
        if i % 2 == 0:
            list_evn.append(i)
    return list_evn


list_even = func_get_even(list_number)
print(list_even)

