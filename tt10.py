import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Updated sample data for restaurants
restaurants = pd.DataFrame({
    'Name': [
        'Bella Italia', 'Paris Bistro', 'Downtown Grill', 'Sunset Cantina', 'Tokyo Delights', 'Bangkok Café', 'Curry Corner',
        'La Dolce Vita', 'Château de Cuisine', 'The Great American', 'Cantina Mexicana', 'Zen Sushi Bar', 'Thai Orchid', 'Spicy Curry House',
        'Piazza Italia', 'Brasserie Belle', 'The Majestic Diner', 'La Fiesta', 'Shogun Sushi House', 'Thai Fusion', 'Maharaja\'s Feast'
    ],
    'Type': [
        'Famous', 'Famous', 'Nearby', 'Nearby', 'Famous', 'Nearby', 'Nearby',
        'Famous', 'Famous', 'Nearby', 'Nearby', 'Famous', 'Nearby', 'Nearby',
        'Famous', 'Famous', 'Nearby', 'Nearby', 'Famous', 'Nearby', 'Nearby'
    ],
    'Cuisine': [
        'Italian', 'French', 'American', 'Mexican', 'Japanese', 'Thai', 'Indian',
        'Italian', 'French', 'American', 'Mexican', 'Japanese', 'Thai', 'Indian',
        'Italian', 'French', 'American', 'Mexican', 'Japanese', 'Thai', 'Indian'
    ],
    'Rating': [
        4.5, 4.7, 4.3, 4.1, 4.8, 4.4, 4.9,
        4.6, 4.8, 4.2, 4.3, 4.7, 4.5, 4.8,
        4.7, 4.9, 4.6, 4.4, 4.9, 4.7, 4.8
    ],
    'Price_Range': [
        '₹500-1500', '₹500-1500', '₹500-1500', '₹500-1500', '₹500-1500', '₹500-1500', '₹500-1500',
        '₹1500-3000', '₹1500-3000', '₹1500-3000', '₹1500-3000', '₹1500-3000', '₹1500-3000', '₹1500-3000',
        '₹3000-5000', '₹3000-5000', '₹3000-5000', '₹3000-5000', '₹3000-5000', '₹3000-5000', '₹3000-5000'
    ],
    'Latitude': [
        28.613940, 28.613940, 28.704060, 28.613940, 28.704060, 28.613940, 28.613940,
        28.704060, 28.704060, 28.613940, 28.613940, 28.704060, 28.704060, 28.613940,
        28.613940, 28.613940, 28.704060, 28.704060, 28.613940, 28.704060, 28.704060
    ],
    'Longitude': [
        77.209021, 77.209021, 77.102493, 77.209021, 77.102493, 77.209021, 77.209021,
        77.102493, 77.102493, 77.209021, 77.209021, 77.102493, 77.102493, 77.209021,
        77.209021, 77.209021, 77.102493, 77.102493, 77.209021, 77.102493, 77.102493
    ],
    'Address': [
        'Connaught Place, New Delhi', 'Janpath, New Delhi', 'Sector 17, Chandigarh', 'South Delhi, New Delhi', 'Sector 22, Chandigarh', 'Connaught Place, New Delhi', 'Old Delhi',
        'Sector 35, Chandigarh', 'Sector 10, Noida', 'Central Delhi', 'South Delhi', 'Connaught Place, New Delhi', 'Sector 22, Chandigarh', 'South Delhi',
        'Janpath, New Delhi', 'Connaught Place, New Delhi', 'Sector 17, Chandigarh', 'Sector 22, Chandigarh', 'Sector 10, Noida', 'Central Delhi', 'Old Delhi'
    ]
})

# Main app content
st.title("Taste Tracker")

# Sidebar for user input
st.sidebar.title("Restaurant Finder")
search_option = st.sidebar.selectbox("Search for:", ["Famous Places", "Nearby Places"])
cuisine_option = st.sidebar.multiselect("Cuisine Type", restaurants['Cuisine'].unique())
price_option = st.sidebar.selectbox("Price Range", ['All'] + sorted(restaurants['Price_Range'].unique()))

# Filter data based on user input
if price_option == 'All':
    filtered_data = restaurants[
        (restaurants['Type'] == search_option.split()[0]) & 
        (restaurants['Cuisine'].isin(cuisine_option))
    ]
else:
    filtered_data = restaurants[
        (restaurants['Type'] == search_option.split()[0]) & 
        (restaurants['Cuisine'].isin(cuisine_option)) & 
        (restaurants['Price_Range'] == price_option)
    ]

st.header(f"Top {search_option}")

if not filtered_data.empty:
    # Display filtered data
    for i, row in filtered_data.iterrows():
        st.subheader(f"{row['Name']} ({row['Cuisine']})")
        st.write(f"Rating: {row['Rating']} | Price Range: {row['Price_Range']}")
        st.write(f"Address: {row['Address']}")
        st.text_input(f"Review for {row['Name']}:", key=f"review_{i}")
        st.slider(f"Rate {row['Name']} (1 to 5):", 1, 5, 3, key=f"rating_{i}")

    # Map visualization
    st.header("Location of Restaurants")
    filtered_data_clean = filtered_data.dropna(subset=['Latitude', 'Longitude'])
    
    if not filtered_data_clean.empty:
        center_lat = 20.593684
        center_lon = 78.962880
        m = folium.Map(location=[center_lat, center_lon], zoom_start=5)

        for i, row in filtered_data_clean.iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=row['Name'],
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(m)

        st_folium(m, width=700)
    else:
        st.write("No valid locations available to display on the map.")
else:
    st.write("No restaurants match your criteria. Here are some popular recommendations:")
    default_recommendations = pd.DataFrame({
        'Name': ['The Spice Hub', 'Café Delight', 'The Royal Feast'],
        'Type': ['Famous', 'Nearby', 'Famous'],
        'Cuisine': ['Indian', 'Italian', 'French'],
        'Rating': [4.8, 4.5, 4.7],
        'Price_Range': ['₹1500-2500', '₹1200-2000', '₹2000-3500'],
        'Latitude': [28.613940, 28.704060, 28.613940],
        'Longitude': [77.209021, 77.102493, 77.209021],
        'Address': ['Connaught Place, New Delhi', 'Sector 35, Chandigarh', 'Janpath, New Delhi']
    })
    
    for i, row in default_recommendations.iterrows():
        st.subheader(f"{row['Name']} ({row['Cuisine']})")
        st.write(f"Rating: {row['Rating']} | Price Range: {row['Price_Range']}")
        st.write(f"Address: {row['Address']}")
        st.text_input(f"Review for {row['Name']}:", key=f"default_review_{i}")
        st.slider(f"Rate {row['Name']} (1 to 5):", 1, 5, 3, key=f"default_rating_{i}")

# Admin functionality: Add a new restaurant
st.sidebar.title("Admin Section")
st.sidebar.subheader("Add New Restaurant")

with st.sidebar.form(key='admin_form'):
    name = st.text_input("Restaurant Name")
    type_ = st.selectbox("Type", ["Famous", "Nearby"])
    cuisine = st.selectbox("Cuisine", ['Italian', 'French', 'American', 'Mexican', 'Japanese', 'Thai', 'Indian'])
    rating = st.slider("Rating (1 to 5)", 1, 5, 3)
    price_range = st.text_input("Price Range (e.g., ₹1000-2000)")
    latitude = st.number_input("Latitude", format="%.6f")
    longitude = st.number
