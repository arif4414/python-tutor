from functools import reduce

list_number = [2, 3, 4, 7, 8, 9]


def is_even(n):
    return n % 2 == 0


# filter is to get some data from list of data
list_even_num = list(filter(is_even, list_number))
print(list_even_num)

lst_even_with_lambda = list(filter(lambda n: n % 2 == 0, list_number))

print('lambda result: ', lst_even_with_lambda)


# map: does some operation like add/subtract or anything else on the filtered data

def update(n):
    return n + 2


updated_data_with_map = list(map(update, lst_even_with_lambda))  # using update function
print('data after map', updated_data_with_map)

updated_data_with_map_lambda = list(map(lambda n: n * 2, lst_even_with_lambda))
print('data after map with lambda', updated_data_with_map_lambda)


# reduce: gets the summarized final data like average/sum etc from whatever map returns

def sum(a, b):
    return a + b


# for sum we need 2 arguments

sum_final_with_reduce = reduce(sum, updated_data_with_map_lambda)
print('data after reduce', sum_final_with_reduce)
sum_final_with_reduce_lambda = reduce(lambda a, b: a + b, updated_data_with_map_lambda)
print('data after reduce with lambda', sum_final_with_reduce_lambda)
