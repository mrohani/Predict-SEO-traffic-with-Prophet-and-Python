# Predict-SEO-traffic-with-Prophet-and-Python

In the first step, you should pay attention to these two things

1_The more historical data we have, the more accurate our model and therefore our predictions will be.
2_The predictive model will only be valid if the internal factors remain the same and there are no external factors affecting it.

# Getting the data from Google Analytics
We can use the data in two ways
Export data from Google Analytics or use the Google Analytics API

# Excel file 
<p >
  <img src="https://rouhani.in/wp-content/uploads/2021/07/Screen-Shot-2021-07-01-at-12.04.15-AM.png">
</p>

get this data from Google Analytics is going to the Channels section on the side bar, clicking on Organic and exporting 

# Google Analytics API
First of all, in order to make use of Google Analytics API, we need to create a project on Google’s developer console, enable the Google Analytics Reporting service and get the credentials
After authenticating, we just need to make the request. The one that we need to use to get the data about the organic sessions for each day

# Adapting the lists to Dataframes

o make use of Prophet we need to input a Dataframe with two columns that need to be named: “ds” and “y”. If you have imported the data from an Excel file, we already have it as a Dataframe so you will only need to name the colums “ds” and “y”:


# Training the model
<p >
  <img src="https://rouhani.in/wp-content/uploads/2021/07/Screen-Shot-2021-07-01-at-12.09.59-AM.png">
</p>
Once we have the Dataframe with the required format,

# Making our predictions
<p >
  <img src="https://rouhani.in/wp-content/uploads/2021/07/Screen-Shot-2021-07-01-at-12.09.49-AM.png">
</p>
