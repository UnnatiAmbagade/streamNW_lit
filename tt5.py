import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Expanded sample data for restaurants with random names
restaurants = pd.DataFrame({
    'Name': ['Bella Italia', 'Le Gourmet', 'The Urban Café', 'Sunset Diner', 'Green Leaf Bistro', 'Sushi Central', 'Thai Garden', 'Downtown Grill', 'Spicy Curry House', 'Royal Indian Restaurant'],
    'Type': ['Famous', 'Famous', 'Nearby', 'Nearby', 'Nearby', 'Famous', 'Nearby', 'Nearby', 'Nearby', 'Famous'],
    'Cuisine': ['Italian', 'French', 'American', 'Mexican', 'Italian', 'Japanese', 'Thai', 'American', 'Indian', 'Indian'],
    'Rating': [4.5, 4.7, 4.3, 4.1, 4.6, 4.8, 4.4, 4.2, 4.9, 4.8],
    'Price_Range': ['₹200-₹400', '₹300-₹500', '₹150-₹250', '₹100-₹200', '₹200-₹400', '₹500-₹700', '₹150-₹300', '₹100-₹250', '₹250-₹450', '₹300-₹600'],
    'Latitude': [28.613940, 28.613940, 28.704060, 28.613940, 28.704060, 28.613940, 28.704060, 28.613940, 28.613940, 28.704060],
    'Longitude': [77.209021, 77.209021, 77.102493, 77.209021, 77.102493, 77.209021, 77.102493, 77.209021, 77.209021, 77.102493],
    'Address': ['Connaught Place, New Delhi, Delhi 110001', 'Janpath, New Delhi, Delhi 110001', 'Sector 17, Chandigarh, Punjab 160017', 'South Delhi, New Delhi, Delhi 110020', 'Sector 22, Chandigarh, Punjab 160022', 'Connaught Place, New Delhi, Delhi 110001', 'Sector 35, Chandigarh, Punjab 160036', 'Central Delhi, New Delhi, Delhi 110001', 'Old Delhi, Delhi 110006', 'South Delhi, New Delhi, Delhi 110030'],
    'Dietary': ['None', 'Vegetarian', 'Non-Vegetarian', 'Vegan', 'Vegetarian', 'Non-Vegetarian', 'Vegan', 'Non-Vegetarian', 'Vegetarian', 'Non-Vegetarian']
})

# Simulate user login
def user_login():
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if username and password:
            st.session_state.logged_in = True
            st.sidebar.success("Logged in successfully")
            st.experimental_rerun()  # Reload the app after login
        else:
            st.sidebar.error("Please enter username and password")

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    user_login()
else:
    # Sidebar for user input
    st.sidebar.title("Taste Tracker")
    search_option = st.sidebar.selectbox("Search for:", ["Famous Places", "Nearby Places"])
    cuisine_option = st.sidebar.multiselect("Cuisine Type", restaurants['Cuisine'].unique())
    price_option = st.sidebar.selectbox("Price Range", ['All'] + sorted(restaurants['Price_Range'].unique()))
    dietary_option = st.sidebar.multiselect("Dietary Preferences", restaurants['Dietary'].unique())

    # Filter data based on user input
    filtered_data = restaurants[
        (restaurants['Type'] == search_option.split()[0]) & 
        (restaurants['Cuisine'].isin(cuisine_option)) & 
        (restaurants['Price_Range'].isin([price_option] if price_option != 'All' else restaurants['Price_Range'].unique())) &
        (restaurants['Dietary'].isin(dietary_option) if dietary_option else restaurants['Dietary'].isin(restaurants['Dietary']))
    ]

    # Customize title and header
    st.title("Taste Tracker")
    st.header("Find the Best Places to Eat")

    # Display recommendations
    st.subheader(f"Top {search_option}")
    if filtered_data.empty:
        st.write("No restaurants match your criteria. Please try different options.")
    else:
        for i, row in filtered_data.iterrows():
            st.subheader(f"{row['Name']} ({row['Cuisine']})")
            st.write(f"Rating: {row['Rating']} | Price Range: {row['Price_Range']}")
            st.write(f"Address: {row['Address']}")
            st.text_input(f"Review for {row['Name']}:", key=f"review_{i}")
            st.slider(f"Rate {row['Name']} (1 to 5):", 1, 5, 3, key=f"rating_{i}")

    # Map visualization centered on India
    st.header("Location of Restaurants")
    if not filtered_data.empty:
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

    # Personalized recommendations
    st.sidebar.title("Personalized Recommendations")
    recommendation = st.sidebar.text_area("Share your recommendations for restaurants:")
    if recommendation:
        st.sidebar.write(f"Thank you for your recommendation: {recommendation}")

    # Manager/Owner Submission Form
    st.sidebar.title("Add Your Restaurant")
    with st.sidebar.form(key='add_restaurant_form'):
        new_name = st.text_input("Restaurant Name")
        new_cuisine = st.text_input("Cuisine Type")
        new_address = st.text_input("Address")
        new_latitude = st.number_input("Latitude", format="%.6f")
        new_longitude = st.number_input("Longitude", format="%.6f")
        new_rating = st.slider("Rating (1 to 5)", 1, 5, 3)
        new_price_range = st.selectbox("Price Range", options=['₹100-₹200', '₹200-₹400', '₹400-₹600', '₹600-₹800', '₹800-₹1000'])
        new_dietary = st.selectbox("Dietary Preference", options=['None', 'Vegetarian', 'Non-Vegetarian', 'Vegan'])
        
        submit_button = st.form_submit_button(label='Submit')
        
        if submit_button:
            st.write("Thank you for adding your restaurant! We will review it soon.")
            # Implement code to save data to your database or file

    # Admin Dashboard Placeholder
    st.sidebar.title("Admin Dashboard")
    if st.session_state.logged_in:
        st.sidebar.write("Admin options will be available here.")

    # Placeholder for future features
    st.sidebar.title("Upcoming Features")
    st.sidebar.write("1. User Reviews & Ratings")
    st.sidebar.write("2. Personalized Recommendations")
    st.sidebar.write("3. Booking & Reservations")
