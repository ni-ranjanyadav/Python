# task = input()

# if task == "permutation":
#     s = str(input())
#     n = len(s)
#     for i in range(n):
#         for j in range(n):
#             if i != j:
#                 print(s[i] + s[j])
                
                
# elif task == "sorted_permutation":
#     s = str(input())
#     for i in range(len(s)):
#         for j in range(len(s)):
#             if i != j:
#                 if s[i] < s[j]:
#                     print(s[i] + s[j])
                    
            
# elif task == "repeat_the_repeat":
#     n = int(input())
#     for i in range(n):
#         for j in range(1, n+1):
#             print(j, end= "")
#         print()
        
# elif task == "repeat_incrementally":
#     n = int(input())
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j, end="")
#         print()
        
# elif task == "increment_and_decrement":
#     n = int(input())
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j, end="")
#         for k in range(j-1,0,-1):
#             print(k, end="")
#         print()
        
# elif task == "repeat_incremently":
#     n = int(input())
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j, end="")
#         print()


task = input()

if task == "factor":
    n = int(input())
    i = 1
    while (i<=n):
        if n % i == 0:
            print(i)
        i+=1
        
elif task == "find_min":
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
        min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    print(min_num)
    
elif task == "prime_check":
    n = int(input())
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

elif task == "is_sorted":
    s = input()
    is_sorted = True
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            is_sorted = False
            break
    print(is_sorted)

elif task == "any_true":
    n = int(input())
    any_true = False
    for _ in range(n):
        num = int(input())
        if num % 3 == 0:
            any_true = True
    print(any_true)

elif task == "manhattan":
    x, y = 0, 0  # starting point
    while True:
        move = input()
        if move == "STOP":
            break
        elif move == "UP":
            y += 1
        elif move == "DOWN":
            y -= 1
        elif move == "RIGHT":
            x += 1
        elif move == "LEFT":
            x -= 1
    # Manhattan distance = |x| + |y|
    distance = abs(x) + abs(y)
    print(distance)
