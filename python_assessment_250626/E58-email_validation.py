#Given Input: 
email1 = "python_pro@gmail.com" 
email2 = "bad-email@com" 
#Expected Output:
#  'python_pro@gmail.com' is a Valid Email 
# 'bad-email@com' is an Invalid Email

import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return f"'{email}' is a Valid Email"
    else:
        return f"'{email}' is an Invalid Email"

print(validate_email(email1))
print(validate_email(email2))
