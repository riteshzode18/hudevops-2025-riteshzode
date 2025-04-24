list1 = ["Hello ", "take "] 

list2 = ["Dear", "Sir"] 


def merge_two_list(list1, list2):
    
    temp = []
    for i in list1:
        for j in list2:
            temp.append(i + j)

    return temp


answer = merge_two_list(list1=list1, list2=list2)
print(answer)
