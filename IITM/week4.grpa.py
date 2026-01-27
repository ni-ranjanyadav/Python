# # Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
# with open(__file__) as f:
#     content = f.read().split("# <nofor>")[2]
# if "for " in content:
#     print("You should not use for loop or the word for anywhere in this exercise")

# # The values of the below variables will be changed by the evaluator
# int_iterable = range(1,10,3)
# string_iterable = ["Apple","Orange", "Banana"]
# some_value = 4
# some_collection = [1,2,3] # list | set | tuple 

# some_iterable = (1,2,3)
# another_iterable = {"apple", "banana", "cherry"} # can be any iterable
# yet_another_iterable = range(1,10)

# # <nofor>
# # <eoi>

# empty_list = [ ] 
# empty_set = set() # be carefull here you might end up creating something called as an empty dict 
# empty_tuple = () 
# # print(type(empty_list).__name__)
# # print(type(empty_set).__name__)
# # print(type(empty_tuple).__name__)
# # print(len(empty_list))
# # print(len(empty_set))
# # print(len(empty_tuple))


# singleton_list = [1] # list: A list with only one element
# singleton_set = {1} # set: A set with only one element
# singleton_tuple = (1,) # tuple: A tuple with only one element
# # print(type(singleton_list).__name__)
# # print(type(singleton_set).__name__)
# # print(type(singleton_tuple).__name__)
# # print(len(singleton_list))
# # print(len(singleton_set))
# # print(len(singleton_tuple))


# a_falsy_list = [] # list: a list but when passed to bool function should return False.
# a_falsy_set = set() # set: a list but when passed to bool function should return False.
# a_truthy_tuple = (1,) # tuple: a tuple but when passed to bool function should return True
# # print(type(a_falsy_list).__name__)
# # print(bool(a_falsy_list))
# # print(type(a_falsy_set).__name__)
# # print(bool(a_falsy_set))
# # print(type(a_truthy_tuple).__name__)
# # print(bool(a_truthy_tuple))


# #int_iterable = [4,2,4,6,7,3,-2,3]
# # int_iterable = range(10)
# # int_iterable = range(20)
# int_iterable_min = min(int_iterable) # int: find the minimum of int_iterable. Hint: use min function
# int_iterable_max = max(int_iterable) # int: find the maximum of int_iterable. Hint: use max function
# int_iterable_sum = sum(int_iterable) # int: you know what to do
# int_iterable_len = len(int_iterable) # int: really... you need hint?
# int_iterable_sorted = sorted(int_iterable) # list: the int_iterable sorted in ascending order
# int_iterable_sorted_desc = list(reversed(int_iterable_sorted)) # list: the int_iterable sorted in desc order
# # print(int_iterable_min)
# # print(int_iterable_max)
# # print(int_iterable_sum)
# # print(int_iterable_len)
# # print(int_iterable_sorted)
# # print(int_iterable_sorted_desc)







# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <noloop>")[2]
if "for " in content or "while " in content:
    print("You should not use for loop, while loop or the word for and while anywhere in this exercise")

# note that apart from the print statements inside the functions, the evaluator will also print what is returned by the function at last
# <noloop>

def list_mutating_operations(items: list, item1, item2):
    # Sort the list in-place
    items.sort()
    print("sorted:", items)

    # Append item1 at the end
    items.append(item1)
    print("append:", items)

    # Insert item2 at index 3 (or at the end if list is shorter)
    insert_index = 3 if len(items) >= 3 else len(items)
    items.insert(insert_index, item2)
    print("insert:", items)

    # Extend with first three elements (or all elements if less than 3)
    items.extend(items[:3])
    print("extend:", items)

    # Pop fifth element (or last if fewer than 5 elements)
    pop_index = 4 if len(items) > 4 else -1
    popped_item = items.pop(pop_index)
    print("pop:", items)

    # Remove first occurrence of item2 if present
    if item2 in items:
        items.remove(item2)
    print("remove:", items)

    # Make index 4 None if exists
    if len(items) > 4:
        items[4] = None
    print("modify_index:", items)

    # Make all even indices None
    items[::2] = [None] * len(items[::2])
    print("modify_slice:", items)

    # Delete third last element if list has at least 3 elements
    if len(items) >= 3:
        del items[-3]
    print("delete_index:", items)

    # Delete all even indices
    del items[::2]
    print("delete_slice:", items)

    return items, popped_item

list_mutating_operations(["Apple", "Cherry","Banana","Grapes"], "Blueberry","Apple"),(['Cherry', 'Blueberry', None], "Grapes")
