import pandas as pd

data = pd.read_csv('california_housing_test.csv')

res = data[(data['population'] > 0) & (data['population'] < 500)].median_house_value.mean()
print(res)
