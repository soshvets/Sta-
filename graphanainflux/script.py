import math
import pandas as pd
from influxdb import DataFrameClient

#Connection with server
client = DataFrameClient(host='localhost', port=8086)
#Database metryki was created earlier on server
client.switch_database('metryki')

#Trygonometry calculation in scope (0, 2pi)
sinus_val = [round(math.sin(math.radians(i))*1000,2) for i in range(0,361)]
cosinus_val = [round(math.cos(math.radians(i))*1000,2) for i in range(0,361)]
tg_val = [round(math.tan(math.radians(i))*1000,2) for i in range(0,361)]

#Creating dataframe object to save on DB
df = pd.DataFrame(data=zip(sinus_val,cosinus_val, tg_val), 
                  index=pd.date_range(start='2022-07-01',periods=361, freq='H'),
                  columns=['sin','cos','tg'])

# Save data in database
client.write_points(df, measurement='trygonometria')
