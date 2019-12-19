import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


# Getting datasets
colors = pd.read_csv("datasets/colors.csv")
inventories = pd.read_csv("datasets/inventories.csv")
inventory_parts = pd.read_csv("datasets/inventory_parts.csv")
inventory_sets = pd.read_csv("datasets/inventory_sets.csv")
part_categories = pd.read_csv("datasets/part_categories.csv")
part_relationships = pd.read_csv("datasets/part_relationships.csv")
parts = pd.read_csv("datasets/parts.csv")
sets = pd.read_csv("datasets/sets.csv")
themes = pd.read_csv("datasets/themes.csv")



# Exploring first rows of datasets
print(colors.head())
print("")
print(inventories.head())
print("")
print(inventory_parts.head())
print("")
print(inventory_sets.head())
print("")
print(part_categories.head())
print("")
print(part_relationships.head())
print("")
print(parts.head())
print("")
print(sets.head())
print("")
print(themes.head())
print("")
