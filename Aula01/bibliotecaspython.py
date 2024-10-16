#To install libraries pip install library_name
#To use library, you need to import
#
# import math
#
# num = 16
#
# print(math.sqrt(num))

# import requests
#
# response = requests.get("https://leonsedov.github.io/portfolio/")
#
# print(response.text)

# import datetime
#
# now = datetime.datetime.now()
#
# print(now)

# import random
# num = random.randint(1, 100)
# print(num)

import pandas as pd

data = {
    "name": ['Fulano','Ciclano','Otavio'],
    "Age": [35, 43, 27],
    "City": ['Sao Paulo', 'Rio de Janeiro', 'Curitiba']
}
df = pd.DataFrame(data)
print("DataFrame criado:\n", df)

# names = df['name']
# print(names)
#
# first_line = df.iloc[0]
# print(first_line)

#Read data from a CSV file
df_csv = pd.read_csv('customers.csv')
print("\nDataFrame lido do CSV:\n", df_csv.head())

#Select the column "City"
cities = df['City']
print("\nCities:\n", cities)

#Filter customers that are older than 30 years old
filtered = df_csv[df_csv['Age'] > 30]
print("\nFiltro de Age:\n", filtered)
