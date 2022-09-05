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

def check_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif HDL_value < 40:
        return "Low"
    else:
        return "Borderline Low"

def driver_function():
    hdl_value = input_HDL()
    answer = check_HDL(hdl_value)
    ouput_HDL_result(hdl_value, answer)

def output_HDL_result(hdl_value, characterization):
    print("The results for an HDL value of {} is {}".format(hdl_value, characterization))
