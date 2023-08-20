import streamlit as st
import pickle
import pandas as pd
import os

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
# movies_dict=pickle.load(open('movies_dict.pkl', 'rb'))
# movies=pd.DataFrame(movies_dict)
pickle_file_path = os.path.join(os.path.dirname(__file__), 'movies_dict.pkl')
with open(pickle_file_path, 'rb') as pickle_file:
    movies_dict = pickle.load(pickle_file)
movies=pd.DataFrame(movies_dict)


similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')
selected_movie_name=st.selectbox(
    'Choose a movie from the given list',
    movies['title'].values
)

# if st.button('Recommend'):
#     recommendations=recommend(movies['title'])
#     for i in recommendations:
#         # print(i)
#         st.write(i)
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)  # Pass the selected movie name
    for i in recommendations:
        st.write(i)