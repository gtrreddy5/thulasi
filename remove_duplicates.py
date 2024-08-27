##########Remove anydata duplicates without using function#################
# values = ['20', '30', '40','30', 10]
# unique_values = list(dict.fromkeys(values))
# print(unique_values)
# ##########Remove anydata duplicates using function#################
def remove_duplicates(original_list):
    seen = set()
    result = []
    for item in original_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
values = ['20', '30', '40','30', 10,'True','True']
unique_list = remove_duplicates(values)
print(unique_list)

##########Remove string duplicates without function#################
# data = "hammer"
# unique_string = ''.join(sorted(set(data),key = data.index))
# print("string without duplicates:",unique_string)

##########Remove string duplicates using function#################
# def remove_duplicates(original):
#     unique_string = ''.join(sorted(set(original),key = original.index))
#     print("string without duplicates:",unique_string)
# data = "hammer"
# result = remove_duplicates(data)

