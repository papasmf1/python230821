import re

def is_valid_email(email):
    # Define the regular expression pattern for a valid email address
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # Use re.search() to check if the email matches the pattern
    if re.search(pattern, email):
        return True
    else:
        return False

sample_emails = [
    "user@example.com",
    "john.doe123@gmail.com",
    "contact@website.net",
    "invalid_email",
    "user@domain",
    "user@domain.co.uk",
    "12345@example.org",
    "test.email@yahoo.co.jp",
    "name.lastname@company.io",
    "no_reply@example",
]

for email in sample_emails:
    print(f"{email}: {is_valid_email(email)}")
