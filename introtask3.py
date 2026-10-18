list_a = ["pass", "fail"]
list_a[0] = "incomplete"
print(list_a) #prints the entire list: ['incomplete', 'fail']

first_name = "Bibi"
last_name = "Kalu"
full_name = first_name + " " + last_name
print(full_name) #prints the full name: Bibi Kalu
print(first_name[0:3])
print(full_name[0:8:2])
print(full_name.replace("Bibi", "Yuji"))
print(full_name.startswith("Bibi"))
print(full_name.endswith("Kalu"))
print(full_name.split(" "))
print(full_name.find("Kalu"))