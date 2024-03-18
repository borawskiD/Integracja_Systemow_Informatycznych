def isPalindrome(txt):
    return txt == txt[::-1]


text = input('Podaj tekst:')
print("To jest palindrom" if isPalindrome(text) else "To nie jest palindrom")
