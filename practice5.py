def is_valid_email(email):
    return "@" in email and "." in email

def describe_result(passed):
    if passed:
        return "PASS"
    else:
        return "FAIL"

emails = ["a@b.com", "abc", "a@b", "@."]

for email in emails:
    result = is_valid_email(email)
    print(f"{email}: {result}, {describe_result(result)}")