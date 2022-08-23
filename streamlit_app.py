import streamlit as st
import pandas
import requests
import snowflake.connector
from  urllib.error import URLError
st.title('My parents new healthier dinner ')

st.header('Breakfast Menu')
st.text(' 🥣  Omega 3 & Blueberry Oatmeal')
st.text(' 🥗  Kale, Spinach & Rocket Smoothie')
st.text(' 🐔 Hard-Boiled Free-Range Egg')
st.text(' 🥑🍞 Avacado Toast')


st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
# Display the table on the page.
st.dataframe(fruits_to_show)

# new section to display fruityvice api response
st.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = st.text_input('What fruit would you like information about?')
    if not fruit_choice:
        st.error("Please select a fruit to get information. ")
    else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    # fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # st.dataframe(fruityvice_normalized)

 # except URLError as e:
  #  st.error()
  

#import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
st.header("The Fruit load list contains")
st.dataframe(my_data_rows)


add_my_fruit = st.text_input('What fruit would you like to add ?','jackfruit')
st.text('Thanks for adding jackfruit')
st.write('Thanks for adding ', add_my_fruit)

# this will not work
my_cur.execute("Insert into fruit_load_list values ('from steamlist')")
