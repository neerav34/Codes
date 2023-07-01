def vowelR(my_string):
    replacements = [('a', ''), ('e', ''), ('i', ''), ('o', ''), ('u', ''), ('A', ''), ('E', ''), ('I', ''), ('O', ''), ('U', '')]
    print(my_string)
    for char, replacement in replacements:
        if char in my_string:
            my_string = my_string.replace(char, replacement)
    print(my_string)

string = input("Enter the string: ")
vowelR(string)
