# -Python-Distribution-of-craters-on-Mars
Project for Data Management and Visualization on Coursera

## Introduction
There are hundreds of thousands of impact craters on Mars, and they are essential to understanding the modification events on Mars and its surface ages. Around 4 billion years ago Mars was heavily bombarded by asteroids, comets, and proto-planets. Let's assume that these celestial bodies had been attacking all parts of the surface of Mars evenly, with the same frequency. This resulted in craters being evenly distributed over the surface of Mars. We know that Mars wasn't heavily attacked by celestial bodies since that time, but there are volcanoes on Mars, which could have erupted with the resulting lava covering up some of the craters. Had it happened? In this project we try to understand it. So, the goal of this research is to get the general idea of the craters' distribution on the surface of Mars. It is not important to discover all the details about this distribution, but it is interesting to know if, for example, the craters are concentrated in one part of Mars. If it is true, then we can suggest that this part is very old, and other parts are younger and have more active volcanoes (which have covered the craters).  

## Data
The data for this project is taken from the Mars Craters Study([Mars Crater codebook (.pdf)](https://d396qusza40orc.cloudfront.net/phoenixassets/data-management-visualization/Mars%20Crater%20Codebook.pdf), [Mars Crater data file (.csv)](https://d396qusza40orc.cloudfront.net/phoenixassets/data-management-visualization/marscrater_pds.csv)), which is created by Stuart Robbins and presents a new global database for Mars that contains 378,540 craters.

From the data set we use the following columns (the description of these columns can be found in the codebook):
* **LATITUDE_CIRCLE_IMAGE**,
* **LONGITUDE_CIRCLE_IMAGE**,
* **DIAM_CIRCLE_IMAGE**.

We will use these data for calculating the location and square area of the craters.

## Approach
We will evaluate the distribution of craters by calculating and comparing the square acreages of craters separately on each of the 4 hemispheres of Mars: northern-western, northern-eastern, southern-western, and southern-eastern. To find the square acreage of craters on one hemisphere we first calculate and then sum up the square acreages of all craters with centers within this hemisphere. 

## Resources
* https://en.wikipedia.org/wiki/List_of_craters_on_Mars;
* http://www.space.com/47-mars-the-red-planet-fourth-planet-from-the-sun.html;
* http://nineplanets.org/mars.html;
* http://theplanets.org/mars/.
