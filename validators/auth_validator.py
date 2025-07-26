def validate_non_empty(field_name: str, value):
    if value is None or str(value).strip() == "":
        raise ValueError(f"{field_name} cannot be empty")

def validate_email_format(email: str):
    import re
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email format")

def validate_password_strength(password: str):
    if len(password) < 5:
        raise ValueError("Password must be at least 6 characters long")