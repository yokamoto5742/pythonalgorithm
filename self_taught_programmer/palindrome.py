def palindrome(word):
    word = word.lower()
    return word == word[::-1]


print(palindrome("Mother"))
print(palindrome("Mom"))
print(palindrome("たけやぶやけた"))