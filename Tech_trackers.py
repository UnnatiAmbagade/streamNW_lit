import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium

# Sample data for restaurants
restaurants = pd.DataFrame({
    'Name': ['Famous Eatery 1', 'Famous Eatery 2', 'Nearby Café 1', 'Nearby Diner 2'],
    'Type': ['Famous', 'Famous', 'Nearby', 'Nearby'],
    'Cuisine': ['Italian', 'French', 'American', 'Mexican'],
    'Rating': [4.5, 4.7, 4.3, 4.1],
    'Latitude': [40.748817, 40.741895, 40.730610, 40.732013],
    'Longitude': [-73.985428, -73.989308, -73.935242, -73.954987]
})

# Sidebar for user input
st.sidebar.title("Restaurant Finder")
search_option = st.sidebar.selectbox("Search for:", ["Famous Places", "Nearby Places"])
cuisine_option = st.sidebar.multiselect("Cuisine Type", restaurants['Cuisine'].unique())

# Filter data based on user input
filtered_data = restaurants[(restaurants['Type'] == search_option.split()[0]) & 
                            (restaurants['Cuisine'].isin(cuisine_option))]

st.title("Food & Beverage Finder")

# Display recommendations
st.header(f"Top {search_option}")
for i, row in filtered_data.iterrows():
    st.subheader(f"{row['Name']} ({row['Cuisine']})")
    st.write(f"Rating: {row['Rating']}")

# Map visualization
st.header("Location of Restaurants")
m = folium.Map(location=[filtered_data['Latitude'].mean(), filtered_data['Longitude'].mean()], zoom_start=13)

for i, row in filtered_data.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Name']).add_to(m)

st_folium(m, width=700)

# Placeholder for future features
st.sidebar.title("Upcoming Features")
st.sidebar.write("1. User Reviews & Ratings")
st.sidebar.write("2. Personalized Recommendations")
st.sidebar.write("3. Booking & Reservations")
