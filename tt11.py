import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Sample data for restaurants
restaurants = pd.DataFrame({
    'Name': ['Bella Italia', 'Paris Bistro', 'Downtown Grill', 'Sunset Cantina', 'Tokyo Delights', 'Bangkok Café', 'Curry Corner', 
             'Roma Trattoria', 'Bistro Lumière', 'The Urban Café', 'El Camino', 'Sushi Haven', 'Thai Street Food', 'Spice Palace',
             'Liberty Diner', 'Aztec Grill', 'Kyoto Kitchen', 'Siam Square', 'Royal Indian Restaurant',
             'La Dolce Vita', 'Château de Cuisine', 'The Great American', 'Cantina Mexicana', 'Zen Sushi Bar', 'Thai Orchid', 'Spicy Curry House',
             'Trattoria da Vinci', 'Café du Palais', 'The Golden Grill', 'El Toro Bravo', 'Mount Fuji Sushi', 'Thai Essence', 'Tandoori Treasure',
             'Piazza Italia', 'Brasserie Belle', 'The Majestic Diner', 'La Fiesta', 'Shogun Sushi House', 'Thai Fusion', 'Maharaja\'s Feast'],
    'Type': ['Famous', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 
             'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby',
             'Famous', 'Famous', 'Famous', 'Famous', 'Famous',
             'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby',
             'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby',
             'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby', 'Nearby'],
    'Cuisine': ['Italian', 'French', 'American', 'Mexican', 'Japanese', 'Thai', 'Indian',
                'Italian', 'French', 'American', 'Mexican', 'Japanese', 'Thai', 'Indian',
                'Italian', 'French', 'American', 'Mexican', 'Japanese', 'Thai', 'Indian',
                'Italian', 'French', 'American', 'Mexican', 'Japanese', 'Thai', 'Indian',
                'Italian', 'French', 'American', 'Mexican', 'Japanese', 'Thai', 'Indian'],
    'Rating': [4.5, 4.7, 4.3, 4.1, 4.8, 4.4, 4.9, 
               4.6, 4.8, 4.2, 4.3, 4.9, 4.4, 4.6,
               4.7, 4.9, 4.5, 4.3, 4.8,
               4.6, 4.8, 4.4, 4.5, 4.9, 4.3, 4.6,
               4.7, 4.9, 4.3, 4.5, 4.9, 4.3, 4.7,
               4.8, 4.6, 4.4, 4.5, 4.9, 4.6, 4.8],
    'Price_Range': ['₹500-1000', '₹500-1000', '₹500-1000', '₹500-1000', '₹500-1000', '₹500-1000', '₹500-1000',
                    '₹800-1500', '₹800-1500', '₹800-1500', '₹800-1500', '₹800-1500', '₹800-1500', '₹800-1500',
                    '₹1000-2000', '₹1000-2000', '₹1000-2000', '₹1000-2000', '₹1000-2000', '₹1000-2000', '₹1000-2000',
                    '₹1200-2200', '₹1200-2200', '₹1200-2200', '₹1200-2200', '₹1200-2200', '₹1200-2200', '₹1200-2200',
                    '₹2000-3000', '₹2000-3000', '₹2000-3000', '₹2000-3000', '₹2000-3000', '₹2000-3000', '₹2000-3000',
                    '₹3500-5000', '₹3500-5000', '₹3500-5000', '₹3500-5000', '₹3500-5000', '₹3500-5000', '₹3500-5000'],
    'Latitude': [28.613940, 28.704060, 28.613940, 28.704060, 28.613940, 28.704060, 28.613940, 
                 28.704060, 28.613940, 28.704060, 28.613940, 28.704060, 28.613940, 28.704060,
                 28.613940, 28.704060, 28.613940, 28.704060, 28.613940,
                 28.704060, 28.613940, 28.704060, 28.613940, 28.704060, 28.613940, 28.704060,
                 28.613940, 28.704060, 28.613940, 28.704060, 28.613940, 28.704060, 28.613940,
                 28.704060, 28.613940, 28.704060, 28.613940, 28.704060, 28.613940, 28.704060],
    'Longitude': [77.209021, 77.102493, 77.209021, 77.102493, 77.209021, 77.102493, 77.209021,
                  77.102493, 77.209021, 77.102493, 77.209021, 77.102493, 77.209021, 77.102493,
                  77.209021, 77.102493, 77.209021, 77.102493, 77.209021,
                  77.102493, 77.209021, 77.102493, 77.209021, 77.102493, 77.209021, 77.102493,
                  77.209021, 77.102493, 77.209021, 77.102493, 77.209021, 77.102493, 77.209021,
                  77.102493, 77.209021, 77.102493, 77.209021, 77.102493, 77.209021, 77.102493],
    'Address': ['Connaught Place, New Delhi', 'Sector 22, Chandigarh', 'South Delhi, New Delhi', 'Sector 17, Chandigarh', 'Sector 35, Chandigarh', 'South Delhi, New Delhi', 'Connaught Place, New Delhi',
                'Janpath, New Delhi', 'Central Delhi', 'Old Delhi', 'Central Delhi', 'Sector 17, Chandigarh', 'Central Delhi', 'Sector 35, Chandigarh',
                'Connaught Place, New Delhi', 'Sector 22, Chandigarh', 'South Delhi, New Delhi', 'Sector 17, Chandigarh', 'Connaught Place, New Delhi',
                'Janpath, New Delhi', 'Central Delhi', 'Old Delhi', 'Central Delhi', 'Sector 17, Chandigarh', 'Central Delhi', 'Sector 35, Chandigarh',
                'Connaught Place, New Delhi', 'Sector 22, Chandigarh', 'South Delhi, New Delhi', 'Sector 17, Chandigarh', 'Connaught Place, New Delhi',
                'Janpath, New Delhi', 'Central Delhi', 'Old Delhi', 'Central Delhi', 'Sector 17, Chandigarh', 'Central Delhi', 'Sector 35, Chandigarh']
})

# Main app content
st.title("Taste Tracker")

# Sidebar for user input
st.sidebar.title("Restaurant Finder")
search_option = st.sidebar.selectbox("Search for:", ["Famous Places", "Nearby Places"])
cuisine_option = st.sidebar.multiselect("Cuisine Type", restaurants['Cuisine'].unique())
price_option = st.sidebar.selectbox("Price Range", ['All'] + sorted(restaurants['Price_Range'].unique()))

# Filter data based on user input
filtered_data = restaurants[
    (restaurants['Type'] == search_option.split()[0]) & 
    (restaurants['Cuisine'].isin(cuisine_option)) & 
    (restaurants['Price_Range'].isin([price_option] if price_option != 'All' else restaurants['Price_Range'].unique()))
]

# Display filtered data for verification
st.write("Filtered Data:")
st.write(filtered_data)

st.header(f"Top {search_option}")

if not filtered_data.empty:
    # Display filtered data
    for _, row in filtered_data.iterrows():
        st.write(f"**{row['Name']}** - {row['Cuisine']}, {row['Price_Range']}")
        st.write(f"Rating: {row['Rating']}")
        st.write(f"Address: {row['Address']}")
        st.write("---")

    # Display map with restaurant locations
    if not filtered_data[['Latitude', 'Longitude']].isnull().any().any():
        m = folium.Map(location=[filtered_data['Latitude'].mean(), filtered_data['Longitude'].mean()], zoom_start=12)
        for _, row in filtered_data.iterrows():
            folium.Marker([row['Latitude'], row['Longitude']], popup=row['Name']).add_to(m)
        st_folium(m, width=700, height=500)
    else:
        st.write("No valid locations available to display on the map.")
else:
    st.write("No restaurants found matching your criteria.")

# Add a submit button within a form
with st.form("search_form"):
    st.form_submit_button("Submit")
