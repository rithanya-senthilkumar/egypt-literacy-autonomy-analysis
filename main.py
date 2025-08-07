# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame

# If you wish change which data set you are working with, do that here: 
lwd=pd.read_csv("livwell135.csv")

# Add Step 1 code here:
indiaBooleanList = lwd["country_name"]=="India"
egyptBooleanList = lwd["country_name"]=="Egypt"
indiaCountryData = lwd.loc[indiaBooleanList]
egyptCountryData = lwd.loc[egyptBooleanList]

plt.scatter(data = indiaCountryData, x = 'WK_working12_p', y = 'ED_attainment_primary_completed_p', label = "India")
plt.scatter(data = egyptCountryData, x = 'WK_working12_p', y = 'ED_attainment_primary_completed_p', label = "Egypt")
plt.xlabel("Women who worked in the past 12 months (%)")
plt.ylabel("Women with completed primary education (%)")
plt.xlim(0, 100)
plt.legend()
plt.show()
# why wont my labels show up
