from validator import is_valid_case_number

if __name__ == "__main__":
    case_number = input("Enter your case number: ")

    if is_valid_case_number(case_number):
        print("Searching... ")
    else:
        print("Invalid case nubmer")