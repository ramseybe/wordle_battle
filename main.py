import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
df_ben=pd.read_csv("ben_wordle.csv")
df_juuls=pd.read_csv("juuls_wordle.csv")
df=pd.merge(df_ben, df_juuls, on=["date","word"])
st.dataframe(df)

date=st.date_input("Enter Date:")
st.write(date)


a="""<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>

<i class="fa fa-car"></i>
<i class="fa fa-car" style="font-size:48px;"></i>
<i class="fa fa-car" style="font-size:60px;color:red;"></i>

</body>
</html>"""

# st.write(HTML(a))

components.html(a,width=300, height=700)

b=st.slider(components.html(a,width=300, height=700),)


option = st.selectbox("Name?",('Ben', 'Juuls'))

st.write('You selected:', option)



if option == "Juuls":
  guess=0
  new_row = {'date': date, 'juuls_score': guess, 'word': ""}
  st.write(new_row)
  df_juuls.loc[len(df_juuls)] = new_row
elif option == "Ben":
  pass
