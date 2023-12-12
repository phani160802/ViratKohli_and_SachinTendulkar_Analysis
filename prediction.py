
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier



dt = DecisionTreeClassifier(max_depth=5,min_samples_leaf=15,random_state=42)

def show_prediction(virat_df,sachin_df):


    st.markdown("## Step into the Prediction Game!")
    st.markdown("Here, you have the chance to forecast outcomes such as a player's run tally based on specific parameters or predict how a player might be dismissed against particular opposition.")

    target_variable = st.selectbox("Select the outcome which you want to be predicted...",['Runs','Dismissal'])

    
    
    grounds_list = ['Colombo (RPS)','Johannesburg','Mohali','Nagpur','Mirpur','Ahmedabad','Wankhede','Hyderabad','Melbourne']


    opposition_list = ['Australia','Sri Lanka','New Zealand','Pakistan']

    #virat_df = virat_df[virat_df['Ground'].isin(grounds_list)]
    sachin_df=sachin_df[sachin_df['Ground'].isin(grounds_list)]
    

    #ground_list.remove('Kingston','Canberra','Centurion','Paarl','Wellington','Gqeberha','Hamilton','Napier','Bulawayo','Leeds','')
    if target_variable == 'Dismissal':
        st.write("Classification algorithm should be used")
        match_filter = st.sidebar.selectbox("Select Match Type:", virat_df['Match Type'].unique().tolist(), index=0)
        ground_filter = st.sidebar.selectbox("Select Ground:", grounds_list, index=0)
        opposition_filter = st.sidebar.selectbox("Select Opposition:",opposition_list, index=0)

        le_opposition = LabelEncoder()
        le_ground = LabelEncoder()
        le_match_type = LabelEncoder()
        le_dismissal = LabelEncoder()

        user_input = {
                            'Match Type':match_filter,
                            'Ground': ground_filter,
                            'Opposition': opposition_filter
                            }


        def virat_prediction(user_input):
             # Sampling Data to tackle Class Imbalance Problem for virat Dataset

                df_sample = virat_df[['Opposition', 'Ground', 'Match Type', 'Dismissal']]

                grouped = df_sample.groupby(['Dismissal', 'Opposition', 'Match Type'])

                samples_per_group = min(grouped.size())

                sampled_data = grouped.apply(lambda x: x.sample(samples_per_group))

                sampled_data = sampled_data.reset_index(drop=True)

                sampled_data = sampled_data.drop(sampled_data[sampled_data['Dismissal'] == 'not out'].index)



                sampled_data['Match Type'] = le_match_type.fit_transform(sampled_data['Match Type'])
                sampled_data['Ground'] = le_ground.fit_transform(sampled_data['Ground'])
                sampled_data['Opposition'] = le_opposition.fit_transform(sampled_data['Opposition'])
                sampled_data['Dismissal'] = le_dismissal.fit_transform(sampled_data['Dismissal'])
                
                user_input_df = pd.DataFrame([user_input])
                user_input_df['Match Type'] = le_match_type.transform([user_input_df['Match Type']])
                user_input_df['Opposition'] = le_opposition.transform([user_input_df['Opposition']])
                user_input_df['Ground'] = le_ground.transform([user_input_df['Ground']])


                x_train = sampled_data[['Match Type','Ground','Opposition']]
                y_train = sampled_data['Dismissal']

                # dt = DecisionTreeClassifier(max_depth=5,min_samples_leaf=15,random_state=42)

                dt.fit(x_train,y_train)

                predicted_dismissal = dt.predict(user_input_df)
                
                return predicted_dismissal


        def sachin_prediction(user_input):

             # Sampling Data to tackle Class Imbalance Problem for virat Dataset

                df_sample = sachin_df[['Opposition', 'Ground', 'Match Type', 'Dismissal']]

                grouped = df_sample.groupby(['Dismissal', 'Opposition', 'Match Type'])

                samples_per_group = min(grouped.size())

                sampled_data = grouped.apply(lambda x: x.sample(samples_per_group))

                sampled_data = sampled_data.reset_index(drop=True)

                sampled_data = sampled_data.drop(sampled_data[sampled_data['Dismissal'] == 'not out'].index)



                sampled_data['Match Type'] = le_match_type.fit_transform(sampled_data['Match Type'])
                sampled_data['Ground'] = le_ground.fit_transform(sampled_data['Ground'])
                sampled_data['Opposition'] = le_opposition.fit_transform(sampled_data['Opposition'])
                sampled_data['Dismissal'] = le_dismissal.fit_transform(sampled_data['Dismissal'])
                
            
                user_input_df = pd.DataFrame([user_input])
                user_input_df['Match Type'] = le_match_type.transform([user_input_df['Match Type']])
                user_input_df['Opposition'] = le_opposition.transform([user_input_df['Opposition']])
                user_input_df['Ground'] = le_ground.transform([user_input_df['Ground']])


                x_train = sampled_data[['Match Type','Ground','Opposition']]
                y_train = sampled_data['Dismissal']

                dt.fit(x_train,y_train)

                predicted_dismissal = dt.predict(user_input_df)
                
                return predicted_dismissal

             
        
        
        st.markdown("### Filters Selected: ")
        st.markdown(f"Match Type: {match_filter}")
        st.markdown(f"Opposition: {opposition_filter}")
        st.markdown(f"Ground at player will Bat: {ground_filter}")
        st.markdown("### Predictions: ")

        #predicted_dismissal = dt.predict(user_input_df)

        sachin_pred = sachin_prediction(user_input)
        virat_pred = virat_prediction(user_input)


        st.write(f' Sachins Predicted Dismissal is {le_dismissal.inverse_transform([sachin_pred])[0]}')
        st.write(f' Virats Predicted Dismissal is {le_dismissal.inverse_transform([virat_pred])[0]}')






    else:
        st.write("Linear Regression can be used for this")

        if target_variable == 'Runs':
            
            Strike_rate =st.sidebar.text_input(
            "Enter Strike Rate at which player will score runs",
            "0.00",
            key="placeholder",
            )

            # Linear Model

            lm = LinearRegression()

            # Input Filters

            opposition_filter = st.sidebar.selectbox("Select Opposition:",opposition_list, index=0)
            ground_filter = st.sidebar.selectbox("Select Ground:",grounds_list, index=0)
            Inns = sorted(virat_df['Pos'].unique().tolist())
            inns_filter=st.sidebar.slider("Select Innings: ",1,2)
            pos_filter=st.sidebar.slider("Select Position: ",Inns[0],Inns[-1])
            fours_filter = st.sidebar.slider("Select Number of Fours: ", 1,50)
            sixes_filter = st.sidebar.slider("Select Number of Sixes: ", 1,50)


            # Creating Dictionary for user inputs
            user_input = {
                    'SR':Strike_rate,
                    'Opposition': opposition_filter,
                    'Inns':inns_filter,
                    'Pos':pos_filter,
                    'Ground': ground_filter,
                    '4s': fours_filter, 
                    '6s': sixes_filter            }


            # Label Encoding

            le_opposition = LabelEncoder()
            le_ground = LabelEncoder()

            def virat_runs_pred(user_input):
                    virat_df['Opposition'] = le_opposition.fit_transform(virat_df['Opposition'])
                    virat_df['Ground'] = le_ground.fit_transform(virat_df['Ground'])
                    # Regression Model
                    x_train = virat_df[['SR','Opposition','Inns','Pos','Ground','4s','6s']]
                    y_train=virat_df['Runs']

                    lm.fit(x_train,y_train)
                    


                    # Now Predicting the user given data using regression model

                    user_input['Opposition'] = le_opposition.transform([user_input['Opposition']])[0]
                    user_input['Ground'] = le_ground.transform([user_input['Ground']])[0]

                    user_input_df = pd.DataFrame([user_input])

                    predicted_runs = lm.predict(user_input_df[['SR','Opposition','Inns','Pos','Ground','4s','6s']])

                    return predicted_runs
            

            def sachin_runs_pred(user_input):
                sachin_df['Opposition'] = le_opposition.fit_transform(sachin_df['Opposition'])

                # Transform 'Match Type' for the user input only
                user_input_df = pd.DataFrame([user_input])
                # user_input_df['Match Type'] = le_match_type.transform([user_input_df['Match Type']])[0]

                x_train = sachin_df[['SR', 'Opposition', 'Inns', 'Pos', '4s', '6s']]
                y_train = sachin_df['Runs']

                lm.fit(x_train, y_train)

                user_input_df['Opposition'] = le_opposition.transform([user_input_df['Opposition']])[0]

                predicted_runs = lm.predict(user_input_df[['SR', 'Opposition', 'Inns', 'Pos', '4s', '6s']])

                return predicted_runs

                        

            st.markdown("### Filters Selected: ")
            st.markdown(f"Opposition: {opposition_filter}")
            st.markdown(f"Innings: {inns_filter}") 
            st.markdown(f"Position at which player will Bat: {pos_filter}")
            st.markdown(f"Ground at player will Bat: {ground_filter}")
            st.markdown(f"4s Scored: {fours_filter}")
            st.markdown(f"6s Scored: {sixes_filter}") 

            st.markdown("### Predictions: ")
            
            sachin_pred_runs = sachin_runs_pred(user_input)
            virat_pred_runs = virat_runs_pred(user_input)

            st.write('Virat Predicted Runs is {}'.format(virat_pred_runs))
            st.write('Sachin Predicted Runs is {}'.format(sachin_pred_runs))


        