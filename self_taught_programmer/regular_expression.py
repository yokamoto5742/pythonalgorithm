import re

string = "The ghost that says boo haunts the loo"
m = re.findall(".oo", string)
print(m)
for match in m:
    print(match)
