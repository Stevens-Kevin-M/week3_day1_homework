# HOMEWORK EXAMPLE (LIST OF NAME WITH TWITTER HANDLE)

# Hint, this will be easier for you if you use f.readlines() vs f.read when opening and reading the files

# KEVIN'S ATTEMPT

print("====================")
print("Full Names / Twitter")
print("====================")

with open("files/names.txt") as f:
    my_lines = f.readlines()

def validateLine(line):
    new_pattern = re.compile("([\w]+)\s@([\w)]+)\s")
    if new_pattern.findall(line):
        return line
        
for line in my_lines:
    print(validateLine(line))
    
    
# NATE'S EXAMPLE

with open("files/names.txt") as f:
    data = f.readlines()
    
pattern = re.compile("([A-Z][a-z]+), ([\w-]*)([A-Z][a-z]+).*\s(@[\w]+)")

for person in data:
    match = pattern.search(person)
    if match:
        print(f"{match.group(2)}{match.group(3)} {match.group(1)} / {match.group(4)}")

# REGEX PROJECT

"""
Expected Output
Abraham Lincoln
Andrew P Garfield
Connor Milliken
Jordan Alexander Williams
None
None
"""

with open("files/regex-test.txt") as f:
    my_names = f.readlines()

def validateName(name):
    pattern = re.compile("([A-Za-z]+) \s*([A-Z]+)\s*([A-Za-z]+)")
    if pattern.findall(name):
        return name
    else:
        None
        
for name in my_names:
    print(validateName(name))    