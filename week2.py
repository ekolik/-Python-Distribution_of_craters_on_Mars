import pandas as pd
import numpy

data = pd.read_csv('marscrater_pds.csv', low_memory=False)


def percent(sub_data):
    # the function returns the percent that the subset takes in the entire dataset
    return round(len(sub_data)/len(data)*100, 2)

# ------------- to print basic info about loaded dataset ----------------
# print(len(data))
# print(len(data.columns))
# print(list(data.columns.values))
# print(data.ix[:10,:4])

# ------------ to create the subsets of craters which are located in north-western, south-western,
# north-eastern, and south-eastern hemispheres -------------------------------------
n_w = data[(data["LATITUDE_CIRCLE_IMAGE"] >= 0) & (data["LONGITUDE_CIRCLE_IMAGE"] < 0)]
s_w = data[(data["LATITUDE_CIRCLE_IMAGE"] < 0) & (data["LONGITUDE_CIRCLE_IMAGE"] <= 0)]
n_e = data[(data["LATITUDE_CIRCLE_IMAGE"] > 0) & (data["LONGITUDE_CIRCLE_IMAGE"] >= 0)]
s_e = data[(data["LATITUDE_CIRCLE_IMAGE"] <= 0) & (data["LONGITUDE_CIRCLE_IMAGE"] > 0)]

# ------------ to check that all craters were selected into one subset or another ----
# print(len(n_w) + len(s_w) + len(n_e) + len(s_e) == len(data))

# ------------ to print which percent of craters belongs to each hemisphere ----------
print('There are {} craters on Mars.'.format(len(data)))
print()
print('The north-western hemisphere contains {} craters, or {}% of all craters.'.format(len(n_w), percent(n_w)))
print('South-western: {} craters, or {}%.'.format(len(s_w), percent(s_w)))
print('North-eastern: {} craters, or {}%.'.format(len(n_e), percent(n_e)))
print('South-eastern: {} craters, or {}%.'.format(len(s_e), percent(s_e)))
print()

# ------------ to create a new column with the craters' diameters rounded to integer --------
data["DIAM_INT"] = data["DIAM_CIRCLE_IMAGE"].round()

# ------------ to print frequency distributions of craters' diameters ------
print("This is the frequency distribution of the craters' diameters. I-st column is the diameter lenght; II-nd - its frequency.")
print(data.groupby("DIAM_INT").size()*100 / len(data))
print()

# ------------ to create a new table with a column that indicates to which hemisphere a crater belongs ---------
n_w['HEMISPH'] = 'nw'
s_w['HEMISPH'] = 'sw'
n_e['HEMISPH'] = 'ne'
s_e['HEMISPH'] = 'se'

frames = [n_w, s_w, n_e, s_e]
new_data = pd.concat(frames)

# ---------------- to print the sum of the craters' squared radiuses for each hemisphere -----
print("This is the sums of the craters' squared radiuses for each hemisphere. I-st column is the abbreviation of a hemisphere; II-nd - the indicated sum.")
new_data["SQUARE_RADIUS"] = ((new_data["DIAM_CIRCLE_IMAGE"]/2)**2).round(2)
print(new_data.groupby(by=["HEMISPH"])['SQUARE_RADIUS'].sum())