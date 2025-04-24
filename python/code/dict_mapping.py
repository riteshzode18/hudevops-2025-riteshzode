Keys = ["Ten", "Twenty", "Thirty"] 

Values = [10,20,30] 


def map_two_list(keys, values):
    di = {}
    for key, val in zip(keys, values):
        di[key] = val

    return di  


answer = map_two_list(keys=Keys, values=Values)
print(answer)



