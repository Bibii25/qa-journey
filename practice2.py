bug_title = input("What is the title of the bug? ")
bug_severity = input("What is the severity of the bug? (low/medium/high) ")

print(f"BUG: {bug_title.upper()} | SEVERITY: {bug_severity.upper()}")

test_name = "Login with valid credentials"
print("login" in test_name)
print("password" in test_name)
print("VALID" in test_name)