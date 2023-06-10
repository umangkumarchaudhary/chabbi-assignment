def sort_list_of_dicts(list_of_dicts, sort_key):
    sorted_list = sorted(list_of_dicts, key=lambda x: x[sort_key])
    return sorted_list

list_of_dicts = []
num_dicts = int(input("Enter the number of dictionaries: "))
for i in range(num_dicts):
    print(f"Dictionary {i+1}:")
    fruit = input("Enter the fruit: ")
    color = input("Enter the color: ")
    dict_item = {"fruit": fruit, "color": color}
    list_of_dicts.append(dict_item)

sort_key = input("Enter the sort key (fruit or color): ")

sorted_list = sort_list_of_dicts(list_of_dicts, sort_key)
print(sorted_list)
