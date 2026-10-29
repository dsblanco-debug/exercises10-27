s = "### # ## #"
my_list = []

for ch in s:
    if ch == "#":
        my_list.append(1)
    elif ch == " ":
        my_list.append(0)

print(my_list)
