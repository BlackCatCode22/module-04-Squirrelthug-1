


def chop(lst):
    """
    This function takes a list and modifies it, removing the first and last elements
    It does not return anything
    """
    if len(lst) > 0:
        del lst[0]              # remove the first element
        if len(lst) > 0:
            del lst[-1]         # remove last element

def middle(lst):
    """
    This function takes a list and returns a new list that contains all but the first and last elements
    """
    return lst[1:-1] if len(lst) > 2 else []


usr_input = input("Enter a file name: ")
try:
    fhand = open(usr_input)
except:
    print("File cannot be opened:", usr_input)
    exit()
count = 0

for line in fhand:
    count += 1
    if not isinstance(line, str):
        print("Invalid data in file:", line)        # guarding against non-string data
        continue
    line = line.upper()
    line = line.rstrip()
    if line == "":                                  # guarding against empty lines
        continue
    print(line)

# Test the chop function
test_list = [1, 2, 3, 4, 5]
chop(test_list)
print(f"chop() test: {test_list}")  # Should print: [2, 3, 4]

# Test the middle function
test_list2 = [1, 2, 3, 4, 5]
new_list = middle(test_list2)
print(f"middle() test: {new_list}")  # Should print: [2, 3, 4]

print(f"Number of lines in the file: {count}")