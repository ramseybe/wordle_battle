import streamlit as st
import pandas as pd
df=pd.read_csv("wordle.csv")
st.dataframe(df)
date=st.date_input("Enter Date:")
st.write(date)

option = st.selectbox("Name?",('Ben', 'Juuls'))

st.write('You selected:', option)



if option == "Juuls":
  pass
elif option == "Ben":
  pass
