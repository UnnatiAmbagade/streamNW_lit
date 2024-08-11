import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Sample data for restaurants
restaurants = pd.DataFrame({
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
        '₹3500-5000', '₹3500-5000', '₹3500-5000', '₹3500-5000', '₹3500-5000', '₹3500-5000', '₹3500-5000'
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
})

# Main app content
st.title("Taste Tracker")

# Sidebar for user input
st.sidebar.title("Restaurant Finder")
search_option = st.sidebar.selectbox("Search for:", ["Famous Places", "Nearby Places"])
cuisine_option = st.sidebar.multiselect("Cuisine Type", restaurants['Cuisine'].unique())
price_option = st.sidebar.selectbox("Price Range", ['All'] + sorted(restaurants['Price_Range'].unique()))

# Create a form with submit button
with st.form("search_form"):
    st.write("Adjust your search criteria and click Submit")
    st.form_submit_button("Submit")

# Filter data based on user input
filtered_data = restaurants[
    (restaurants['Type'] == search_option.split()[0]) & 
    (restaurants['Cuisine'].isin(cuisine_option)) & 
    (restaurants['Price_Range'].isin([price_option] if price_option != 'All' else restaurants['Price_Range'].unique()))
]

st.header(f"Top {search_option}")

if not filtered_data.empty:
    # Display filtered data
    st.dataframe(filtered_data[['Name', 'Cuisine', 'Rating', 'Price_Range', 'Address']])
    
    # Create a map centered around the first restaurant
    if not filtered_data.empty:
        map_center = [filtered_data['Latitude'].mean(), filtered_data['Longitude'].mean()]
        restaurant_map = folium.Map(location=map_center, zoom_start=12)
        
        for _, row in filtered_data.iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=f"{row['Name']}<br>{row['Cuisine']}<br>Rating: {row['Rating']}<br>Price Range: {row['Price_Range']}<br>{row['Address']}"
            ).add_to(restaurant_map)

        st_folium(restaurant_map, width=700, height=500)
else:
    st.write("No restaurants found with the selected criteria.")

# Display thank you message
if st.session_state.get("form_submitted", False):
    st.write("Thank you for your submission!")

