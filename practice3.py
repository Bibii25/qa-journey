bug_severity = input("Enter the bug severity (low, medium, high): ")
if bug_severity.lower() == "low":
    print("Low severity bug, please fix when you have time.")
elif bug_severity.lower() == "medium":
    print("Medium severity bug, please fix soon.")
else:
    print("High severity bug, please fix immediately.")