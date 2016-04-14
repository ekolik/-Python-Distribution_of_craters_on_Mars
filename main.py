import pandas as pd
import numpy
import seaborn
import matplotlib.pyplot as plt
import math

data = pd.read_csv('marscrater_pds.csv', low_memory=False)


def percent(sub_data):
    # the function returns the percent that the subset takes in the entire dataset
    return round(len(sub_data)/len(data)*100, 2)

# ------------- to print basic info about loaded dataset ----------------
# print(len(data))
# print(len(data.columns))
# print(list(data.columns.values))
# print(data.ix[:10,:4])

# ------------ to create the subsets of craters which are located in north-western, north-eastern,
# south-western, and south-eastern quadrants -------------------------------------
n_w = data[(data["LATITUDE_CIRCLE_IMAGE"] >= 0) & (data["LONGITUDE_CIRCLE_IMAGE"] < 0)]
n_e = data[(data["LATITUDE_CIRCLE_IMAGE"] > 0) & (data["LONGITUDE_CIRCLE_IMAGE"] >= 0)]
s_w = data[(data["LATITUDE_CIRCLE_IMAGE"] < 0) & (data["LONGITUDE_CIRCLE_IMAGE"] <= 0)]
s_e = data[(data["LATITUDE_CIRCLE_IMAGE"] <= 0) & (data["LONGITUDE_CIRCLE_IMAGE"] > 0)]

# ------------ to check that all craters were selected into one subset or another ----
# print(len(n_w) + len(s_w) + len(n_e) + len(s_e) == len(data))

# ------------ to print which percent of craters belongs to each quadrant ----------
print('There are {} craters on Mars.'.format(len(data)))
print()
print('The north-western quadrant contains {} craters, or {}% of all craters.'.format(len(n_w), percent(n_w)))
print('North-eastern: {} craters, or {}%.'.format(len(n_e), percent(n_e)))
print('South-western: {} craters, or {}%.'.format(len(s_w), percent(s_w)))
print('South-eastern: {} craters, or {}%.'.format(len(s_e), percent(s_e)))
print()

# ------------ to print frequency distributions of craters' diameters ------
# data["DIAM_INT"] = data["DIAM_CIRCLE_IMAGE"].round()
# print("This is the frequency distribution of the craters' diameters. I-st column is the diameter length; II-nd - its frequency.")
# print(data.groupby("DIAM_INT").size()*100 / len(data))
# print()
# ------------- to print quartile split of the diameter variable -----------------
# print("This is the quartile split of the craters' diameters. I-st column contains the intervals of diameters' length;")
# print("II-nd - the number of craters with the length of its diameter in the corresponding interval.")
# data["DIAM_QUART"] = pd.qcut(data["DIAM_CIRCLE_IMAGE"], 4)
# print(data.groupby("DIAM_QUART").size())
# print()

# -------------- to check for missing data in the diameter's column ------------------------
# print(pd.isnull(data["DIAM_CIRCLE_IMAGE"]).any())

# ------------ to create a new table with a column that indicates to which hemisphere a crater belongs ---------
n_w['HEMISPH'] = 'nw'
n_e['HEMISPH'] = 'ne'
s_w['HEMISPH'] = 'sw'
s_e['HEMISPH'] = 'se'

frames = [n_w, n_e, s_w, s_e]
new_data = pd.concat(frames)

# ---------------- to print the sum of the craters' squared areas for each quadrant of Mars -----
print("This is the sums of the craters' squared areas for each quadrant. I-st column is the abbreviation of a quadrant; II-nd - the indicated sum.")
new_data["SQUARED_AREA"] = ((new_data["DIAM_CIRCLE_IMAGE"]/2)**2*math.pi).round(2)
print(new_data.groupby(by=["HEMISPH"])['SQUARED_AREA'].sum())
print()
print("This is the descriptive statistics of the craters' squared areas")
print(new_data["SQUARED_AREA"].describe())



# ---------------- to subset useful columns for more convenient use -----------------------
new_data = new_data[["CRATER_NAME", "HEMISPH", "LATITUDE_CIRCLE_IMAGE", "LONGITUDE_CIRCLE_IMAGE", "DIAM_CIRCLE_IMAGE", "SQUARED_AREA"]]
# print(new_data.head(10))


# ---------------- visualization ----------------------------
new_data["HEMISPH"] = pd.Categorical(new_data["HEMISPH"])
seaborn.countplot(x="HEMISPH", data=new_data)
plt.xlabel("Quadrants of Mars: north-western, north-eastern, south-western, and south-eastern")
plt.title("Number of craters on each quadrant of Mars")
plt.show()

seaborn.distplot(new_data["LATITUDE_CIRCLE_IMAGE"], kde=False)
plt.xlabel("Latitude degree: from south (-90°) to north (90°)")
plt.title("Concentration of the craters on Mars from south to north")
plt.show()

seaborn.distplot(new_data["LONGITUDE_CIRCLE_IMAGE"], kde=False)
plt.xlabel("Longitude degree: from west (-1800°) to east (180°)")
plt.title("Concentration of the craters on Mars from west to east")
plt.show()


for_plot = new_data[new_data["SQUARED_AREA"] >= (new_data["SQUARED_AREA"].mean()+new_data["SQUARED_AREA"].std())]

seaborn.regplot(x="LONGITUDE_CIRCLE_IMAGE", y="LATITUDE_CIRCLE_IMAGE", fit_reg=False, data = for_plot)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("The craters with the squared area >= mean squared area + one standard deviation")
plt.show()


seaborn.factorplot(x="HEMISPH", y="SQUARED_AREA", data=new_data, kind="strip")
plt.xlabel("Quadrants of Mars: north-western, north-eastern, south-western, and south-eastern")
plt.ylabel("Crater's squared area, km")
plt.title("Sizes of the craters on each quadrant of Mars")
plt.show()