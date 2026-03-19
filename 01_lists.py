
# =====================================
# Step 1 — Create a list
# =====================================

numbers = [1, 2, 3, 4, 5]

total = 0

for n in numbers: 
              total += n

average = total / len(numbers)

print('Average:', average)
print('\n===================')

# =====================================
# Step 2 — Access elements
# =====================================

print('\nAccessing elements:')
print('First element:', numbers[0])
print('Last element:', numbers[-1])       
print('\n===================')
# =====================================
# Step 3 — Loop through list
# =====================================

print("\nLoop through list:")

for n in numbers:
    print(n)
print('\n===================')
# =====================================
# Step 4 — Append new elements
# =====================================

numbers.append(6)
numbers.append(7)

print("\nAfter appending new elements:")
print(numbers)
print('\n===================')

# =====================================
# Step 5 — Remove elements
# =====================================
numbers.remove(3)                        # remove specific value
numbers.remove(4)                        # remove specific value   
numbers.pop(0)                           # remove element at index 0
numbers.pop()                            # remove last element

print("\nAfter removing elements:")
print(numbers)              
print('\n===================')

# =====================================
# Step 6 — Filter values
# =====================================

filtered = []
for n in numbers:
    if n > 4:
        filtered.append(n)  

print("\nFiltered values (greater than 4):")
print(filtered)
print('\n===================')

# =====================================
# Step 7 — List comprehension 
# =====================================

filtered2 = [n for n in numbers if n > 3]

print("\nFiltered using list comprehension:")
print(filtered2)
print('\n===================')

# =====================================
# Step 8 — Find max and min
# =====================================

print('\nMax value:', max(numbers))
print('Min value:', min(numbers))
print('\n===================')

# =====================================
# Step 9 — Sort list
# =====================================

numbers.sort()

print('\nSorted list:')
print(numbers)
print('\n===================')

# =====================================
# Step 10 — Realistic example
# =====================================

# Example: electricity demand data
demand = [120, 110, None, 100, None, 130]

print("\nOriginal demand data:")
print(demand)


# Remove missing values
clean_demand = []

for d in demand:
    if d is not None:
        clean_demand.append(d)

print("\nClean demand data:")
print(clean_demand)


# Compute average demand
total = 0

for d in clean_demand:
    total += d

avg_demand = total / len(clean_demand)

print("\nAverage demand:", avg_demand)