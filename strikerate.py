import streamlit as st

def show_strikerate(virat_df,sachin_df):
    
    st.markdown("*** Let's Have a look at Strike Rate Wise Analysis between Virat Kohli and Sachin Tendulkar***")
    st.dataframe(virat_df)
    st.dataframe(sachin_df)