# def vowelR(str):
#     # str=list(str)
#     for i in range(len(str)):
#         if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u':
#             del str[i]
#     print(str)     
    
# s=input("Enter the string: ")
# print(s[2])
# vowelR(s)

def vowelR(my_string):
    replacements = [('a', ''), ('e', ''), ('i', ''), ('o', ''), ('u', ''), ('A', ''), ('E', ''), ('I', ''), ('O', ''), ('U', '')]
    # my_string=my_string.lower()
    print(my_string)
    for char, replacement in replacements:
        if char in my_string:
            my_string = my_string.replace(char, replacement)

    print(my_string)

string = input("Enter the string: ")
vowelR(string)