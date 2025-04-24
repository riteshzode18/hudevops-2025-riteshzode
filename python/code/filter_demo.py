print("1 Answer")

lst1=[-1000, 500, -600, 700, 5000, -90000, -17500] 

# mutiply by -1 to convert negative to poistive
lst = list(map(lambda x: x * -1, list(filter(lambda x: x < 0, lst1))))

# use abs method
# lst = list(map(lambda x: abs(x), list(filter(lambda x: x < 0, lst1))))

print(lst)

print("2 Answer")

lst1=["Netflix", "Hulu", "Sling", "Hbo"] 

lst2=[198, 166, 237, 125] 

def map_two_list_to_dict(lst1, lst2):
    di = {}
    for key, val in zip(lst1, lst2):
        di[key] = val

    return di  

answer = map_two_list_to_dict(lst1=lst1, lst2=lst2)
print(answer)

