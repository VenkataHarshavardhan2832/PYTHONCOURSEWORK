"""Given a string and character as input check weather character exist in string or not

string is Harsha if enter H as a input character it should return true
"""
character_strings = "Harsha"
char = input("Enter a character: ")

def check_char(character_strings, char):
    for i in character_strings:
        if i == char:
            return True
    return False
print(check_char(character_strings, char))