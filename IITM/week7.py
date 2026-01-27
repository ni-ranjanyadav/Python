# def seconds_to_minute_seconds(seconds):
#     minutes = seconds//60
#     remaining_seconds = seconds%60
#     return(minutes,remaining_seconds)

# def create_indexed_dict(items):
#     indexed_dict = {index: item for index, item in enumerate(items)}
#     return indexed_dict


# a = (1,2)
# b = (3,4)
# c = (6,7)
# def manhattan_distance_via_b(a, b,c):
#     ab_distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
#     bc_distance = abs(b[0] - c[0]) + abs(b[1] - c[1])
#     d = ab_distance + bc_distance
#     return d
# print(manhattan_distance_via_b(a,b,c))


# a= 3
# b= 3
# c= 5
# def is_right_triangle_with_even_sides(a:int,b:int,c:int) -> bool:
#     return bool(a % 2 == 0 and c**2 == a**2 + b**2)
# print(is_right_triangle_with_even_sides(a,b,c))


# string = 'a1b2c3'
# def is_odd_indices_alpha_and_even_indices_digits(string):
#     for i, ch in enumerate(string):
#         if i % 2 == 0:
#             if not ch.isdigit():
#                 return False
#         else:
#             if not ch.isalpha():
#                 return False
#     return True
# print(is_odd_indices_alpha_and_even_indices_digits(string))


# s = str(input())
# def has_a_in_second_half(s):
#     mid = len(s) // 2
#     second_half = s[mid:]
#     return 'a' in second_half.lower()
# print(has_a_in_second_half(s))


# s = 'Niranjan'
# def remove_edges(s):
#     return s[2:len(s)-2]
# print(remove_edges(s))

# t = (10,20,30,40,50,60)
# def reverse_first_half(t):
#     first_half = t[:len(t)//2][::-1]
#     second_half = t[len(t)//2:]
#     return first_half + second_half
# print(reverse_first_half(t))


# def number_of_unique_common_digits(n1, n2):
#     common = set(str(n1)) & set(str(n2))
#     return len(common)
# print(number_of_unique_common_digits(287498, 295424))


# # explicit version
# def final_position(pos: tuple, vel: tuple, time: int) -> tuple:
#     x_final = pos[0] + vel[0] * time
#     y_final = pos[1] + vel[1] * time
#     return (x_final, y_final)
# print(final_position((1,2), (2,1), 3))


# def func(nums:list):
#     return sum(num*2 for num in nums)


# DATA PROCESSING

def num_to_word(num: int) -> str:
    '''
    Given an integer, generate a string with its digits as words separated by hyphens.

    Arguments:
    num: int - the input number

    Return:
    str - the string with digits as words separated by hyphens
    '''
    digit_words = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three',
        '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
        '8': 'eight', '9': 'nine'
    }
    return '-'.join(digit_words[d] for d in str(abs(num)))


def row_index_with_most_number_of_zeros(matrix:list)->int:
    '''
    Given a matrix, find the index of the row with the 
    maximum number of zeros in it.

    Arguments: matrix: list[list] 
    Rertun: int - index of the row with the maximum number of zeros.
    '''
    return max(range(len(matrix)), key=lambda i: matrix[i].count(0))
