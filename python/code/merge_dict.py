dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} 

dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50 }


# print(dict1 | dict2)
# print({**dict1, **dict2})

def merge_dict(dict1, dict2):
    return dict1 | dict2

answer = merge_dict(dict1=dict1, dict2=dict2)
print(answer)