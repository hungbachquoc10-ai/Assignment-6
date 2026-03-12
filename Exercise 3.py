name_string = set()
print("Enter names one by one. Press Enter (empty string) to quit.")
while True:
    name = input("Enter a name: ").strip()
    if name == "":
        break
    if name in name_string:
        print("Existing name")
    else:
        print("New name")
        name_string.add(name)
print("List of all names entered:")
for n in name_string:
    print(n)