case_number = input("Enter your case number: ")

def is_modern_format(case_number):
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

def is_legacy_format(case_number):
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

    if not county.isdigit():
        return False

    if not case_type.isalpha() or not case_type.isupper():
        return False

    if not case_number_part.isdigit():
        return False

    return True


def is_appeals_format(case_number):
    if not (7 <= len(case_number) <= 10):
        return False

    district = case_number[0:2]
    case_part = case_number[2:]

    if not district.isalpha() or not district.isupper():
        return False

    if not case_part.isdigit():
        return False

    return True

def is_valid_case_number(case_number):
    return (
        is_modern_format(case_number)
        or is_legacy_format(case_number)
        or is_appeals_format(case_number)
    )

if is_valid_case_number(case_number):
    print("searching")
else:
    print("Invalid case number!") 
   