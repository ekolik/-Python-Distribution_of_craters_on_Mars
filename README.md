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
We will evaluate the distribution of craters by calculating and comparing the square acreages of craters separately on each of the 4 hemispheres of Mars: north-western, north-eastern, south-western, and south-eastern. To find the square acreage of craters on one hemisphere we first calculate and then sum up the square acreages of all craters with centers within this hemisphere.

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
There are the current [code](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/main.py) and its [output](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/main_output.txt). During the execution of the code, the dataset was first downloaded and examined for the variables that are important for the project. Specifically, the following data were calculated:
* the number and percentage of the craters that belong to each hemisphere;
* the frequency distribution and quartile split of the craters' diameters;
* the sums of the craters' squared radii for each hemisphere.

Additionally, it was checked that all observations (all craters) have data about their coordinates and diameter's length. In other words, there are no missing data in these variables.

Based on the results of the calculations, the following observations were made:
* the south-eastern hemisphere contains the biggest percentage of the craters, and the north-western - the smallest;
* the sum of the craters' squared radii on the south-eastern hemisphere is the biggest, and on the north-western - the smallest;
* almost half of all craters have a diameter equal to 1 km, and only two craters have a diameter longer than 1000 km.

These results and observations are important for the purpose of the project and will be used for the final conclusions.
