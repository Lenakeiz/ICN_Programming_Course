def calculate_average_wrong_indent(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
    count += 1  # Indented at the wrong level
    average = total / count  # Average will be incorrectly calculated
    return average

def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    average = total / count
    return average
    
def number_existence_wrong_indentation(number_to_find, numbers):
    found = False
    number_index = None
    for index, num in enumerate(numbers):        
        if number_to_find == num:
            number_index = index
            found = True
            print("True")
            break        
        else:
            print("False")
    return [found,number_index]

def number_existence(number_to_find, numbers):
    found = False
    number_index = None
    for index, num in enumerate(numbers):        
        if number_to_find == num:
            number_index = index
            found = True
            print("True")
            break       
    else:
        print("False")
    return [found,number_index]

numbers = [5, 1, 3, 4, 2]

average = calculate_average_wrong_indent(numbers)
print("The average is:", average)

[isFound, index] = number_existence_wrong_indentation(4, numbers)
if isFound:
    print(f"The number exists in the list: {numbers[index]}")
