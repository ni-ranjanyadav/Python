# Using Walrus Operation

# if(n := len([1,2,3,4,5]))>3:
#     print(f"List is too long ({n} element, expected <=3)")
    
    
# from typing import List, Tuple, Dict, Union

# n: int = 5
# name: str = "niranjan"

# def add(a: int, b: int) -> int:
#     return a + b
    
# result = add(3, 4) 
# print(result)


# # Match Case
# def http_status(status):
#     match status:
#         case 200:
#             return "ok"
#         case 404:
#             return "Not Found"
#         case 500:
#             return "internal server error"
#         case _:
#             return "unknown status"
        
# print(http_status(200))



# # Dictionary Merged
# dict1 = {'a': 1, 'b': 2}
# dict2 = {"b": 3, "c": 4}

# merged = dict1 | dict2
# print(merged)

