def remove(original):
    seen = set()
    result = []
    for x in original:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result
values = ['20', '30', '40','30', 10, True, True]
unique_values = remove(values)
print(unique_values)