y = input("Enter a word: ")


def isPalindrome(y):
    return y == y[::-1]


ans = isPalindrome(y)

if ans:
    print("Yes!")
else:
    print("No!")

