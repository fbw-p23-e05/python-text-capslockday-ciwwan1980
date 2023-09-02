
# input_string = input("Enter string: ")

# if input_string.isupper():
#     normalized_string = input_string.lower() + "!"
# else:
#     normalized_string = input_string.capitalize()

# print(normalized_string)


# input_string = input("Enter the sentence: ")

# if input_string.isupper():
#     normalized_string = input_string.lower().capitalize()
# else:
#     normalized_string = input_string.capitalize()

# print(normalized_string)


def input_string():

    input_string=input("Enter the setences: ")
    if input_string.isupper():
        normalized_string=input_string.lower()+ "!"
    else:
        normalized_string=input_string.capitalize()

    return normalized_string

result=input_string()
print(result)