l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def sort_merge_list(list_1, list_2):
    merged_list = list_1 + list_2
    merged_list.sort()
    print(merged_list)

sort_merge_list(l_1, l_2)