# def get_multiplied_digits(number ):
#     str_number = str(number)
#     first = int(str_number[0])
#     if len(str_number) == 1:
#         return first
#     else:
#         return first * get_multiplied_digits(int(str_number[1:]))

# print(get_multiplied_digits(12345))

def get_multiplied_digits(number: str):
    str_number = str(number)
    first = int(str_number[0])
    print(first)
    if len(str_number) == 1:
        if first == 0:
            first += 1
        else:
            return first
        return first
    elif first == 0:
        first += 1
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))
number = input()
print(get_multiplied_digits(number))
