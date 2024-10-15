
def first_find_highest(first_num_value, sec_num_value, third_num_value):
    if first_num_value > sec_num_value:
        if first_num_value > third_num_value:
            return first_num_value
        else:
            return third_num_value
    else:
        if sec_num_value > third_num_value:
            return sec_num_value
        else:
            return third_num_value





