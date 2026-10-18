duration = 6.5
if duration < 3:
    print("Fast")
elif duration < 8:
    print("Acceptable")
else:
    print("Too slow")

passed = True
if passed:
    print("Test passed")
else:
    print("Test failed")

status_code = 200
message = "login successful"

if status_code == 200 and "successful" in message:
    print("Pass")
if status_code == 404 or status_code == 500:
    print("Error page")
if not passed:
    print("Needs investigation")

steps_passed = int(input("Enter the number of steps passed: "))
total_steps = int(input("Enter the total number of steps: "))
if steps_passed == total_steps:
    print("PASS")
elif steps_passed == 0:
    print("FAIL: nothing worked")
else:
    print("PARTIAL: investigate")