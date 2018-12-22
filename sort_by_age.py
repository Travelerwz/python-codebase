'''
元祖中字典元素排序
按照关键字排序，倒序
'''

alist = [{'name':'a','age':20},{'name':'b','age':26},{'name':'c','age':22}]

def sort_by_age(list1):
    return sorted(list1,key = lambda x:x['age'],reverse=True)

result = sort_by_age(alist)
print(result)
