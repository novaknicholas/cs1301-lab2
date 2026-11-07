# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Homepage",  # The title that appears in the browser tab
    page_icon="🏠",         # An emoji that appears as the icon in the browser tab
)

# WELCOME PAGE TITLE
st.title("Famous Waterfalls Around the World")
st.header("Famous Waterfalls Around the World 🌎")

st.write(
    "Welcome! This app explores famous waterfalls from around "
    "the world through interactive maps, charts, and survey results."
)

st.subheader("Explore the App")

st.write(
    "📍 Visuals: Compare waterfall heights, explore their locations "
    "on a world map, and see survey results."
)

st.write(
    "📝 Survey: Vote for the waterfall you'd most like to visit "
    "and share how many waterfalls you've visited."
)

# INTRODUCTORY TEXT
st.write("""
This application is designed to collect and visualize data.
You can navigate to the different pages using the sidebar on the left.

### How to use this app:
- **Survey Page**: Go here to input new data into our CSV file.
- **Visuals Page**: Go here to see the data visualized in different graphs.

This project is part of CS 1301's Lab 2.
""")

# OPTIONAL: ADD AN IMAGE
# 1. Navigate to the 'images' folder in your Lab02 directory.
# 2. Place your image file (e.g., 'welcome_image.png') inside that folder.
# 3. Uncomment the line below and change the filename to match yours.
#
# st.image("images/welcome_image.png")
st.image("images/waterfall.jpg", width=300, caption="Sissu Falls")