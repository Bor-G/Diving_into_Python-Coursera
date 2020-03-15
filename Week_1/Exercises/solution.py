import sys
digit_string = sys.argv[1]
result = 0
for char in digit_string:
    result += int(char)

print(result)
    