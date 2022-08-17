import streamlit as st
st.title('My parents new healthier dinner ')

st.header('Breakfast Menu')
st.text(' 🥣  Omega 3 & Blueberry Oatmeal')
st.text(' 🥗  Kale, Spinach & Rocket Smoothie')
st.text(' 🐔 Hard-Boiled Free-Range Egg')
st.text(' 🥑🍞 Avacado Toast')


st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]


# Display the table on the page.
st.dataframe(fruits_to_show)

st.header("Fruityvice Fruit Advice!")

# new section to display fruityvice api response
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "kiwi")



# take json version and normalize 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as table
st.dataframe(fruityvice_normalized)
