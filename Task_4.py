stra = 'qqqwwgggg'

ls = list()
for i in stra:
    ls.append(i)

my_list = {}
for elem in ls:
    my_list[elem] = my_list.get(elem, 0) + 1
print(my_list)

            