import pandas as pd
import numpy as np

# reading CSV file
data = pd.read_csv('sales.csv')

# converting column data to list
sales = data['sales'].tolist()

print(len(sales))


# an average needs to find the sum and then divide by the number of entries