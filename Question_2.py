def count_pos_sum_neg(numbers):
    pos_count_list = [num for num in numbers if num > 0]
    neg_list = [num for num in numbers if num < 0]
    print([len(pos_count_list), sum(neg_list)])
    return [len(pos_count_list), sum(neg_list)]

count_pos_sum_neg([1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15])

    # for some reason the return command doesnt show up in the terminal.
    # so I have to use print() to see the answer.
