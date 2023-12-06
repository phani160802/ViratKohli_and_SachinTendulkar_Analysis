import streamlit as st

def show_dismissal(virat_df,sachin_df):
    st.write("*** Lets Have a look at dissmissal wise analysis of Virat Kohli and Sachin Tendulkar")
    st.dataframe(virat_df)
    st.dataframe(sachin_df)
