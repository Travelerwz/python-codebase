'''
字符串转字典
字符串分割
'''
str1 = "k:1|k2:2|k3:3"
def str2dict(str):
    dict1 = {}
    for items in str.split("|"):
        key,value = items.split(':')
        dict1[key] = value
    return dict1

dict2 = str2dict(str1)
print(dict2)
