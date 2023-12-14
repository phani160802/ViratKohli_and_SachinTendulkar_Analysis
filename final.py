import importlib
import pandas as pd
import streamlit as st
import seaborn as sns
import altair as alt
import matplotlib.pyplot as plt
from centuries import show_centuries
from strikerate import show_strikerate
from boundaries import show_boundaries
from runs import show_runs
from dismissal import show_dismissal
from prediction import show_prediction
import json
import requests  
from streamlit_lottie import st_lottie  

@st.cache_data()    
def load_virat_file():
    virat_df = pd.read_csv('./Data/final_virat_stat.csv')
    virat_df['Opposition'] = virat_df['Opposition'].str.strip()
    virat_df['SR'] = pd.to_numeric(virat_df['SR'].replace('-', 0))
    virat_df['Inns'] = pd.to_numeric(virat_df['Inns'].replace('-', 0))
    virat_df.drop("Unnamed: 0",axis=1,inplace=True)
    virat_df['Match Type'] = [i.strip() for i in virat_df['Match Type']]
    return(virat_df)


@st.cache_data()    
def load_sachin_file():
    sachin_df = pd.read_csv('./Data/final_sachin_stats.csv')
    sachin_df['Opposition'] = sachin_df['Opposition'].str.strip()
    sachin_df['SR'] = pd.to_numeric(sachin_df['SR'].replace('-', 0))
    sachin_df['4s'] = pd.to_numeric(sachin_df['4s'].replace('-', 0))
    sachin_df['6s'] = pd.to_numeric(sachin_df['6s'].replace('-', 0))
    sachin_df['Match Type'] = [i.strip() for i in sachin_df['Match Type']]
    sachin_df.drop("Unnamed: 0",axis=1,inplace=True)
    return(sachin_df)


virat_df = load_virat_file()

sachin_df = load_sachin_file()

# Animation 
@st.cache_data
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://lottie.host/3c812719-2de8-4e54-829e-6123a58617dd/6gVnfh5iZH.json")

# Sidebar for navigation

# st.sidebar.title('Welcome to Cric Stats')


selected = st.sidebar.radio('Pick a criteria to analyze:', ['Home Page','Centuries','Runs','Dismissal','Prediction Game'],index=0)


# Navigation to Pages

if selected == 'Centuries':
    show_centuries(virat_df,sachin_df)

elif selected == 'Runs':
    show_runs(virat_df,sachin_df)

elif selected == 'Boundaries':
    show_boundaries(virat_df,sachin_df)

elif selected == 'Strike Rate':
    show_strikerate(virat_df,sachin_df) 

elif selected =='Dismissal':
    show_dismissal(virat_df,sachin_df)

elif selected == 'Prediction Game':
    show_prediction(virat_df,sachin_df)

elif selected == 'Home Page':
    v_totalruns = virat_df['Runs'].sum()
    v_totalmatches = virat_df['Runs'].count()
    v_totalcenturies = virat_df[virat_df['Runs']>=100].shape[0]
    v_avgstrikerate =  virat_df['SR'].mean()


    s_totalruns = sachin_df['Runs'].sum()
    s_totalmatches = sachin_df['Runs'].count()
    s_totalcenturies = sachin_df[sachin_df['Runs']>=100].shape[0]
    s_avgstrikerate = sachin_df['SR'].mean()



    data = {'Player': ['Virat Kohli', 'Sachin Tendulkar'],
            'Total Matches Played': [v_totalmatches,s_totalmatches],
            'Total Runs': [v_totalruns,s_totalruns],
            'Centuries': [v_totalcenturies, s_totalcenturies],
            'Average Strike Rate': [v_avgstrikerate,s_avgstrikerate]}
    overview_df = pd.DataFrame(data)



    # Home Page

    st.title('Welcome to Cricket Legends Face-off!')
    st.markdown(
        """
        <style>
            .stLottie { width: 100%; height: auto; margin: 0 auto;
                display: block; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display the Lottie animation
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",
        height = 300,
        width=300,
        key=None,
    )

    st.write(""" This app allows you to analyze cricket statistics of legendary players like Virat Kohli and Sachin Tendulkar.
        Pick a criteria from the sidebar to explore various aspects of their performance.
        """)
    st.subheader('Overview Statistics:')
    st.table(overview_df)


    # Top Performances Section
    st.subheader('Pick a player to see their Top performances:')
    selected_player = st.selectbox('Select player for top performances:', ['Virat Kohli', 'Sachin Tendulkar'],index=None)

    # Top Performances Section
    st.subheader('Top Performances:')

    # Functions to calculate 

    def highest_runs_per_year(df):
        df['Date'] = pd.to_datetime(df['Date'])
        df['Year'] = df['Date'].dt.year
        highest_runs_per_year = df.groupby('Year')['Runs'].max().reset_index()
        sorted_highest_runs = highest_runs_per_year.sort_values(by='Runs', ascending=False)
        highest_runs_year = sorted_highest_runs.iloc[0]['Year']
        return highest_runs_year

    def highest_runs_opposition(df):
        highest_runs_per_year = df.groupby('Opposition')['Runs'].max().reset_index()
        sorted_highest_runs = highest_runs_per_year.sort_values(by='Runs', ascending=False)
        highest_runs_opp = sorted_highest_runs.iloc[0]['Opposition']
        return highest_runs_opp


    def batting_avg(df):
        return round(df["Runs"].sum() / df['Dismissal'].count(),2)


    virat_topdata = {
            'Highest Score': max(virat_df['Runs']),
            'Highest Runs in a year': highest_runs_per_year(virat_df),
            'Highest Runs Against': highest_runs_opposition(virat_df),
            'Batting Average': batting_avg(virat_df)
            }
    virat_topdf = pd.DataFrame(virat_topdata,index=[0])

    sachin_topdata = {
            'Highest Score': max(sachin_df['Runs']),
            'Highest Runs in a year': highest_runs_per_year(sachin_df),
            'Highest Runs Against': highest_runs_opposition(sachin_df),
            'Batting Average': batting_avg(sachin_df)
            }
    sachin_topdf = pd.DataFrame(sachin_topdata,index=[0])


    if selected_player == 'Virat Kohli':
        st.dataframe(virat_topdf)

    elif selected_player == 'Sachin Tendulkar':
        st.dataframe(sachin_topdf)


