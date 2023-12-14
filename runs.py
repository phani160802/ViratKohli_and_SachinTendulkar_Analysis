import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce
import numpy as np


def show_runs(virat_df,sachin_df):
    
    def matchtype(df,df1,x):
        return (df[df['Match Type']==x],df1[df1['Match Type']==x])
    
    def filter_data(df, filters_dict):
        filtered_df = df.copy()

        for column, values in filters_dict.items():
            if values != 'All':
                if column == 'Inns':
                    if isinstance(values, list):
                        filtered_df = filtered_df[filtered_df[column].astype(str).isin(map(str, values))]
                    else:
                        filtered_df = filtered_df[filtered_df[column] == int(values)]
                else:
                    if isinstance(values, list):
                        filter_condition = filtered_df[column].str.contains('|'.join(map(str.strip, values)), case=False)
                        filtered_df = filtered_df[filter_condition]
                    else:
                        filter_condition = filtered_df[column].str.contains(values, case=False)
                        filtered_df = filtered_df[filter_condition]

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

    st.header("Welcome to Runs and Strike Rate wise Analysis:")
    st.markdown("In this section, we dive deeper into Runs scored and the strike rate at which those runs were scored against each opposition.")
    st.markdown("This analysis will help finding who performed better against each opposition. Whom the players enjoyed playing with...")

    st.markdown('### Filters: ')
    st.markdown("Use the filters below to tailor your exploration:")
    st.markdown("- **Opposition:** Select specific opponents to analyze the players' performances against different teams.")
    st.markdown("- **Match Type:** Differentiate between Test matches, One Day Internationals (ODIs), and Twenty20 Internationals (T20Is) to see their adaptability across formats.")


    # Filter Buttons


    st.markdown("### Select Match Type: ")
    match_filter = st.radio(" ",['All','Test','ODI','T20I'],index=0,horizontal=True)

    with st.sidebar:
        st.markdown("### Sidebar Filters:")
        opp_list = [i.strip() for i in virat_df['Opposition'].unique()]
        opp_list.remove('Pakistan')
        opp_list.remove('Ireland')
        opposition_filter = st.sidebar.multiselect("Select Opposition:", opp_list)

     

    if not opposition_filter:
        st.markdown("### Please Select Opposition to Continue !")

    else:
            filters_dict = {
            'Match Type':match_filter,
            'Opposition':opposition_filter}

            st.markdown("### Filters Selected: ")
            st.markdown(f"Match Type: {match_filter}")
            st.markdown(f"Opposition: {opposition_filter}")

            if match_filter == 'T20I':
                st.markdown("Unfortunately, Sachin did not participate in T20 Internationals throughout his career.")
                virat_df1 = filter_data(virat_df, filters_dict)
                opp_filter_list = list(opposition_filter)
                max_runs_scored = {}
                avg_strike_rate={}

                # Populate max_runs_scored dictionary
                for i in opp_filter_list:
                    maxlist = [
                        max(virat_df1[virat_df1["Opposition"] == i]['Runs'])
                    ]
                    avglist = [virat_df1[virat_df1['Opposition'] == i]['SR'].mean()]
                    max_runs_scored[i] = maxlist
                    avg_strike_rate[i] = avglist

                # Convert max_runs_scored to a final DataFrame
                final_df = pd.DataFrame({
                    'Player Name': ['Virat Kohli'] * len(opp_filter_list),
                    'Opposition': opp_filter_list,
                    'Max Runs Scored': [score for scores in max_runs_scored.values() for score in scores],
                    'Average Strike Rate': [float(sr) if isinstance(sr, (float, np.float64)) else np.nan for srs in avg_strike_rate.values() for sr in srs]
                })

                st.dataframe(final_df)



            else:
                virat_df1 = filter_data(virat_df,filters_dict)
                sachin_df1 = filter_data(sachin_df,filters_dict)

                
                opp_filter_list = list(opposition_filter)
                max_runs_scored = {}
                avg_strike_rate={}

                # Populate max_runs_scored dictionary
                for i in opp_filter_list:
                    maxlist = [
                        max(virat_df1[virat_df1["Opposition"] == i]['Runs']),
                        max(sachin_df1[sachin_df1["Opposition"] == i]['Runs'])
                    ]
                    avglist = [virat_df1[virat_df1['Opposition'] == i]['SR'].mean(), sachin_df1[sachin_df1['Opposition'] == i]['SR'].mean()]
                    max_runs_scored[i] = maxlist
                    avg_strike_rate[i]=avglist

                # Convert max_runs_scored to a final DataFrame
                final_df = pd.DataFrame({
                        'Player Name': ['Virat Kohli', 'Sachin Tendulkar'] * len(opp_filter_list),
                        'Opposition': [opp_filter_list[i // 2] for i in range(len(opp_filter_list) * 2)],
                        'Max Runs Scored': [max_runs_scored[opposition][player_idx] for opposition in opp_filter_list for player_idx in range(2)],
                        'Average Strike Rate': [float(avg_strike_rate[opposition][player_idx]) if isinstance(avg_strike_rate[opposition][player_idx], (float, np.float64)) else np.nan for opposition in opp_filter_list for player_idx in range(2)]
                    })


                st.dataframe(final_df)

                st.markdown("### Visual Delight.. ")
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 12))  # Creating a subplot with two columns

                # Plot for Max Runs Scored Analysis
                sns.barplot(x='Player Name', y='Max Runs Scored', hue='Opposition', data=final_df, palette='pastel', ax=ax1)
                ax1.set_title("Max Runs Scored Analysis", fontsize=14)
                ax1.set_ylabel("Max Runs Scored", fontsize=12)
                ax1.set_xlabel("Players", fontsize=12)
                ax1.legend(title='Opposition', title_fontsize='12',fontsize='12',bbox_to_anchor=(1.05, 1), loc='center')
                for p in ax1.patches:
                                ax1.annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points',fontsize=13)

                # Plot for Average Strike Rate Analysis
                sns.barplot(x='Player Name', y='Average Strike Rate', hue='Opposition', data=final_df, palette='pastel', ax=ax2)
                ax2.set_title("Average Strike Rate Analysis", fontsize=14)
                ax2.set_ylabel("Average Strike Rate", fontsize=12)
                ax2.set_xlabel("Players", fontsize=12)
                ax2.get_legend().set_visible(False)

                for p in ax2.patches:
                            ax2.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points',fontsize=13)


                sns.despine()

                # Show the plot
                st.pyplot(fig)

                st.markdown("#### Confused about what plots actually convey!!!")
                st.markdown("Select Opposition filters as England, Zimbabwe, Austrailia, and South Africa.")
                st.markdown("From the Average Strike Rate Plot it is quite evident that Virat Kohli has scored runs with a much higher strike rate than sachin tendulkar.")
                st.markdown("Virat Kohli outshines Sachin Tendulkar with a striking display of aggression and adaptability. Virat's ability to score at a blistering pace sets him apart, making him the go-to player, especially in the fast-paced realms of ODIs and T20Is, where rapid scoring reigns supreme.")





    

