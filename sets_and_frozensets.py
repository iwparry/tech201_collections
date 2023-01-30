# Sets and Frozen Sets

# Lists and Sets are very similar
# Sets are unordered

# Create a set

car_parts = {"wheels", "doors", "exhaust"}
print(car_parts)
# print(car_parts[1]) # 'set' object is not subscriptable - no indices

car_parts.discard("doors") # removes "doors"
print(car_parts)

car_parts.add("windows") # adds "windows to the set
print(car_parts)

# Frozen sets

# Like Tuples Frozen sets are immutable, still unordered (no indices)

x = frozenset([1, 2, 3, 4, "five"])
print(x)


