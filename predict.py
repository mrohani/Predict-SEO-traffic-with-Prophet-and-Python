import pandas as pd

df = pd.read_excel ('.xlsx', sheet_name= "")
df = df.drop(len(df) - 1)

We can draw with Matplotlib how the data looks like:

from matplotlib import pyplot

df["Sesiones"].plot(title = "Sesiones")
pyplot.show()



from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = ''
VIEW_ID = ''

credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
analytics = build('analyticsreporting', 'v4', credentials=credentials)


response = analytics.reports().batchGet(body={
  'reportRequests': [{
  'viewId': VIEW_ID,
  'dateRanges': [{'startDate': '2020-09-01', 'endDate': '2021-01-31'}],
  'metrics': [
    {"expression": "ga:sessions"}
  ], "dimensions": [
    {"name": "ga:date"}
  ],
"filtersExpression":"ga:channelGrouping=~Organic",
"includeEmptyRows": "true"
}]}).execute()


	df.columns = ['ds', 'y']


	from pandas import DataFrame
df_sessions = DataFrame(list_values,columns=['ds','y'])




import fbprophet
from fbprophet import Prophet

model = Prophet()
model.fit(df_sessions)



from pandas import to_datetime

forecast_days = []
for x in range(1, 28):
date = "2021-02-" + str(x)
forecast_days.append([date])
forecast_days = DataFrame(forecast_days)
forecast_days.columns = ['ds']
forecast_days['ds']= to_datetime(forecast_days['ds'])


forecast = model.predict(forecast_days)


from matplotlib import pyplot
model.plot(forecast)
pyplot.show()



train = df_sessions.drop(df_sessions.index[-12:])
future = df_sessions.loc[df_sessions["ds"]> train.iloc[len(train)-1]["ds"]]["ds"]




from sklearn.metrics import mean_absolute_error
import numpy as np
from numpy import array

#We train the model
model = Prophet()
model.fit(train)

#Adapt the dataframe that is used for the forecast days to Prophet’s required format.
future = list(future)
future = DataFrame(future)
future = future.rename(columns={0: 'ds'})

# We make the forecast
forecast = model.predict(future)

# We calculate the MAE between the actual values and the predicted values
y_true = df_sessions['y'][-12:].values
y_pred = forecast['yhat'].values
mae = mean_absolute_error(y_true, y_pred)

# We plot the final output for a visual understanding
y_true = np.stack(y_true).astype(float)
pyplot.plot(y_true, label='Actual')
pyplot.plot(y_pred, label='Predicted')
pyplot.legend()
pyplot.show()
print(mae)