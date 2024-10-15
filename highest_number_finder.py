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

# To find the most highest
def final_most_highest(first_highest, fourth_num_value, fifth_num_value):
    if first_highest > fourth_num_value:
        if first_highest > fifth_num_value:
            return first_highest
        else:
            return fifth_num_value
    else:
        return fourth_num_value

# Input for all five values
first_value = int(input("First value: "))
sec_value = int(input("Second value: "))
third_value = int(input("Third value: "))
fourth_value = int(input("Fourth value: "))
fifth_value = int(input("Fifth value: "))

# The result for the first set
first_result = first_find_highest(first_value, sec_value, third_value)

# The final result or the highest number
final_result = final_most_highest(first_result, fourth_value, fifth_value)

# Print the highest number
print("The highest number is:", final_result)






