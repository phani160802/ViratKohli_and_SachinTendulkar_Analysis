import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce



def show_centuries(virat_df,sachin_df):
    # Functions 
    
    def matchtype(df,df1,x):
        return (df[df['Match Type']==x],df1[df1['Match Type']==x])
    
    
    def filter_data(df, filters_dict):
        filtered_df = df.copy()

        for column, value in filters_dict.items():
            if value != 'All':
                if column == 'Inns':
                    filtered_df = filtered_df[filtered_df[column] == int(value) if value != 'All' else filtered_df[column] == value]
                else:
                    filtered_df = filtered_df[filtered_df[column] == value]

        return filtered_df
    
    # Styling

    st.markdown("""
        <style>
        .stRadio [role=radiogroup]{
            align-items: center;
            justify-content: center;
        }
        </style>
    """,unsafe_allow_html=True)


    # Body

    st.header("Welcome to Centuries Analysis: Unveiling Cricket Legends' Milestones")
    st.markdown("In this section, we dive into the incredible journey of cricket legends Virat Kohli and Sachin Tendulkar, exploring the monumental centuries they've achieved throughout their illustrious careers.")
    st.markdown('Discover the total number of centuries made by Virat Kohli and Sachin Tendulkar, gaining insights into their extraordinary batting prowess and unparalleled accomplishments.')

    st.markdown('### Filters: ')
    st.markdown("Use the filters below to tailor your exploration:")
    st.markdown("- **Opposition:** Select specific opponents to analyze the players' performances against different teams.")
    st.markdown("- **Match Type:** Differentiate between Test matches, One Day Internationals (ODIs), and Twenty20 Internationals (T20Is) to see their adaptability across formats.")
    st.markdown("- **Innings:** Select respective innings you want to analyze.")


    # Filter Buttons

    match_filter = st.radio("Select Match Type: ",['All','Test','ODI','T20I'],index=0,horizontal=True)

    with st.sidebar:
        st.markdown("### Sidebar Filters:")
        opposition_filter = st.selectbox("Select Opposition:", ['All'] + virat_df['Opposition'].unique().tolist(), index=0)
        innings_filter = st.selectbox("Select Innings:", ['All', '1', '2'], index=0)


    filters_dict = {
        'Match Type':match_filter,
        'Opposition':opposition_filter,
        'Inns':innings_filter
    }

    virat_df1 = filter_data(virat_df,filters_dict)
    sachin_df1 = filter_data(sachin_df,filters_dict)

    v_centuries = virat_df1[virat_df1['Runs']>=100].shape[0]
    s_centuries = sachin_df1[sachin_df1['Runs']>=100].shape[0]
    
    # Bar Chart
    fig, ax = plt.subplots(figsize=(3, 2))
    sns.barplot(x=['Virat Kohli', 'Sachin Tendulkar'], y=[v_centuries, s_centuries], ax=ax, width=0.5)
    # Show the plot
    st.pyplot(fig)
    





    # if match_filter == 'All':
    #     # Filter data for centuries
    #     v_centuries = virat_df[virat_df['Runs']>=100].shape[0]
    #     s_centuries = sachin_df[sachin_df['Runs']>=100].shape[0]


    #     # Bar Chart
    #     fig, ax = plt.subplots(figsize=(3, 2))
    #     sns.barplot(x=['Virat Kohli', 'Sachin Tendulkar'], y=[v_centuries, s_centuries], ax=ax, width=0.5)

    #     # Show the plot
    #     st.pyplot(fig)
    
    # elif match_filter == 'Test':

    #     virat_df1,sachin_df1 = matchtype(virat_df,sachin_df,match_filter)
    #     v_centuries = virat_df1[virat_df1['Runs']>=100].shape[0]
    #     s_centuries = sachin_df1[sachin_df1['Runs']>=100].shape[0]
    #     # Bar Chart
    #     fig, ax = plt.subplots(figsize=(3, 2))
    #     sns.barplot(x=['Virat Kohli', 'Sachin Tendulkar'], y=[v_centuries, s_centuries], ax=ax, width=0.5)

    #     # Show the plot
    #     st.pyplot(fig)

    # elif match_filter == 'ODI':

    #     virat_df2,sachin_df2 = matchtype(virat_df,sachin_df,match_filter)
    #     v_centuries = virat_df2[virat_df2['Runs']>=100].shape[0]
    #     s_centuries = sachin_df2[sachin_df2['Runs']>=100].shape[0]
    #     # Bar Chart
    #     fig, ax = plt.subplots(figsize=(3, 2))
    #     sns.barplot(x=['Virat Kohli', 'Sachin Tendulkar'], y=[v_centuries, s_centuries], ax=ax, width=0.5)

    #     # Show the plot
    #     st.pyplot(fig)

    # elif match_filter == 'T20I':

    #     virat_df3,sachin_df3 = matchtype(virat_df,sachin_df,match_filter)
    #     v_centuries = virat_df3[virat_df3['Runs']>=100].shape[0]
    #     s_centuries = sachin_df3[sachin_df3['Runs']>=100].shape[0]
    #     # Bar Chart
    #     fig, ax = plt.subplots(figsize=(3, 2))
    #     sns.barplot(x=['Virat Kohli', 'Sachin Tendulkar'], y=[v_centuries, s_centuries], ax=ax, width=0.5)

    #     # Show the plot
    #     st.pyplot(fig)


    

