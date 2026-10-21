results = ["pass", "fail", "pass", "fail", "pass"]
results.append("skipped")
results.remove("pass")
print(results)

print(f"{results.count("pass")} in {len(results)} tests passed")

action_results = [("Login", "pass"), ("Search", "fail"), ("Checkout", "pass"), ("Logout", "fail"), ("Profile Update", "pass")]
for action, result in action_results:
    if result == "fail":
        print(action)

failed = []
for action, result in action_results:
    if result == "fail":
        failed.append(action)
print(failed)
