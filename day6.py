results = ["pass", "fail", "pass"]

print(results[0])
print(results[-1])
print(len(results))
print(results[0:2])

results.append("fail")
results.insert(1, "skipped")
results[0] = "blocked"
results.remove("fail")
last = results.pop()
print(results)

print("pass" in results)
print(results.count("pass"))
results.sort()

for result in results:
    print(result)

test_case = ("Login", 4, True)
print(test_case[0])

name, steps, expected = test_case
print(f"{name} has {steps} steps")