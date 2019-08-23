a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

a_set = set(a)
b_set = set(b)

diff = a_set.difference(a_set.intersection(b_set))
print(diff)

