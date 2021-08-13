import streamlit as st
import datetime
import pandas as pd
import numpy as np
import requests


'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')


## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

st.markdown('''please provide :
- date and time ''')

d = st.date_input(
    "When do you want your taxi",
    datetime.date(2019, 7, 6))
st.write('You want a ride on :', d)

t = st.time_input('What time would you like your taxi', datetime.time(8, 45))

st.write('you have requested a taxi for', t)

# interpolation
pickup_datetime= f"{d} {t}"

'pickup longitude'
pu_longitude = st.number_input('Insert pickup longitude')

st.write('you will be picked up from ', pu_longitude)

'pickup latitude'
pu_latitude = st.number_input('Insert pickup latitude')

st.write('you will be picked up from ', pu_latitude)

'dropoff longitude'
do_longitude = st.number_input('Insert drop off longitude')

st.write('you will be picked up from ', do_longitude)

'dropoff latitude'
do_latitude = st.number_input('Insert drop off latitude')

st.write('you will be picked up from ', do_latitude)

'passenger count'
pass_count = st.number_input('Insert no. of passengers')

st.write('number of passengers', pass_count)



'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...'''
dictionary = { 'pickup_datetime' : pickup_datetime, 'pickup_longitude' : pu_longitude, 'pickup_latitude' : pu_latitude,'dropoff_longitude' : do_longitude, 'dropoff_latitude': do_latitude, 'passenger_count': int(pass_count) }

'''3. Let's call our API using the `requests` package...'''

test = requests.get(url, dictionary).json()

st.write(test['prediction'])

'''4. Let's retrieve the prediction from the **JSON** returned by the API...'''



## Finally, we can display the prediction to the user

