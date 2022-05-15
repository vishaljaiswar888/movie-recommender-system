import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
     response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=ab237a8649d6a4853891a64247a521c3&language=en-US".format(movie_id))
     data = response.json()
     return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


def recommend(movie):
     movie_index = movies[movies["title"] == movie].index[0]
     distances = similarity[movie_index]
     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

     recommended_movies = []
     recommended_movies_poster = []
     for i in movies_list:
          movie_id = movies.iloc[i[0]].id

          recommended_movies.append(movies.iloc[i[0]].title)
          # fetching poster from API
          recommended_movies_poster.append(fetch_poster(movie_id))
     return recommended_movies, recommended_movies_poster


similarity = pickle.load(open("similarity.pkl", "rb"))

movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

st.title("Movie Recommender System")


selected_movie_name = st.selectbox(
     'Select the movie you need recommendations for!😉',
     movies["title"].values)

st.write('You selected:', selected_movie_name)


if st.button('Recommend'):
     names, posters = recommend(selected_movie_name)
     st.write("Enjoy our recommendations below!😀")

     col1, col2, col3, col4, col5 = st.columns(5)

     with col1:
          st.write(names[0])
          st.image(posters[0])

     with col2:
          st.write(names[1])
          st.image(posters[1])

     with col3:
          st.write(names[2])
          st.image(posters[2])

     with col4:
          st.write(names[3])
          st.image(posters[3])

     with col5:
          st.write(names[4])
          st.image(posters[4])

#     for i in recommendations:
#         st.write(i)
else:
     st.write('Click the recommend button for the recommendations!🙂')