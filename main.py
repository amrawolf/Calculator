a = "абвгдеєжзиійїклмнопрстуфхцчшщьюяabcdefghijklmnopqrstuvwxyz0123456789"

print("If you want to encrypt text enter 1. If you want to decipher text enter 2: ")
choice = int(input())

if choice == 1:
    print("Enter your words: ")
    val = input()
    print("What indentation do you want to make?")
    key = int(input())
    val_lower = val.lower()
    vald = ""

    for letter in val_lower:
        position = a.find(letter)
        new_position = position + key
        if letter in a:
            vald = vald + a[new_position]
        else:
            vald = vald + letter
    print(vald)
elif choice == 2:
    print("Enter your words: ")
    val = input()
    print("What indentation do you want to make?")
    key = int(input())
    val_lower = val.lower()
    vald = ""

    for letter in val_lower:
        position = a.find(letter)
        new_position = position - key
        if letter in a:
            vald = vald + a[new_position]
        else:
            vald = vald + letter
    print(vald)