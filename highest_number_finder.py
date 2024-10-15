# For the first three values
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

# For the last two values
def second_find_highest(fourth_num_value, fifth_num_value):
    if fourth_num_value > fifth_num_value:
        return fourth_num_value
    else:
        return fifth_num_value

# To compare the two highest number of the two sets
def final_find_highest(first_highest, second_highest):
    if first_highest > second_highest:
        return first_highest
    else:
        return second_highest

# Input for all five values
first_value = int(input("First value: "))
sec_value = int(input("Second value: "))
third_value = int(input("Third value: "))
fourth_value = int(input("Fourth value: "))
fifth_value = int(input("Fifth value: "))

# The results for the first and second set
res1 = first_find_highest(first_value, sec_value, third_value)
res2 = second_find_highest(fourth_value, fifth_value)

# The final result or the highest number
final_result = final_find_highest(res1, res2)

# Print the highest number
print("The highest number is:", final_result)






