name = ["taro", "jiro", "hanako"]
job =["Architect", "Engineer", "Doctor"]

all_list = []

for i, value in enumerate(name):
    new = value.upper()
    name[i] = new
    all_list.append(new)

for i, value in enumerate(job):
    new = value.upper()
    job[i] = new
    all_list.append(new)

print(all_list)

