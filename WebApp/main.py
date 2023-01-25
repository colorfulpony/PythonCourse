import streamlit as st
import pandas

data = {
    'Series_1': [1, 2, 3, 5, 7],
    'Series_2': [10, 30, 40, 50, 30],
}

df = pandas.DataFrame(data)

st.title("Our first streamlit app")
st.subheader("Introducing to our app")
st.write("""This is text
Bla bla bla""")
st.write(df)
