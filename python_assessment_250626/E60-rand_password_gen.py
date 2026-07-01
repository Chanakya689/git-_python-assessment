#Given Input: Length: 12
#Expected Output: Generated Password: 4k#79!zP[2mQ

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    print(characters)
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = 12
print(f"Generated Password: {generate_password(length)}")