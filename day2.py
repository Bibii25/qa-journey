test_name = "Login with valid credentials"
print(test_name.upper())
print(test_name.lower())
print(len(test_name)) #counts the number of characters: 28
print(test_name[0]) #prints the first charcter of the variable: L
print(test_name[0:5]) #prints the first to fifth characters of the variable (0-4): Login
print(test_name.replace("valid", "invalid")) #replaces a word with another
print("valid" in test_name) #checks that a word can be found in the variable: True
print(test_name.split(" ")) #splits each word of the variable name

name = input("What is the test name? ")
steps = int(input("How many steps? "))
result = input("Did it pass? (yes/no) ")

print(f"Test '{name}' has {steps} steps.")
print(f"Passed: {result.lower() == 'yes'}")

bug_title = input("What is the bug title? ")
bug_severity = input("What is the severity of the bug? (high/medium/low) ")

print(f"BUG: '{bug_title.upper()} | SEVERITY: '{bug_severity.upper()} ")