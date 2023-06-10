def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    uncommon_elements = list(set(list1) ^ set(list2))
    return common_elements, uncommon_elements

list1 = input("Enter elements for the first list (comma-separated): ").split(",")

list2 = input("Enter elements for the second list (comma-separated): ").split(",")

common, uncommon = compare_lists(list1, list2)
print("Common elements:", common)
print("Uncommon elements:", uncommon)
