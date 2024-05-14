import re

def stringvalidator(s):
    print(any(c.isalnum() for c in s))
    print(bool(re.search(r'[a-zA-Z]', s)))
    print(bool(re.search(r'\d', s)))
    print(bool(re.search(r'[a-z]', s)))
    print(bool(re.search(r'[A-Z ]', s)))

stringvalidator("#$%@^&*")