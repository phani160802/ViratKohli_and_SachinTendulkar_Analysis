import pandas as pd
import streamlit as st
import seaborn as sns


@st.cache_data()    
def load_virat_file():
    virat_df = pd.read_csv('final_virat_stat.csv')
    return(virat_df)


@st.cache_data()    
def load_sachin_file():
    sachin_df = pd.read_csv('final_sachin_stats.csv')
    return(sachin_df)

st.write("**Virat Dataset**")
virat_df = load_virat_file()
sachin_df = load_sachin_file()


st.dataframe(virat_df)
st.dataframe(sachin_df)


