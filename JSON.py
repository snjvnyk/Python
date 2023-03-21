import pandas as pd

with open('cruise_ship_schema.json', 'r') as f:
  data = json.load(f)

print(data['crew'])

