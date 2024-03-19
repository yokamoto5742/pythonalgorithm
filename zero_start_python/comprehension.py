data = [3**n for n in range(1, 11)]
print(data)

data = [str(n) + '月' for n in range(1, 13)]
print(data)

a = ['apple', 'banana', 'cherry', 'avocado']
b = [s.upper() for s in a]
print(b)

a0 = ['apple', 'banana', 'cherry', 'avocado']
a1 = [s for s in a0 if s.startswith('a')]
print(a1)

a0 = ['apple', 'banana', 'cherry', 'avocado']
a1 = [s for s in a0 if s[0] == 'a']
print(a1)
