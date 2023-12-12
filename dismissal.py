import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def show_dismissal(virat_df,sachin_df):
    st.title("Dismissal Analysis")

    st.markdown("Here, you can look at the type of dismissal statistics of each player in respective Match Format")

    opposition_filter = st.selectbox("Select Opposition:", ['All'] + virat_df['Opposition'].unique().tolist(), index=0)

    tab1, tab2, tab3,tab4 = st.tabs(["All", "Test", "ODI","T20I"])
    with tab1:

        if opposition_filter == 'All':

            st.title(f'Dismissal Analysis with respect to {opposition_filter} Opponents')
            sub_virat_df = virat_df[['Match Type','Opposition','Dismissal']]
            sub_sachin_df = sachin_df[['Match Type','Opposition','Dismissal']]
            virat_dismissal_counts = pd.crosstab(sub_virat_df['Dismissal'], columns='count')
            sachin_dismissal_counts = pd.crosstab(sub_sachin_df['Dismissal'], columns='count')

            st.markdown('#### Virat Kohli Dismissal Types Heatmap')
            fig_virat, ax_virat = plt.subplots(figsize=(10, 4))
            sns.heatmap(virat_dismissal_counts, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'}, ax=ax_virat)
            plt.xlabel('Count')
            plt.ylabel('Dismissal Type')
            st.pyplot(fig_virat)

            # Display the Sachin Tendulkar dismissal types heatmap
            st.markdown('#### Sachin Tendulkar Dismissal Types Heatmap')
            fig_sachin, ax_sachin = plt.subplots(figsize=(10, 4))
            sns.heatmap(sachin_dismissal_counts, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'}, ax=ax_sachin)
            plt.xlabel('Count')
            plt.ylabel('Dismissal Type')
            st.pyplot(fig_sachin)
        else:
            st.title(f'Dismissal Analysis with respect to {opposition_filter}')
            sub_virat_df = virat_df[virat_df['Opposition']==opposition_filter]
            sub_sachin_df = sachin_df[sachin_df['Opposition']==opposition_filter]
            virat_dismissal_counts = pd.crosstab(sub_virat_df['Dismissal'], columns='count')
            sachin_dismissal_counts = pd.crosstab(sub_sachin_df['Dismissal'], columns='count')

            st.markdown('#### Virat Kohli Dismissal Types Heatmap')
            fig_virat, ax_virat = plt.subplots(figsize=(10, 4))
            sns.heatmap(virat_dismissal_counts, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'}, ax=ax_virat)
            plt.xlabel('Count')
            plt.ylabel('Dismissal Type')
            st.pyplot(fig_virat)

            # Display the Sachin Tendulkar dismissal types heatmap
            st.markdown('#### Sachin Tendulkar Dismissal Types Heatmap')
            fig_sachin, ax_sachin = plt.subplots(figsize=(10, 4))
            sns.heatmap(sachin_dismissal_counts, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'}, ax=ax_sachin)
            plt.xlabel('Count')
            plt.ylabel('Dismissal Type')
            st.pyplot(fig_sachin)
        

        with tab2:
                virat_test_df = virat_df[virat_df['Match Type']=='Test']
                sachin_test_df=sachin_df[sachin_df['Match Type']=='Test']

                if opposition_filter == 'All':

                    st.title(f'Dismissal Analysis with respect to {opposition_filter} Opponents')
                    sub_virat_df = virat_test_df[['Match Type','Opposition','Dismissal']]
                    sub_sachin_df = sachin_test_df[['Match Type','Opposition','Dismissal']]
                    virat_dismissal_counts = pd.crosstab(sub_virat_df['Dismissal'], columns='count')
                    sachin_dismissal_counts = pd.crosstab(sub_sachin_df['Dismissal'], columns='count')

                    st.markdown('#### Virat Kohli Dismissal Types Heatmap')
                    fig_virat, ax_virat = plt.subplots(figsize=(10, 4))
                    sns.heatmap(virat_dismissal_counts, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'}, ax=ax_virat)
                    plt.xlabel('Count')
                    plt.ylabel('Dismissal Type')
                    st.pyplot(fig_virat)

                    # Display the Sachin Tendulkar dismissal types heatmap
                    st.markdown('#### Sachin Tendulkar Dismissal Types Heatmap')
                    fig_sachin, ax_sachin = plt.subplots(figsize=(10, 4))
                    sns.heatmap(sachin_dismissal_counts, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'}, ax=ax_sachin)
                    plt.xlabel('Count')
                    plt.ylabel('Dismissal Type')
                    st.pyplot(fig_sachin)
                else:
                    st.title(f'Dismissal Analysis with respect to {opposition_filter}')
                    sub_virat_df = virat_test_df[virat_df['Opposition']==opposition_filter]
                    sub_sachin_df = sachin_test_df[sachin_df['Opposition']==opposition_filter]
                    virat_dismissal_counts = pd.crosstab(sub_virat_df['Dismissal'], columns='count')
                    sachin_dismissal_counts = pd.crosstab(sub_sachin_df['Dismissal'], columns='count')

                    st.markdown('#### Virat Kohli Dismissal Types Heatmap')
                    fig_virat, ax_virat = plt.subplots(figsize=(10, 4))
                    sns.heatmap(virat_dismissal_counts, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'}, ax=ax_virat)
                    plt.xlabel('Count')
                    plt.ylabel('Dismissal Type')
                    st.pyplot(fig_virat)

                    # Display the Sachin Tendulkar dismissal types heatmap
                    st.markdown('#### Sachin Tendulkar Dismissal Types Heatmap')
                    fig_sachin, ax_sachin = plt.subplots(figsize=(10, 4))
                    sns.heatmap(sachin_dismissal_counts, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'}, ax=ax_sachin)
                    plt.xlabel('Count')
                    plt.ylabel('Dismissal Type')
                    st.pyplot(fig_sachin)


        with tab3:
                
                virat_ODI_df = virat_df[virat_df['Match Type']=='ODI']
                sachin_ODI_df=sachin_df[sachin_df['Match Type']=='ODI']

                if opposition_filter == 'All':

                    st.title(f'Dismissal Analysis with respect to {opposition_filter} Opponents')
                    sub_virat_df = virat_ODI_df[['Match Type','Opposition','Dismissal']]
                    sub_sachin_df = sachin_ODI_df[['Match Type','Opposition','Dismissal']]
                    virat_dismissal_counts = pd.crosstab(sub_virat_df['Dismissal'], columns='count')
                    sachin_dismissal_counts = pd.crosstab(sub_sachin_df['Dismissal'], columns='count')

                    st.markdown('#### Virat Kohli Dismissal Types Heatmap')
                    fig_virat, ax_virat = plt.subplots(figsize=(10, 4))
                    sns.heatmap(virat_dismissal_counts, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'}, ax=ax_virat)
                    plt.xlabel('Count')
                    plt.ylabel('Dismissal Type')
                    st.pyplot(fig_virat)

                    # Display the Sachin Tendulkar dismissal types heatmap
                    st.markdown('#### Sachin Tendulkar Dismissal Types Heatmap')
                    fig_sachin, ax_sachin = plt.subplots(figsize=(10, 4))
                    sns.heatmap(sachin_dismissal_counts, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'}, ax=ax_sachin)
                    plt.xlabel('Count')
                    plt.ylabel('Dismissal Type')
                    st.pyplot(fig_sachin)
                else:
                    st.title(f'Dismissal Analysis with respect to {opposition_filter}')
                    sub_virat_df = virat_ODI_df[virat_df['Opposition']==opposition_filter]
                    sub_sachin_df = sachin_ODI_df[sachin_df['Opposition']==opposition_filter]
                    virat_dismissal_counts = pd.crosstab(sub_virat_df['Dismissal'], columns='count')
                    sachin_dismissal_counts = pd.crosstab(sub_sachin_df['Dismissal'], columns='count')

                    st.markdown('#### Virat Kohli Dismissal Types Heatmap')
                    fig_virat, ax_virat = plt.subplots(figsize=(10, 4))
                    sns.heatmap(virat_dismissal_counts, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'}, ax=ax_virat)
                    plt.xlabel('Count')
                    plt.ylabel('Dismissal Type')
                    st.pyplot(fig_virat)

                    # Display the Sachin Tendulkar dismissal types heatmap
                    st.markdown('#### Sachin Tendulkar Dismissal Types Heatmap')
                    fig_sachin, ax_sachin = plt.subplots(figsize=(10, 4))
                    sns.heatmap(sachin_dismissal_counts, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'}, ax=ax_sachin)
                    plt.xlabel('Count')
                    plt.ylabel('Dismissal Type')
                    st.pyplot(fig_sachin)
        with tab4:
                    
                    virat_T20_df = virat_df[virat_df['Match Type']=='T20I']
                    sachin_T20_df=sachin_df[sachin_df['Match Type']=='T20I']

                    if opposition_filter == 'All':

                        st.title(f'Dismissal Analysis with respect to {opposition_filter} Opponents')
                        sub_virat_df = virat_T20_df[['Match Type','Opposition','Dismissal']]
                        sub_sachin_df = sachin_T20_df[['Match Type','Opposition','Dismissal']]
                        virat_dismissal_counts = pd.crosstab(sub_virat_df['Dismissal'], columns='count')
                        sachin_dismissal_counts = pd.crosstab(sub_sachin_df['Dismissal'], columns='count')

                        st.markdown('#### Virat Kohli Dismissal Types Heatmap')
                        fig_virat, ax_virat = plt.subplots(figsize=(10, 4))
                        sns.heatmap(virat_dismissal_counts, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'}, ax=ax_virat)
                        plt.xlabel('Count')
                        plt.ylabel('Dismissal Type')
                        st.pyplot(fig_virat)

                        # Display the Sachin Tendulkar dismissal types heatmap
                        st.markdown('#### Sachin Tendulkar Dismissal Types Heatmap')
                        fig_sachin, ax_sachin = plt.subplots(figsize=(10, 4))
                        sns.heatmap(sachin_dismissal_counts, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'}, ax=ax_sachin)
                        plt.xlabel('Count')
                        plt.ylabel('Dismissal Type')
                        st.pyplot(fig_sachin)
                    else:
                        st.title(f'Dismissal Analysis with respect to {opposition_filter}')
                        sub_virat_df = virat_T20_df[virat_df['Opposition']==opposition_filter]
                        sub_sachin_df = sachin_T20_df[sachin_df['Opposition']==opposition_filter]
                        virat_dismissal_counts = pd.crosstab(sub_virat_df['Dismissal'], columns='count')
                        sachin_dismissal_counts = pd.crosstab(sub_sachin_df['Dismissal'], columns='count')

                        st.markdown('#### Virat Kohli Dismissal Types Heatmap')
                        fig_virat, ax_virat = plt.subplots(figsize=(10, 4))
                        sns.heatmap(virat_dismissal_counts, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'}, ax=ax_virat)
                        plt.xlabel('Count')
                        plt.ylabel('Dismissal Type')
                        st.pyplot(fig_virat)

                        # Display the Sachin Tendulkar dismissal types heatmap
                        st.markdown('#### Sachin Tendulkar Dismissal Types Heatmap')
                        fig_sachin, ax_sachin = plt.subplots(figsize=(10, 4))
                        sns.heatmap(sachin_dismissal_counts, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Count'}, ax=ax_sachin)
                        plt.xlabel('Count')
                        plt.ylabel('Dismissal Type')
                        st.pyplot(fig_sachin)




    

