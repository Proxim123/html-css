#inputName = input()
#print(f"Hello {inputName}")

#variables and conditions
i=2
if i > 0:
	print(f"positive number: {i}")
elif i < 0:
	print(f"negative number: {i}")
else:
	print(f"number value is: {i}")

f=2.5
print(f"float: {f}")

b=True
print(f"boolean: {b}")

n=None
print(f"None: {n}")

name = "Alice"
coordinates = (10.0, 20.0)
names = ["Alice", "Robert", "Jessie"]

print(f"name: {name}, coordinates: {coordinates}, nameList: {names}")
print(f"name[0]: {name[0]}, coordinates[1]: {coordinates[1]}, nameList[2]: {names[2]}")

#loop
for i in range(5):
	print(i)

for name in names:
	print(name)

#datatype::set
s = set()
s.add(1)
s.add(3)
s.add(5)
s.add(3)
print(s)

#datatype::dictionaries
ages = {"Mitch": 20, "Isabel": 18}
ages["Rosie"] = 19
print(ages)
ages["Mitch"] += 1
print(ages["Mitch"])

#functions
def square(x):
	return x * x
for i in range(10):
	print("{}'s square is {}".format(i, square(i)))
