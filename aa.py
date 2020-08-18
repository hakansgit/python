big_arr = [[5, 10, 1970], [6, 15, 1980], [7, 20, 1990]] 

# for i, inn_arr in enumerate(big_arr):
#    big_arr[i] = "/".join([str(el) for el in inn_arr])

# print(big_arr)

print(["/".join([str(el) for el in inn_arr]) for inn_arr in big_arr])