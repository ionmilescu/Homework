def is_palindrome():
  s = input("Enter a string: ")

    # Reverse the string
  s_rev = s[::-1]

  if s == s_rev:
    print("The string is a palindrome.")
    return True
  else:
    print("The string is not a palindrome.")
    return False

result = is_palindrome()
print(result)  # Output: True or False






  