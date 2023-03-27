import pandas as pd
from datetime import datetime
import altair as alt
import streamlit as st

# preprocessing
df = pd.read_csv('all fit data.csv')
df['Date'] = df['Date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
df['Hour of day'] = df['Time'].apply(lambda x: x.split(':')[0])

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['Day of week'] = df['Date'].apply(lambda x: days[x.weekday()])

# heading
st.header('Google fit graph')

# input data
attribute = st.selectbox('Attribute', ('Calories (kcal)', 'Heart Points', 'Heart Minutes', 'Step count'))
weekday = st.selectbox('Day of the week', ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))

# data filtering
df = df[df['Day of week'] == weekday]
dff = df.groupby(['Hour of day']).mean()[attribute].reset_index()

# graph using altair
linegraph = alt.Chart(dff).mark_line().encode(
    x='Hour of day',
    y=attribute
)

# output
st.altair_chart(linegraph)
