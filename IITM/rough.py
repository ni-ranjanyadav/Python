def is_odd_length_palindrome(s: str):
    if (s == s[::-1]) and len(s)%2 == 1:
        return True
    else:
        return False
s = input("Enter word: ")
print(is_odd_length_palindrome(s))