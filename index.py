
# functions that finds the first missing positive integer
def first_missing_positive_integer(input_list):
    input_list.sort()
    # 1 is the lowest positive integer
    temp = 1
    for i in input_list:
        if temp == i:
            temp +=1
        elif i > temp:
            break
    return temp



user_input = input('Enter elements of a list separated by space:\n')
user_list = user_input.split()
#validated list
valid_user_input = []


#  user input  validation
for item in user_list:
    if item.isdigit():  # lacks negative numbers
        valid_user_input.append(int(item))
    else:
        print(f"'{item}' is not a valid integer.")
        
result = first_missing_positive_integer(valid_user_input)
print(result)