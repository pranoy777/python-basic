str1 = input("please enter first string: ").lower()
str2 = input("please enter first string: ").lower()
found = False
if len(str1)==len(str2):
    for c in str1:
        if c in str2:
            pass
        else:
            found=True
            break
    if found:
        print("It is not an anagram")
    else:
        print("yes! It is an anagram")
else:
    print("Length mismatched")
