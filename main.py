"""
The function determines whether the given word is a palindrome. It compares whether a given word when read from left to right sounds the same when read from right to left.
At the end it returns True/False.
"""

def palindrome(word):
  palindrome1 = ""
  palindrome2 = ""
  for i in range(len(word)):
    palindrome1 += word[i]
  for i in range(len(word)-1, -1, -1):
    palindrome2 += word[i]
  if palindrome1 == palindrome2:
    return True
  else:
    return False
