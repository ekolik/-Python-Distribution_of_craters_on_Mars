Project for the Regression Modeling in Practice course on Coursera

### Introduction to Regression
*Sample*

The data is taken from the Mars Craters Study ([Mars Crater codebook (.pdf)](https://d396qusza40orc.cloudfront.net/phoenixassets/data-management-visualization/Mars%20Crater%20Codebook.pdf), [Mars Crater data file (.csv)](https://d396qusza40orc.cloudfront.net/phoenixassets/data-management-visualization/marscrater_pds.csv)), which is created by Stuart Robbins and presents a new global database for Mars that contains 378,540 craters statistically complete for diameters ≥ 1km. This dataset provides the following information about the craters: the latitude and longitude of a crater, its depth and diameter, number of layers in a crater, the presence of ejecta and morphology if its layers. 

*Procedure*

The data was collected by a multi-stage process of identification and analysis conducted by Stuart Robbins in 2009. According to his [paper](http://about.sjrdesign.net/research_mars.html#crater_database_mars), his work involved examining the global daytime thermal infrared [mosaic of Mars](http://www.mars.asu.edu/data/thm_dir/), which was collected during [THEMIS mission](http://www.nasa.gov/mission_pages/themis/mission/index.html), and marking every resolved crater in this mosaic. *The researcher allowed ~500m spacing between point resolution and looked for ≥ 5 points along a crater rim which limits the diameter to ~700-800 meters. He estimates the statistical completeness to be at ~1.0 km.* *

\* *It looks confusing, but it's the most comprehensible explanation I was able to find. :)*

*Measures*

Here are the measures of the data collected:
* Latitude and longitude of a crater are in decimal degrees North and East respectively. These coordinates represent the derived center of a non-linear least squares circle that was fit to the vertices identifying the crater rim. In other words, the coordinates indicate the estimated center of a crater.
* Diameter of a crater is in km. It is equal to the diameter of a non-linear least squares circle fit to the vertices identifying the crater rim.
* Depth of a crater is in km. It is equal to the average elevation of each of the manually determined 5 points along (or inside) the crater rim.
* Number of layers is in the 0-to-5 range. It is equal to the maximum number of cohesive layers in any reliably identified azimuthal direction.
* Crater ejecta is described by categorical codes. The codes indicate if the ejecta is hummocky with short lobes, smooth with short lobes, hummocky with splash, or smooth with splash. The ejecta shape might be: pin-cushion, pedestal, sandbar, bumblebee, butterfly, pseudo-butterfly, or rectangular.

As one part of my work, I evaluate the distribution of craters by calculating and comparing the square acreages of craters separately on each of the 4 quadrants of Mars: north-western, north-eastern, south-western, and south-eastern. To find the square acreage of craters on one quadrant, I first calculate and then sum up the square acreages of all craters with centers within this quadrant.
