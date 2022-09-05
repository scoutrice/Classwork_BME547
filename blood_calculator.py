def interface():
    print("Blood Calculator")
    print("Options")
    print("1 - Analyze HDL")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = int(input("Enter Choice: "))
        if choice == 9:
            return
        elif choice == 1:
            HDL_driver()

def input_HDL():
    HDL_input = input("Enter the HDL value: ")
    return int(HDL_input)

def check_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif HDL_value >= 40:
        return "Borderline Low"
    else:
        return "Low"

def HDL_driver():
    hdl_value = input_HDL()
    answer = check_HDL(hdl_value)
    output_HDL_result(hdl_value, answer)

def output_HDL_result(HDL_value, charac):
    print("The results for an HDL value of {} is {}".format(HDL_value, charac))

interface()