def interface():
    print("Blood Calculator")
    print("Options")
    print("9 - Quit")
    choice = input("Enter Choice: ")
    if choice == 9:
        return

interface()

def input_HDL():
    HDL_input = input("Enter the HDL value: ")
    return int(HDL_input)

input_HDL()