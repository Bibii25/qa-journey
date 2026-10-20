def greet_tester():
    print("Hello, tester!")
greet_tester()
greet_tester()
def show_results(test_name, passed):
    print(f"{test_name}: {passed}")

show_results("Login", True)
show_results("Checkout", False)

def has_at_symbol(email):
    return "@" in email
result = has_at_symbol("bibi@example.com")
print(result)