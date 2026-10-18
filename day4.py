for i in range(5):
    print("This is iteration number", i)
for run in range(5):
    print("Run number", run)
for hello in range(5):
    print("Hello, this is iteration number", hello)
for letter in "Login":
    print(letter)
results = ["pass", "fail", "incomplete"]
for result in results:
    print("Result: ",result)

attempts = 0
while attempts < 3:
    print("Attempt", attempts + 1)
    attempts = attempts + 1

while True:
    answer = input("Type 'stop' to quit: ")
    if answer.lower() == "stop":
        break
print("You typed:", answer)

results = ["pass", "fail", "pass", "pass"]
passed_count = 0
for result in results:
    if result == "pass":
        passed_count = passed_count + 1
print(f"{passed_count} of {len(results)} tests passed.")
test = 0
for result in range(len(results)): 
    print(f"Test {test + 1}: {results[result]} ")
    test = test + 1