import streamlit as st
import pandas as pd
df_ben=pd.read_csv("wordle.csv")
df_juuls=pd.read_csv("wordle.csv")
df=pd.merge(df1, df2, on="date")
st.dataframe(df)
st.write(df)
date=st.date_input("Enter Date:")
st.write(date)

option = st.selectbox("Name?",('Ben', 'Juuls'))

st.write('You selected:', option)



if option == "Juuls":
  guess=0
  new_row = {'date': date, 'ben_score': guess, 'word': ""}
elif option == "Ben":
  pass
