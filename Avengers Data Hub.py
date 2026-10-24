import numpy as np
import pandas as pd
import streamlit as st


# title 
st.title("Welcome to Avengers !")

st.write('I am Iron-man ')

df=pd.DataFrame({
    'Name':['Aadil','Dhruv','Harshad','Nikul','Nauman'],
    "Age":[20,20,20,21,20]

})

st.write(df)

print(' ')
st.write("random Number Dataset")
r=pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])

st.write(r)

st.line_chart(r)
