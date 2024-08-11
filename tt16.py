import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Sample data for restaurants
data = {
    'Name': [
        'Bella Italia', 'Paris Bistro', 'Downtown Grill', 'Sunset Cantina', 'Tokyo Delights', 'Bangkok Café', 'Curry Corner',
        'Roma Trattoria', 'Bistro Lumière', 'The Urban Café', 'El Camino', 'Sushi Haven', 'Thai Street Food', 'Spice Palace',
        'Liberty Diner', 'Aztec Grill', 'Kyoto Kitchen', 'Siam Square', 'Royal Indian Restaurant',
        'La Dolce Vita', 'Château de Cuisine', 'The Great American', 'Cantina Mexicana', 'Zen Sushi Bar', 'Thai Orchid', 'Spicy Curry House',
        'Trattoria da Vinci', 'Café du Palais', 'The Golden Grill', 'El Toro Bravo', 'Mount Fuji Sushi', 'Thai Essence', 'Tandoori Treasure',
        'Piazza Italia', 'Brasserie Belle', 'The Majestic Diner', 'La Fiesta', 'Shogun Sushi House', 'Thai Fusion', 'Maharaja\'s Feast'
    ],
    'Type': [
        'Famous', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby',
        'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby',
        'Famous', 'Famous', 'Famous', 'Famous', 'Famous',
        'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby',
        'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby',
        'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby'
    ],
    'Cuisine': [
        'Italian', 'French', 'American', 'Mexican', 'Japanese', 'Thai', 'Indian',
        'Italian', 'French', 'American', 'Mexican', 'Japanese', 'Thai', 'Indian',
        'Italian', 'French', 'American', 'Mexican', 'Japanese', 'Thai', 'Indian',
        'Italian', 'French', 'American', 'Mexican', 'Japanese', 'Thai', 'Indian',
        'Italian', 'French', 'American', 'Mexican', 'Japanese', 'Thai', 'Indian'
    ],
    'Rating': [
        4.5, 4.7, 4.3, 4.1, 4.8, 4.4, 4.9,
        4.6, 4.8, 4.2, 4.3, 4.9, 4.4, 4.6,
        4.7, 4.9, 4.5, 4.3, 4.8,
        4.6, 4.8, 4.4, 4.5, 4.9, 4.3, 4.6,
        4.7, 4.9, 4.3, 4.5, 4.9, 4.3, 4.7,
        4.8, 4.6, 4.4, 4.5, 4.9, 4.6, 4.8
    ],
    'Price_Range': [
        '₹500-1000', '₹500-1000', '₹500-1000', '₹500-1000', '₹500-1000', '₹500-1000', '₹500-1000',
        '₹800-1500', '₹800-1500', '₹800-1500', '₹800-1500', '₹800-1500', '₹800-1500', '₹800-1500',
        '₹1000-2000', '₹1000-2000', '₹1000-2000', '₹1000-2000', '₹1000-2000', '₹1000-2000', '₹1000-2000',
        '₹1200-2200', '₹1200-2200', '₹1200-2200', '₹1200-2200', '₹1200-2200', '₹1200-2200', '₹1200-2200',
        '₹2000-3000', '₹2000-3000', '₹2000-3000', '₹2000-3000', '₹2000-3000', '₹2000-3000', '₹2000-3000',
        '₹3500-5000', '₹3500-5000', '₹3500-5000', '₹3500-5000', '₹3500-5000', '₹3500-5000', '₹3500-5000',
    ],
    'Latitude': [
        28.613940, 28.704060, 28.613940, 28.704060, 28.613940, 28.704060, 28.613940,
        28.704060, 28.613940, 28.704060, 28.613940, 28.704060, 28.613940, 28.704060,
        28.613940, 28.704060, 28.613940, 28.704060, 28.613940,
        28.704060, 28.613940, 28.704060, 28.613940, 28.704060, 28.613940, 28.704060,
        28.613940, 28.704060, 28.613940, 28.704060, 28.613940, 28.704060, 28.613940,
        28.704060, 28.613940, 28.704060, 28.613940, 28.704060, 28.613940, 28.704060
    ],
    'Longitude': [
        77.209021, 77.102493, 77.209021, 77.102493, 77.209021, 77.102493, 77.209021,
        77.102493, 77.209021, 77.102493, 77.209021, 77.102493, 77.209021, 77.102493,
        77.209021, 77.102493, 77.209021, 77.102493, 77.209021,
        77.102493, 77.209021, 77.102493, 77.209021, 77.102493, 77.209021, 77.102493,
        77.209021, 77.102493, 77.209021, 77.102493, 77.209021, 77.102493, 77.209021,
        77.102493, 77.209021, 77.102493, 77.209021, 77.102493, 77.209021, 77.102493
    ],
    'Address': [
        'Connaught Place, New Delhi', 'Sector 22, Chandigarh', 'South Delhi, New Delhi', 'Sector 17, Chandigarh', 'Sector 35, Chandigarh', 'South Delhi, New Delhi', 'Connaught Place, New Delhi',
        'Janpath, New Delhi', 'Central Delhi', 'Old Delhi', 'Central Delhi', 'Sector 17, Chandigarh', 'Central Delhi', 'Sector 35, Chandigarh',
        'Connaught Place, New Delhi', 'Sector 22, Chandigarh', 'South Delhi, New Delhi', 'Sector 17, Chandigarh', 'Connaught Place, New Delhi',
        'Janpath, New Delhi', 'Central Delhi', 'Old Delhi', 'Central Delhi', 'Sector 17, Chandigarh', 'Central Delhi', 'Sector 35, Chandigarh',
        'Connaught Place, New Delhi', 'Sector 22, Chandigarh', 'South Delhi, New Delhi', 'Sector 17, Chandigarh', 'Connaught Place, New Delhi',
        'Janpath, New Delhi', 'Central Delhi', 'Old Delhi', 'Central Delhi', 'Sector 17, Chandigarh', 'Central Delhi', 'Sector 35, Chandigarh'
    ]
}

# Create DataFrame
restaurants = pd.DataFrame(data)

# Streamlit app
st.title("Taste Tracker")

# Display all restaurants
st.header("All Restaurants")

# Display the DataFrame
st.write(restaurants)

# Map setup
m = folium.Map(location=[28.613940, 77.209021], zoom_start=10)

# Add restaurant markers to the map
for _, row in restaurants.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Name']}<br>{row['Cuisine']}<br>{row['Address']}",
        icon=folium.Icon(color='blue' if row['Type'] == 'Famous' else 'green')
    ).add_to(m)

# Display the map
st_folium(m)

# Thank you message on submit
if st.button("Submit"):
    st.write("Thank you for using Taste Tracker!")
