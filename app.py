import sklearn
import pickle
import streamlit as st

movies = pickle.load(open('movies.pkl','rb'))

similarity = pickle.load(open('similarity.pkl','rb'))

st.header("Movie Recommender System")
selected = st.selectbox("Select your favorite movie",movies)

def recommender(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recomended = []
    for i in distance[1:6]:
        recomended.append(movies.iloc[i[0]].title)
    return recomended

if st.button("Recommend"):
    recommended_movies = recommender(selected)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(recommended_movies[0])
    with col2:
        st.text(recommended_movies[1])
    with col3:
        st.text(recommended_movies[2])
    with col4:
        st.text(recommended_movies[3])
    with col5:
        st.text(recommended_movies[4])