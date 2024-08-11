import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Sample data for restaurants
data = {
    'Name': ['Bella Italia', 'Paris Bistro'],
    'Cuisine': ['Italian', 'French'],
    'Rating': [4.5, 4.7],
    'Price_Range': ['₹500-1000', '₹500-1000'],
    'Latitude': [28.613940, 28.704060],
    'Longitude': [77.209021, 77.102493],
    'Address': ['Connaught Place, New Delhi', 'Sector 22, Chandigarh']
}

# Create DataFrame
try:
    restaurants = pd.DataFrame(data)
    st.write("DataFrame created successfully!")
except Exception as e:
    st.write(f"Error creating DataFrame: {e}")

# Streamlit app
st.title("Taste Tracker")

# Display all restaurants
st.header("All Restaurants")

# Display the DataFrame
st.write(restaurants)

# Map setup
m = folium.Map(location=[28.613940, 77.209021], zoom_start=10)

# Add restaurant markers to the map
try:
    for _, row in restaurants.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"{row['Name']}<br>{row['Cuisine']}<br>{row['Address']}",
            icon=folium.Icon(color='blue')
        ).add_to(m)
    st.write("Map created successfully!")
except Exception as e:
    st.write(f"Error creating map: {e}")

# Display the map
st_folium(m)

# Thank you message on submit
if st.button("Submit"):
    st.write("Thank you for using Taste Tracker!")
