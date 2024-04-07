list0 = []

list1 = [1, -1, 0]

list2 = [1, [0, 4]]

list3 = [1, [[2, 0, 1], 4], 1000]

list4 = [1, [[2, 0, 1], 4], "1000"]


def flatten(x):
    if isinstance(x, list):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]


def transform_to_binary(list_arg) -> []:
    flatlist = flatten(list_arg)
    try:
        for i in range(len(flatlist)):
            if flatlist[i] <= 0:
                flatlist[i] = 0
            else:
                flatlist[i] = 1
    except TypeError as e:
        return e

    return flatlist


def transform_to_binary_without_range(list_arg) -> []:
    print(list_arg)
    returnlist = []
    for i in list_arg:
        print(i)
        if i <= 0:
            returnlist.append(0)
        else:
            returnlist.append(1)

    return returnlist


def transform_to_binary_map(list_arg) -> []:
    print(list_arg)
    returnlist = map(lambda x: x * x, list_arg)

    return list(returnlist)

print(transform_to_binary(list0))
print(transform_to_binary(list1))
print(transform_to_binary(list2))
print(transform_to_binary(list3))
print(transform_to_binary(list4))

# print(transform_to_binary_without_range(list11))
