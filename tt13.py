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
}

# Create DataFrame
restaurants = pd.DataFrame(data)

# Streamlit app
st.title("Taste Tracker")

# Form for filtering data
with st.form(key='filter_form'):
    st.header("Filter Options")
    search_option = st.selectbox("Select Type:", ['Famous', 'Nearby'])
    cuisine_option = st.multiselect("Select Cuisine(s):", options=restaurants['Cuisine'].unique(), default=restaurants['Cuisine'].unique())
    price_option = st.selectbox("Select Price Range:", options=['All'] + sorted(restaurants['Price_Range'].unique()))

    submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.session_state.form_submitted = True
    else:
        st.session_state.form_submitted = False

# Filter data based on user input
filtered_data = restaurants[
    (restaurants['Type'] == search_option) & 
    (restaurants['Cuisine'].isin(cuisine_option)) & 
    (restaurants['Price_Range'].isin([price_option] if price_option != 'All' else restaurants['Price_Range'].unique()))
]

# Display results if the form has been submitted
if st.session_state.get('form_submitted', False):
    st.header(f"Top {search_option} Places")

    if not filtered_data.empty:
        for _, row in filtered_data.iterrows():
            st.write(f"**{row['Name']}** - {row['Cuisine']}, {row['Price_Range']}")
            st.write(f"Rating: {row['Rating']}")
            st.write(f"Address: {row['Address']}")
            st.write("---")

        # Display map with restaurant locations
        st.subheader("Location Map")
        map_center = [filtered_data['Latitude'].mean(), filtered_data['Longitude'].mean()]
        m = folium.Map(location=map_center, zoom_start=12)

        for _, row in filtered_data.iterrows():
            folium.Marker([row['Latitude'], row['Longitude']], popup=row['Name']).add_to(m)

        st_folium(m, width=700, height=500)

        st.success("Thank you for using the Taste Tracker app!")
    else:
        st.warning("No restaurants found based on your criteria.")
