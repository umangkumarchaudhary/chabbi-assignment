def get_sublist(lst, start_index, end_index):
    sublist = lst[start_index:end_index:2]
    return sublist

lst = input("Enter elements for the list (comma-separated): ").split(",")

start_index = int(input("Enter the start index: "))

end_index = int(input("Enter the end index: "))

result = get_sublist(lst, start_index, end_index)
print("Sublist:", result)

