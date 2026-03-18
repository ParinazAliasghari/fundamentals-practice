# =====================================
# Step 1: Create a simple dictioanry 
# =====================================
prices = { "Oslo": 100, "Bergen": 75, "Trondheim": 78}

print(prices)
print(prices["Oslo"])
for city, price in prices.items():
              print(city, price)
for city in prices:
              print(city,prices[city])
print('==============\n')            
# =====================================
# Step 2: Add a new key-value pair to the dictionary
# =====================================
prices["Stavanger"] = 80
print(prices)
print('==============\n')
# =====================================
# Step 3: Create dataset (list of dictionaries)
# =====================================
data =[
    {"city": "Oslo", "temperature": 5, "demand": 120},
    {"city": "Bergen", "temperature": None, "demand": 110},
    {"city": "Trondheim", "temperature": 2, "demand": None},
    {"city": "Stavanger", "temperature": 7, "demand": 100}
]

print (data)
print('--------------\n')
print (data[0])
print('--------------\n')
print (data[0]["city"])
print('--------------\n')
print (data[0]["temperature"])
print('--------------\n')
print('original dataset:')
for row in data:
        print(row)

print(type(data))
print(type(row))       
print('==============\n')

# =====================================
# Step 5: Detect missing values
# =====================================
print('Row with missing data:')
for row in data:
        if None in row.values():
              print(row)
print('--------------\n')
for row in data:
        if row.values() == None:
              print(row)
print('--------------\n')

for row in data:
        if row["temperature"] == None or row["demand"] == None:
              print(row)
print('--------------\n')
for row in data:
        if row["temperature"] is None or row["demand"] is None:
              print(row)
print('--------------\n')
for row in data:
    for value in row.values():
        if value == None:
            print(row)
print('--------------\n')
for row in data:
    if any(value is None for value in row.values()):
        print(row)
print('--------------\n')

# =====================================
# Step 6: Compute average temperature (ignore None)
# =====================================
total_temp = 0
count = 0
for row in data:
       if row['temperature'] is not None:
              total_temp += row['temperature']
              count += 1

average_temp = total_temp / count
print('Average temperature:', average_temp)
print('--------------\n')

# =====================================
# Step 7 — Fill missing temperature values
# =====================================
for row in data:
       if row['temperature'] is None:
              row['temperature'] = average_temp

print('Dataset after filling missing temperature values:')
for row in data:
       print(row)
print('==============\n')

# =====================================
# Step 8 — Remove rows with missing demand
# =====================================  
clean_data = []
for row in data:
       if row['demand'] is not None:
              clean_data.append(row) 
print('Dataset after removing rows with missing demand:\n')
for row in clean_data:
       print(row)

print('==============\n')
# =====================================
# Step 9: Compute average demand
# =====================================
total_demand = 0
count = 0

for row in clean_data:
       total_demand += row['demand']
       count += 1           
average_demand = total_demand / count
print('Average demand:', average_demand)
print('==============\n')   


# =====================================
# Step 10 — Add new calculated column
# =====================================

for row in clean_data:
    row["demand_per_degree"] = row["demand"] / row["temperature"]

print("\nDataset with new column:")

for row in clean_data:
    print(row)

print('==============\n')
