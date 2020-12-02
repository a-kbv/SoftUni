import re

# ONE_LINER
# Time: 0.259s | Mem: 9.81 MB

print(','.join([var.strip("_") for var in re.findall(r"\b\_[a-zA-Z0-9]+\b", input())]))

# OTHER_WAY_IS
# Time: 0.196s | Mem: 9.80 MB

data = input()
var_pattern = r"\b\_[a-zA-Z0-9]+\b"
variables = re.findall(var_pattern, data)
variables = [var.strip('_') for var in variables]
print(','.join(variables))

