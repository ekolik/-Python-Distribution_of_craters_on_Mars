# -Python-Distribution-of-craters-on-Mars
Project for Data Management and Visualization on Coursera

## Introduction
There are hundreds of thousands of impact craters on Mars, and they are essential to understanding the modification events on Mars and its surface ages. Around 4 billion years ago Mars was heavily bombarded by asteroids, comets, and proto-planets. Let's assume that these celestial bodies had been attacking all parts of the surface of Mars evenly, with the same frequency. This results in craters being evenly distributed over the surface of Mars. We know that Mars wasn't heavily attacked by celestial bodies since that time, but there are volcanoes on Mars, which could have erupted with the resulting lava covering up some of the craters. Had it happened? In this project we try to understand it. So, the goal of this research is to get the general idea of the craters' distribution on the surface of Mars. It is not important to discover all the details about this distribution, but it is interesting to know if, for example, the craters are concentrated in one part of Mars. If it is true, then we can suggest that this part is very old, and other parts are younger and have more active volcanoes (which have covered the craters).  

## Data
The data for this project is taken from the Mars Craters Study ([Mars Crater codebook (.pdf)](https://d396qusza40orc.cloudfront.net/phoenixassets/data-management-visualization/Mars%20Crater%20Codebook.pdf), [Mars Crater data file (.csv)](https://d396qusza40orc.cloudfront.net/phoenixassets/data-management-visualization/marscrater_pds.csv)), which is created by Stuart Robbins and presents a new global database for Mars that contains 378,540 craters.

From the data set we use the following columns (the description of these columns can be found in the codebook):
* **LATITUDE_CIRCLE_IMAGE**,
* **LONGITUDE_CIRCLE_IMAGE**,
* **DIAM_CIRCLE_IMAGE**.

We will use these data for calculating the location and square area of the craters.

## Approach
We will evaluate the distribution of craters by calculating and comparing the square acreages of craters separately on each of the 4 quadrants of Mars: north-western, north-eastern, south-western, and south-eastern. To find the square acreage of craters on one quadrant we first calculate and then sum up the square acreages of all craters with centers within this quadrant.

## Literature review
In order to discover if the question of the project has already been answered in other papers, the Internet was searched for the terms: "*mars crater facts*", "*mars crater distribution*", "*mars crater density*". The related sources that have been found and reviewed are listed is in the **Resources** section. 

During the review it was discovered that the southern hemisphere of Mars contains more and larger craters than the northern. The southern hemisphere is older, and its surface wasn't significantly modified after the period of "heavy bombardment" by asteroids. On the contrary, the surface of the northern hemisphere is much younger and has likely been modified after the "bombardment" by volcanic activity. 

No information have been found about the density of craters on western and eastern hemispheres. It might be caused by the absence of significant difference in this density on these hemispheres. The results of this project will give us some evidence. 
## Resources
* https://en.wikipedia.org/wiki/List_of_craters_on_Mars;
* https://en.wikipedia.org/wiki/Geology_of_Mars;
* http://geology.isu.edu/wapi/Geo_Pgt/Mod09_Mars/mars.htm;
* http://www.space.com/47-mars-the-red-planet-fourth-planet-from-the-sun.html;
* http://nineplanets.org/mars.html;
* http://theplanets.org/mars/.

## Workflow
There are the [code](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/main.py) and its [output](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/main_output.txt) that are made for the purpose of the project. 

During the execution of the code, the dataset was downloaded and examined for the variables that are important for the project. Firstly, it was checked that all observations (all craters) have data about their coordinates and diameter's length. In other words, there are no missing data in these variables. Then, the following data were calculated:
* the number and percentage of the craters that belong to each quadrant;
* the sums of the craters' squared areas for each quadrant;
* the descriptive statistics of the craters' squared areas.

Based on the results of the calculations, the following observations were made:
* the south-eastern quadrant contains the biggest percentage of the craters, and the north-western - the smallest;
* the sum of the craters' squared radii on the south-eastern quadrant is the biggest, and on the north-western - the smallest;
* almost half of all craters have a diameter equal to 1 km, and only two craters have a diameter longer than 1000 km.

To visualize the data, the following plots were created:
* the counts of the craters on each quadrant ([view](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/craters_density.png));
* the distribution of the craters from south to north ([view](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/hist_latitude.png));
* the distribution of the craters from west to east ([view](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/hist_longitude.png));
* the map of the craters with the squared area equal to or greater than the sum of the mean of the squared areas of all craters plus one standard deviation from that mean ([view](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/crater_map.png));
* the categorical plot of the squared areas of the craters per each quadrant ([view](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/sizes_distr.png)). 

## Results and conclusions
Examination of the plots led to the following conclusions:
* The quadrants of Mars can be sorted by the increasing number of craters they contain in the following way: north-western, north-eastern, south-western, and south-eastern. This proves that, in particular, the southern hemisphere has more craters than the northern, and the eastern - more than western.
* Not only the number of craters but their sizes also increase with the quadrants sorted in the way showed above (north-western, north-eastern, south-western, and south-eastern). For example, the south-eastern quadrant contains not only the biggest number of the craters but also most of the largest ones. Conversely, the north-western quadrant contains not only the smallest number of the craters but also most of the smallest ones.
* The majority of the craters are located near the equator of Mars, just a little to its south.
* The majority of the craters with the biggest squared area are located in the southern hemisphere (in its east-southern quadrant, to be precise).

The exploration of this topic is continued in the [Data Analysis](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/Data_analysis.md) section.
