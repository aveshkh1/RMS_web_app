import streamlit as st
import joblib
import pandas as pd
import requests
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['original_title'] == movie].index[0]
    distances = similarity[index]
    movies_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_posters = []
    recommended_movies=[]
    for i in movies_list:
        id=movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(id))
        recommended_movies.append(movies.iloc[i[0]].original_title)
    return recommended_movies,recommended_movie_posters

similarity=joblib.load('Similarity')
movie_list = joblib.load('movies_dict')
st.title('Movie Recommendation system')
movies=pd.DataFrame(movie_list)
selected_movie=st.selectbox(
    'How to be contacted',
    movies['original_title'].values)
if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

