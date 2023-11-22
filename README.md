# CSCI303-final-project

**Model Selection: identify and describe the algorithm(s) used and why; this can be using the techniques we discuss in class or other machine learning algorithm(s) of your choice.** \
We used scipy.optimize.minimize alongside a custom function to run the inversion of the anomaly geometry. The goal here is to minimize a function that returns the total distance from the modeled data to the observed data at each point.

**Results & Evaluation: report the conclusions and results of your analysis including validation metrics, techniques, and visualizations.**
The geometry of the model that was produced is similar to the real geometry. The biggest difference is in the bottom portions of the geometries, they taper down in the inverted model where they do not in the real geometry. This is because the bottom portion of the geometry does not affect the gravity anomaly as much and the model we ran is only with one polygon.

**Future Work: explain what potential next steps or what other questions could be explored based on the results of your work, or given more time.**
The next steps would be running this model with more polygons until the output was accurate to the actual geometry.
![image](https://github.com/Jalen-Perkins/CSCI303-final-project/assets/118387392/02df1bbf-06a5-4b00-a5f9-960d968b8aba)


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Jalen-Perkins/CSCI303-final-project/main)
