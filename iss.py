import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import requests
import json
from PIL import Image

#caching data
def fetch_data(link):
    response =  requests.get(link)
    data = json.loads(response.text)
    return data

astronauts = fetch_data("http://api.open-notify.org/astros.json")

iss = fetch_data('http://api.open-notify.org/iss-now.json')

# set title
st.title('Space Cowboys')

# add description
st.markdown('This page displays the names of the astronauts who are currently out in space. Additionally, the location of the ISS is shown. 🚀')

#add picture
st.image('https://airbus-h.assetsadobe2.com/is/image/content/dam/stock-and-creative/imagery/generic-press-images/space-generic-1.jpg?wid=1920&fit=fit,1&qlt=85,0')


# show total number and names of the people in space
st.subheader('Total number:')

st.subheader('')
st.markdown(astronauts['number'])

st.subheader('People in Space:')

for person in astronauts['people']:
    st.markdown(person['name'])

# show ISS location as a map
st.subheader('ISS Location:')

lat = float(iss['iss_position']['latitude'])
lon = float(iss['iss_position']['longitude'])


df = pd.DataFrame([lat, lon])
df = df.transpose()
df.columns=['lat', 'lon']

st.markdown('This map shows the current position of the ISS.')

st.map(df, zoom=1)