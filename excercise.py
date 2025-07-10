# exercise.py
# Part 1: Mutable vs Immutable
a = 100
b = a
print("Before:", a, b, id(a), id(b))
# Variables a and b start with the same ID since they equate to the same value.

a += 1
print("After a += 1:", a, b, id(a), id(b))
# After adding 1 to a, a will have a different ID since integers are immutable,
# but b will stay the same ID since nothing tried to modify it.

x = [1, 2, 3]
y = x
print("Before:", x, y, id(x), id(y))
# Variables x and y will also start with the same ID since they are set to the same list.

x.append(4)
print("After x.append(4):", x, y, id(x), id(y))
# After appending 4 to list x, both list x and y will still be the same ID since lists are
# mutable.

# ===

# Part 2: Lists & Loops
names = ["alice", "bob", "charlie", "dana"]

# Task A: build upper_names
upper_names = []
for n in names:
    # TODO: append uppercase n
    upper_names.append(n.upper())

print(upper_names)

# Task B: enumerate over upper_names
for i, n in enumerate(upper_names):
    # TODO: print index and name
    print(f"Index: {i}, Name: {n}")

# Task C: demo two list methods
# 1. insert
upper_names.insert(1, "Jonathan")
print(upper_names)
# 2. remove
upper_names.remove("BOB")
print(upper_names)
# 3. sort
upper_names.sort()
print(upper_names)
