# This creates the page for displaying data visualizations.

import streamlit as st
import json
import altair as alt

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Data Visualizations 📈")


# PART 1: GRAPHS FROM data.json
# --- YOUR CODE GOES HERE ---

with open("data.json", "r") as file:
    data = json.load(file)

waterfalls = data["waterfalls"]


# STATIC VISUALIZATION

st.subheader("Famous Waterfall Heights")

bar_chart = alt.Chart(
    alt.Data(values=waterfalls)
).mark_bar().encode(
    x=alt.X("name:N", title="Waterfall"),
    y=alt.Y("height:Q", title="Height (meters)")
).properties(
    title="Heights of Famous Waterfalls"
)

st.altair_chart(bar_chart, use_container_width=True)


# DYNAMIC VISUALIZATION

st.subheader("Waterfall Locations")

continents = [
    "All",
    "North America",
    "South America",
    "Europe",
    "Africa",
    "Asia",
    "Oceania"
]

if "continent" not in st.session_state:
    st.session_state.continent = "All"

st.selectbox(
    "Choose a continent:",
    continents,
    key="continent"
)

filtered_waterfalls=[]

for waterfall in waterfalls:
    if st.session_state.continent == "All":
        filtered_waterfalls.append(waterfall)
    elif waterfall["continent"] == st.session_state.continent:
        filtered_waterfalls.append(waterfall)

st.map(filtered_waterfalls, latitude="latitude", longitude="longitude")
#extra credit w/ median and man

heights = []

for waterfall in filtered_waterfalls:
    heights.append(waterfall["height"])

heights.sort()
mean = sum(heights) / len(heights)
middle = len(heights) // 2
if len(heights) % 2 == 1:
    median = heights[middle]
else:
    median = (heights[middle - 1] + heights[middle]) / 2

#store the previous statistics
if "previous_mean" not in st.session_state:
    st.session_state.previous_mean = mean
    st.session_state.previous_median = median
    st.session_state.previous_continent = st.session_state.continent

#calculate changes when the continent changes
if st.session_state.previous_continent != st.session_state.continent:
    st.session_state.mean_change = mean - st.session_state.previous_mean
    st.session_state.median_change = median - st.session_state.previous_median

    st.session_state.previous_mean = mean
    st.session_state.previous_median = median
    st.session_state.previous_continent = st.session_state.continent

#display the statistics
st.metric(
    "Mean Waterfall Height",
    str(round(mean, 2)) + " m",
    delta=round(st.session_state.get("mean_change", 0), 2)
)

st.metric(
    "Median Waterfall Height",
    str(round(median, 2)) + " m",
    delta=round(st.session_state.get("median_change", 0), 2)
)



###################
# PART 2: GRAPHS FROM data.csv
# --- YOUR CODE GOES HERE ---
# Read survey responses from CSV
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    responses = list(reader)

#count votes for each waterfall
votes = {}

for response in responses:
    waterfall = response["Category"]

    if waterfall in votes:
        votes[waterfall] += 1
    else:
        votes[waterfall] = 1

#c onvert vote counts into data for the chart
vote_data = []

for waterfall in votes:
    vote_data.append({
        "Waterfall": waterfall,
        "Votes": votes[waterfall]
    })

#static visualization
st.subheader("Most Popular Waterfalls")

if len(vote_data) > 0:
    chart = alt.Chart(
        alt.Data(values=vote_data)
    ).mark_bar().encode(
        x=alt.X("Waterfall:N", title="Waterfall"),
        y=alt.Y("Votes:Q", title="Number of Votes")
    ).properties(
        title="Waterfalls People Want to Visit"
    )

    st.altair_chart(chart, use_container_width=True)
else:
    st.write("No survey responses yet.")



#dynamic visualization
st.subheader("Waterfalls Visited by Survey Respondents")

if "minimum_visits" not in st.session_state:
    st.session_state.minimum_visits = 0

st.slider(
    "Minimum number of waterfalls visited:",
    min_value=0,
    max_value=20,
    key="minimum_visits"
)

#filter survey responses
visit_data = []

for response in responses:
    if response["Value"].isdigit():
        visits = int(response["Value"])

        if visits >= st.session_state.minimum_visits:
            visit_data.append({
                "Waterfall": response["Category"],
                "Visits": visits
            })

#display the dynamic chart
if len(visit_data) > 0:
    visit_chart = alt.Chart(
        alt.Data(values=visit_data)
    ).mark_circle(size=100).encode(
        x=alt.X("Waterfall:N", title="Preferred Waterfall"),
        y=alt.Y("Visits:Q", title="Number of Waterfalls Visited"),
        tooltip=["Waterfall:N", "Visits:Q"]
    ).properties(
        title="Survey Responses by Number of Waterfalls Visited"
    )

    st.altair_chart(visit_chart, use_container_width=True)
else:
    st.write("No responses match this filter.")