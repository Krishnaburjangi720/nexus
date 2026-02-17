def sanitize_email(raw_input: str) -> str:
    email = raw_input.strip().lower()

    if email == "" or email.count("@") != 1:
        return "Invalid Email"

    return email
