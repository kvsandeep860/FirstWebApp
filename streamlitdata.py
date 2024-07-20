import streamlit as st
import numpy as np
import pandas as pd
st.title("BMI calculator")
with st.form("BMI calculator"):
    col1,col2,col3=st.columns([3,2,1])
with col1:
    weight=st.number_input("Enter weight in kg")
with col2:
    height=st.number_input("Enter height on meter")
with col3:
    submit= st.form_submit_button("calculate")
if submit:
    bmi=weight/(height)**2
    bmi=round(bmi,2)
    st.text("Your Body Mass Index is:")
    st.text(bmi)
    if bmi<=18.5:
        st.error("Under Weight")
    elif 18.6<=bmi<=24.5:
        st.success("normal")
    else:
        st.error("over weight")