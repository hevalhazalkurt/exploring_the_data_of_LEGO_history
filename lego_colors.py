import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


# Getting datasets
colors = pd.read_csv("datasets/colors.csv")


# Exploring first rows of colors DataFrame
print(colors.head())


# Exploring colors
# Finding how many colors available
num_colors = len(colors)
print(num_colors)

# Finding numbers of transparent and non-transparent colors
trans_colors = colors.groupby("is_trans").count()
print(trans_colors)

# Visualizing transparent colors
colors.groupby('is_trans')['name'].nunique().plot(kind='bar', color=["purple", "violet"])
plt.title("The numbers of transparent and non-transparent colors")
plt.xlabel("is transparent?")
plt.ylabel("number")
plt.xticks(np.arange(2), ('False', 'True'), rotation=0)
plt.show()


# Add # sign to the values of "rgb" column
colors['rgb'] = colors['rgb'].apply(lambda x : '#'+x)
colors_rgb = dict(zip(colors.name, colors.rgb))


# Making color table
def colortable(colors, title, sort_colors=True, emptycols=0):

    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12
    topmargin = 40

    # Sort colors by hue, saturation, value and name.
    if sort_colors is True:
        by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(color))), name) for name, color in colors.items())
        names = [name for hsv, name in by_hsv]
    else:
        names = list(colors)

    n = len(names)
    ncols = 4 - emptycols
    nrows = n // ncols + int(n % ncols > 0)

    width = cell_width * 4 + 2 * margin
    height = cell_height * nrows + margin + topmargin
    dpi = 64

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(margin/width, margin/height, (width-margin)/width, (height-topmargin)/height)
    ax.set_xlim(0, cell_width * 4)
    ax.set_ylim(cell_height * (nrows-0.5), -cell_height/2.)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()
    ax.set_title(title, fontsize=24, loc="left", pad=10)

    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        swatch_end_x = cell_width * col + swatch_width
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(text_pos_x, y, name, fontsize=14,
                horizontalalignment='left',
                verticalalignment='center')

        ax.hlines(y, swatch_start_x, swatch_end_x,
                  color=colors[name], linewidth=18)

    return fig

colortable(colors_rgb, "All Lego Colors")
plt.show()



# Grouping main colors
color_names = list(colors_rgb.keys())

main_colors = {}

for color in color_names:
    color = color.replace("-", " ").split()
    if color[-1] in main_colors:
        main_colors[color[-1]] += 1
    else:
        main_colors[color[-1]] = 1


m_colors = {}

for color, num in main_colors.items():
    if int(num) >= 5:
        m_colors[color] = num


plt.bar(list(m_colors.keys()), m_colors.values(), align="center", edgecolor= "gray", color=[color.lower() for color in m_colors.keys()])
plt.xticks(range(len(m_colors)), list(m_colors.keys()), rotation=90)
plt.title("Main Colors of LEGO")
plt.show()
