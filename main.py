import streamlit as st
import pandas as pd
import pickle


def recommend(place):
    places_index = places[places['Places'] == place].index[0]
    distances = similarity[places_index]
    places_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_places = []
    for i in places_list:
        recommended_places.append(places.iloc[i[0]].Places)
    return recommended_places

places_list = pickle.load(open('places_dict.pickle','rb'))
places = pd.DataFrame(places_list)

similarity = pickle.load(open('similarity.pkl','rb'))
places_list = places_list['Places'].values

st.title('Places Recommendation')

selected_movie_name = st.selectbox(
'Enter places',
places['Places'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)