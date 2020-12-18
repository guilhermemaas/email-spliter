def return_two_lists():
    list1 = ['xpto', 'xpto1']
    list2 = ['abc', 'abc1']
    return (list1, list2)


list_1 = []
list_2 = []
list_1, list_2 = return_two_lists()

print(f'list_1: {list_1}')
print(f'list_2: {list_2}')