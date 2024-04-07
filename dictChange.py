dict0 = {}

dict1 = {2:3, 5:6, 8:9}

dict2 = {2:3, 5:3, 8:3}

dict3 = {"a": "aa", "b": "bb", "c": "aa"}
dict4 = {"b": "aa", "b": "bb", "c": "aa"}


def key_value_change(dictarg: dict) -> dict: 
    returndict = dict()
    for elem in dictarg.keys():
        temp = dictarg[elem]
        returndict[temp] = elem
    return returndict 

print(key_value_change(dict0))
print(key_value_change(dict1))
print(key_value_change(dict2))
print(key_value_change(dict3))
print(key_value_change(dict4))

print(dict0)
print(dict1)
print(dict2)
print(dict3)
print(dict4)
