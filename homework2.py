import pandas as pd

data = pd.read_csv('california_housing_test.csv')

min_population = data.population.min()
res = data[data['population'] == min_population].households.max()
print(res)