import re

def test_password(pword):
    strength = 0
    if len(pword) > 14:
        strength += 1
    # If it contains lowercase letters, strength+=1
    # Create a class of lowercase chars
    # Find if there are any characters in pword in the lowercase class
    if re.search(r'[a-z]', pword):
        strength += 1
    if re.search(r'[A-Z]', pword):
        strength += 1
    if re.search(r'\d', pword):
        strength += 1
    if re.search(r'[^a-zA-Z0-9]', pword):
        strength += 1

    if 0 <= strength <= 2:
        print("The password ", pword, " is weak.")
    elif 3 <= strength <= 4:
        print("The password ", pword, " is medium.")
    elif 5 <= strength:
        print("The password ", pword, " is strong!")


if __name__ == '__main__':
    test_password("hi")
    test_password("hellotherefriendsiloveyou")
    test_password("helloworld01011997")
    test_password("heL2lo2@!!@#@$#@$##@$@#!")

