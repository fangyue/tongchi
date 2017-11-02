# this file contains the matching algorithm for finding lunchmates
# query_set is the set that satisfies the location requirement.
# two simple matching algorithms:
# 1. simple shuffle and return the group
# 2. bruceforce to find out the best matching
# since we only support 2 people group for now, Algorithm 2 is used.

import data_util
import const
from random import shuffle

def update_request_in_2_people_group(request_1,request_2):
    data_util.set_matched_result(request_1, request_2.user_id)
    data_util.set_matched_result(request_2, request_1.user_id)


def update_request_in_group(group_list):
    if (len(group_list) != 2):
        raise ValueError('Cannot support more than 2 group matching yet')
    update_request_in_2_people_group(group_list[0], group_list[1])

def simple_shuffle_and_update(query_set, lm_num = 1):
    group_people_num = lm_num + 1
    tmp_list = []
    for request in query_set:
        tmp_list.append(request)

    if (len(tmp_list) < group_people_num):
        return

    shuffle(tmp_list)
    
    step = group_people_num
    for i in range(0, len(tmp_list), step):
        group_list = []
        for j in range(i, i + step - 1):
            group_list.append(tmp_list[j])

        update_request_in_group(group_list)

def count_bit_matched(num1, num2):
    tmp = (num1 & num2)
    one_count = 0

    for i in range(0, 63):
        if (tmp & (1 << i) != 0):
            one_count = one_count + 1

    return one_count

def find_best_match_and_update(query_set):
    tmp_list = []
    for request in query_set:
        tmp_list.append(request)

    if (len(tmp_list) < 2):
        return
    
    matched_set =  set()
    for i in range(len(tmp_list)):
        if i in matched_set]:
            continue
        max_matched = -1
        max_index = -1
        for j in range(i + 1, len(tmp_list)):
            if j in matched_set:
                continue
            tmp_matched = count_bit_matched(tmp_list[i].request_interest,
                tmp_list[j].request_interest)
            if (tmp_matched > max_matched):
                max_matched = tmp_matched
                max_index = j

        if (max_index < 0):
            break
        update_request_in_2_people_group(tmp_list[i], tmp_list[max_index])
        matched_set.add(i)
        matched_set.add(max_index)

