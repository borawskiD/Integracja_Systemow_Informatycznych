def longest(tekst):
    return max(tekst, key=len)


file = open("test.txt").read().replace(".", "").replace(",", "").split()

print(longest(file))
