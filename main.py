import streamlit as st
import pandas as pd
df_ben=pd.read_csv("ben_wordle.csv")
df_juuls=pd.read_csv("juuls_wordle.csv")
df=pd.merge(df_ben, df_juuls, on=["date","word"])
st.dataframe(df)

date=st.date_input("Enter Date:")
st.write(date)

option = st.selectbox("Name?",('Ben', 'Juuls'))

st.write('You selected:', option)



if option == "Juuls":
  guess=0
  new_row = {'date': date, 'juuls_score': guess, 'word': ""}
  st.write(new_row)
  df_juuls.loc[len(df_juuls)] = new_row
elif option == "Ben":
  pass
