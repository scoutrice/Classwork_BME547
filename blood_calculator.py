def interface():
    print("Blood Calculator")
    print("Options")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
    print("3 - Analyze cholesterol")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = int(input("Enter Choice: "))
        if choice == 9:
            return
        elif choice == 1:
            HDL_driver()
        elif choice == 2:
            LDL_driver()
        elif choice == 3:
            Cholesterol_driver()

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

def input_LDL():
    LDL_input = input("Enter the LDL value: ")
    return int(LDL_input)

def check_LDL(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value < 160:
        return "Borderline High"
    elif 160 <= LDL_value <190:
        return "High"
    else:
        return "Very High"

def LDL_driver():
    ldl_value = input_LDL()
    ans = check_LDL(ldl_value)
    output_LDL_result(ldl_value, ans)

def output_LDL_result(LDL_value, character):
    print("The results for an LDL value of {} is {}".format(LDL_value, character))

def input_chol():
    chol_input = input("Enter the cholesterol value: ")
    return int(chol_input)

def check_chol(Chol_value):
    if Chol_value < 200:
        return "Normal"
    elif 200 <= Chol_value < 240:
        return "Borderline High"
    else:
        return "High"

def Cholesterol_driver():
    chol_value = input_chol()
    ans_chol = check_chol(chol_value)
    output_chol_result(chol_value, ans_chol)

def output_chol_result(Chol_value, char):
    print("The results for the a cholesterol value of {} is {}".format(Chol_value, char))

if __name__ == "__main__":
    interface()