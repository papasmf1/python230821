import re

def is_valid_korean_ssn(ssn):
    # Define the regular expression pattern for a valid Korean resident registration number
    pattern = r'^\d{6}-\d{7}$'
    
    # Use re.match() to check if the ssn matches the pattern from the start of the string
    if re.match(pattern, ssn):
        return True
    else:
        return False

# Test the function
ssn1 = "123456-7890123"
ssn2 = "890123-4567890"
ssn3 = "1234567890123"
ssn4 = "12A456-7890123"
ssn5 = "123456-78901"

print(is_valid_korean_ssn(ssn1))  # True
print(is_valid_korean_ssn(ssn2))  # True
print(is_valid_korean_ssn(ssn3))  # False
print(is_valid_korean_ssn(ssn4))  # False
print(is_valid_korean_ssn(ssn5))  # False
