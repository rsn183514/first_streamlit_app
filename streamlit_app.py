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
st.dataframe(my_fruit_list)
