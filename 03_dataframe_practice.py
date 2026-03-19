
import pandas as pd

# =====================================
# Step 1 — Create DataFrame (from list of dictionaries)
# =====================================

data = [ {"city": "Oslo",      "temperature": 5,    "demand": 120},
         {"city": "Bergen",    "temperature": None, "demand": 110},
         {"city": "Trondheim", "temperature": 2,    "demand": None},
         {"city": "Stavanger", "temperature": 7,    "demand": 100}        
      ]

df = pd.DataFrame(data)

print('=================================')
print("Raw Data:")
print(data)
print('---------------------------------')
print("Original DataFrame:")
print(df)
print('=================================')

# =====================================
# Step 2 — Create DataFrame (from dictionaries of list)
# =====================================

data2 = {"city":        ["Oslo", "Bergen", "Trondheim", "Stavanger" ],
         "temperature": [5, None, 2,7],
         "demand":      [120, 110, None, 100]
         }

df2 = pd.DataFrame(data2)

print('=================================')
print("Raw Data2:")
print(data2)
print('---------------------------------')
print("Original DataFrame:")
print(df2)
print('=================================')

# =====================================
# Step 3 — Inspect data
# =====================================

print('\nHead:')
print(df.head())