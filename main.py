case_number = input("Enter your case number: ")

def is_valid_case_number(case_number):
    if len(case_number) != 12:
        return False

    if case_number[4] != "-":
        return False

    year = case_number[0:2]
    county = case_number[2:4]
    case_type = case_number[5:7]
    case_number_part = case_number [7:]

    if not year.isdigit():
        return False

    if not county.isalpha() or not county.isupper():
        return False

    if not case_type.isalpha() or not case_type.isupper():
        return False

    if not case_number_part.isdigit():
        return False

    return True

if is_valid_case_number(case_number) == False:
    print("Invalid Case Number!")
else:
    print("Searching...")
