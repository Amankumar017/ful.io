import re

def is_valid_contact_number(number):
    pattern = r'^(\+?\d{1,3}[-.\s]?)?(\(\d{3}\)|\d{3})([-.\s]?)\d{3}([-.\s]?)\d{4}$'
    return re.match(pattern, number.replace('-', '')) is not None

contact_numbers = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890",
]

valid_count = 0

for number in contact_numbers:
    if is_valid_contact_number(number):
        print(f"{number}: Valid")
        valid_count += 1
    else:
        print(f"{number}: Invalid")

if valid_count >= 5:
    print("Test passed: At least 5 valid contact numbers were identified.")
else:
    print("Test failed: Less than 5 valid contact numbers were identified.")
