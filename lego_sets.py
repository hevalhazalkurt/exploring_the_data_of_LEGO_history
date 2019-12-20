import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


# Getting datasets
sets = pd.read_csv("datasets/sets.csv")
print(sets.head())


# Visualizing numbers of sets by year
sets.groupby('year')['name'].nunique().plot(kind='bar')
plt.title("The numbers of sets by year")
plt.xlabel("YEARS")
plt.ylabel("NUMBERS")
plt.show()


parts_by_year = sets[['year', 'num_parts']].groupby('year', as_index=False).mean()
parts_by_year.plot(x='year', y='num_parts', color="purple")
plt.title("Average number of parts by year")
plt.xlabel("YEAR")
plt.ylabel("PARTS")
plt.show()
