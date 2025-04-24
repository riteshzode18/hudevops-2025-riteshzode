
user_input = [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]] 
# user_input = input()

## find suplicate in single list
def find_duplicate_in_single_list(lst):
    di = {}
    for i in lst:
        if i not in di:
            di[i] = 0
        di[i] += 1

    # print(di)    
    temp = []

    for key, value in di.items():
        if value > 1:
            temp.append(f"{key} -> {value}")        

    return temp

for j in user_input:
    # print(j)
    output = find_duplicate_in_single_list(j)
    print(", ".join(output))