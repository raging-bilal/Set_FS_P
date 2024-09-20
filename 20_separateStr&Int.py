# 20. Given a list containing strings and integers. Write a program to create two separate lists consisting of strings and integers respectively. 



def separate_strings_and_integers(input_list):
    strings = []
    integers = []

    for item in input_list:
        if isinstance(item, str):
            strings.append(item)
        elif isinstance(item, int):
            integers.append(item)

    return strings, integers

# Example usage
my_list = [1, 'apple', 3, 'banana', 5, 'cherry', 10, 'grape']
strings, integers = separate_strings_and_integers(my_list)

print("List of Strings:", strings)
print("List of Integers:", integers)
