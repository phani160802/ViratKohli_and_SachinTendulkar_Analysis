import pandas as pd
import streamlit as st
import seaborn as sns
import altair as alt
import matplotlib.pyplot as plt

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

st.write("**Sachin Dataset**")
sachin_df = load_sachin_file()


st.dataframe(virat_df)
st.dataframe(sachin_df)

opposition_list = list(virat_df["Opposition"].unique())
opp_list=[str(i.strip()) for i in opposition_list ]

selected_x_var = st.selectbox('Select Opposition',
                              opp_list)


selected_player = st.radio('Select Player Name',
['Virat Kohli','Sachin Tendulkar'])

if selected_player == 'Virat Kohli':
    final_df = virat_df[virat_df['Opposition']==selected_x_var]
    st.dataframe(final_df)
elif selected_player == 'Sachin Tendulkar':
    final_df = sachin_df[sachin_df['Opposition']==selected_x_var]
    st.dataframe(final_df)
else:
    pass


st.subheader(f'Dismissal Count against {selected_x_var}')
fig, ax = plt.subplots()
sns.countplot(x='Dismissal',data=final_df)
ax.set_xlabel('Dismissal Type')
ax.set_ylabel('Count')
st.pyplot(fig)

