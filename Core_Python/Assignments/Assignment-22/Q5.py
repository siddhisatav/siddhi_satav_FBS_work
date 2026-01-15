import re

def is_valid_email(email):
    # Regex pattern for a simple email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Match the email against the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage
emails = [
    "test@example.com",
    "user.name123@gmail.co",
    "invalid-email",
    "user@domain",
    "user@domain."
]

for e in emails:
    print(f"{e}: {is_valid_email(e)}")
