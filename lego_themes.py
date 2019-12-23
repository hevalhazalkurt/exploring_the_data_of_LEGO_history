import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


# Getting datasets
sets = pd.read_csv("datasets/sets.csv")#.set_index("theme_id")
themes = pd.read_csv("datasets/themes.csv").set_index("id")

print(sets.head())
print("")
print(themes.head())

print("")


set_themes = sets["theme_id"].value_counts()
print(set_themes.head())
print("")

set_themes = pd.DataFrame({"id": set_themes.index, "count": set_themes.values})
print(set_themes.head())
print("")


set_themes = pd.merge(set_themes, themes, on="id")
print(set_themes.head())
print("")


set_themes_no_parent = set_themes[pd.isnull(set_themes["parent_id"])]
print(set_themes_no_parent)
print("")


set_themes_top_10 = set_themes_no_parent.sort_values(by=["count"], ascending=False)[:10]
top_10 = set_themes_top_10["count"]
top_10.index = set_themes_top_10["name"]

top_10.plot.bar(color="gold", rot=30)
plt.title("Top 10 Themes That Have Most Sets")
plt.show()
