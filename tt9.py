import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Comprehensive sample data for restaurants
restaurants = pd.DataFrame({
    'Name': [
        'Bella Italia', 'Paris Bistro', 'Downtown Grill', 'El Camino', 'Sushi Haven', 
        'Thai Street Food', 'Spice Palace', 'Roma Trattoria', 'Bistro Lumière', 'Liberty Diner', 
        'Cantina Mexicana', 'Sushi World', 'Thai House', 'Indian Essence', 'The Spice Hub', 
        'Café Delight', 'The Royal Feast'
    ],
    'Type': [
        'Famous', 'Famous', 'Nearby', 'Nearby', 'Famous', 
        'Nearby', 'Nearby', 'Famous', 'Famous', 'Nearby', 
        'Nearby', 'Famous', 'Nearby', 'Nearby', 'Famous', 
        'Famous', 'Famous'
    ],
    'Cuisine': [
        'Italian', 'French', 'American', 'Mexican', 'Japanese', 
        'Thai', 'Indian', 'Italian', 'French', 'American', 
        'Mexican', 'Japanese', 'Thai', 'Indian', 'Indian', 
        'Italian', 'French'
    ],
    'Rating': [
        4.5, 4.7, 4.3, 4.1, 4.6, 
        4.4, 4.2, 4.7, 4.6, 4.4, 
        4.3, 4.8, 4.5, 4.6, 4.8, 
        4.5, 4.7
    ],
    'Price_Range': [
        '₹500-1000', '₹500-1000', '₹800-1500', '₹1000-2000', '₹3500-5000', 
        '₹800-1600', '₹500-1200', '₹1000-2000', '₹2000-3500', '₹1000-2000', 
        '₹1000-2000', '₹1500-3000', '₹1000-2000', '₹1500-3000', '₹1500-2500', 
        '₹1200-2000', '₹2000-3500'
    ],
    'Latitude': [
        28.613940, 28.613940, 28.704060, 28.613940, 28.613940, 
        28.704060, 28.613940, 28.704060, 28.613940, 28.704060, 
        28.704060, 28.613940, 28.704060, 28.704060, 28.613940, 
        28.704060, 28.613940
    ],
    'Longitude': [
        77.209021, 77.209021, 77.102493, 77.209021, 77.209021, 
        77.102493, 77.209021, 77.102493, 77.209021, 77.102493, 
        77.102493, 77.209021, 77.102493, 77.102493, 77.209021, 
        77.102493, 77.209021
    ],
    'Address': [
        '123 Italian Street, New Delhi', '456 French Avenue, New Delhi', '789 American Road, Chandigarh', '321 Sunset Boulevard, Chandigarh', 
        '654 Tokyo Lane, New Delhi', '987 Bangkok Street, Chandigarh', '147 Curry Plaza, New Delhi', '258 Roma Place, Chandigarh', 
        '369 Lumière Avenue, Chandigarh', '741 Urban Street, New Delhi', '852 Camino Road, New Delhi', '963 Sushi Lane, Chandigarh', 
        '147 Thai Street, Chandigarh', '258 Spice Court, Chandigarh', 'Connaught Place, New Delhi', 'Sector 35, Chandigarh', 
        'Janpath, New Delhi'
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
filtered_data = restaurants[
    (restaurants['Type'] == search_option.split()[0]) & 
    (restaurants['Cuisine'].isin(cuisine_option)) & 
    (restaurants['Price_Range'].isin([price_option] if price_option != 'All' else restaurants['Price_Range'].unique()))
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
    longitude = st.number_input("Longitude", format="%.6f")
    address = st.text_input("Address")

    submit_button = st.form_submit_button(label='Add Restaurant')

    if submit_button:
        new_restaurant = pd.DataFrame({
            'Name': [name],
            'Type': [type_],
            'Cuisine': [cuisine],
            'Rating': [rating],
            'Price_Range': [price_range],
            'Latitude': [latitude],
            'Longitude': [longitude],
            'Address': [address]
        })

        # Append to the DataFrame (In real-world use, this should be stored in a database)
        restaurants = pd.concat([restaurants, new_restaurant], ignore_index=True)
        st.sidebar.success("Restaurant added successfully!")

# Personalized recommendations
st.sidebar.title("Personalized Recommendations")
recommendation
