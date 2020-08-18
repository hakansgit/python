numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
most_freq, count = (0, 0)

for num in numbers:
    num_count = numbers.count(num)
    if num_count > count:
        most_freq = num
        count = num_count

print(
    f"the most frequent number is {most_freq} and it was {count} times repeated")

# a = {
#     'dic1': {
#         'key1': 'value1',
#         'key2': 'value2'
#     },
#     'arr1': [0, 2, 4],
#     'anum': 1
# }

# print(a)