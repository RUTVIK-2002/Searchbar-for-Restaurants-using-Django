# import csv
# import json

# data = []
# #count = 0

# with open('restaurants_small.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         try:
#             item_dict = {
#                 'id': int(row['id']),
#                 'name': row['name'],
#                 'location': row['location'],
#                 'items': json.loads(row['items']),
#                 'lat_long': row['lat_long'],
#                 'full_details': json.loads(row['full_details']) if row['full_details'] else {}  # Replace with default value if empty
#             }
#             data.append(item_dict)
#         except json.JSONDecodeError as e:
#             print(f"Error in row {row['id']}: {e}")

# Print the result
# for item in data:
#     print(item)
# print(data[0]['full_details']['location']['locality_verbose'])

import pandas as pd
data = pd.read_csv('restaurants_small.csv')
print(data['id'].nunique())