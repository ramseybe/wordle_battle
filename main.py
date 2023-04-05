import streamlit as st
import pandas as pd
df=pd.read_csv("wordle.csv")
st.dataframe(df)
date=st.date_input("Enter Date:")
st.write(date)
