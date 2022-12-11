import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps2.pk1', 'rb') as file:
        data = pickle.load(file)
    return data

data=load_model()

regressor = data["model"]

def show_predict_page():
    st.title("Musical Album Rating Prediction")
    st.header("""Let's classify the album by genres""")
    
    col01, col00, col02 = st.columns([6,1,6])
    with col01:
        country = st.checkbox('Country/Folk',value=False,disabled=False)
        dance = st.checkbox('Dance/EDM',value=False,disabled=False)
        hiphop = st.checkbox('Hip Hop',value=False,disabled=False)
        jazz = st.checkbox('Jazz',value=False,disabled=False)
        metal = st.checkbox('Metal',value=False,disabled=False)
    with col02:
        pop = st.checkbox('Pop',value=False,disabled=False)
        punk = st.checkbox('Punk',value=False,disabled=False)
        rock = st.checkbox('Rock',value=False,disabled=False)
        rb = st.checkbox('R&B',value=False,disabled=False)
        soul = st.checkbox('Soul',value=False,disabled=False)

    st.header("""Let's use keywords to describe the album""")
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.subheader("""Lyrics""")
        aggressive = st.checkbox('Aggressive',value=False,disabled=False)
        concept = st.checkbox('Concept Album',value=False,disabled=False)
        conscious = st.checkbox('Conscious',value=False,disabled=False)
        dark = st.checkbox('Dark',value=False,disabled=False)
        mysterious = st.checkbox('Mysterious',value=False,disabled=False)
        playful = st.checkbox('Playful',value=False,disabled=False)
        poetic = st.checkbox('Poetic',value=False,disabled=False)
        political = st.checkbox('Political',value=False,disabled=False)
        romantic = st.checkbox('Romantic',value=False,disabled=False)
        sentimental = st.checkbox('Sentimental',value=False,disabled=False)
        
    
    with col2:
        st.subheader("""Production""")
        atmospheric = st.checkbox('Atmospheric',value=False,disabled=False)
        energetic = st.checkbox('Energetic',value=False,disabled=False)
        female = st.checkbox('Female Vocals',value=False,disabled=False)
        futuristic = st.checkbox('Futuristic',value=False,disabled=False)
        instrumental = st.checkbox('Instrumental',value=False,disabled=False)
        malevocals = st.checkbox('Male Vocals',value=False,disabled=False)
        melodic = st.checkbox('Melodic',value=False,disabled=False)
        psychedelic = st.checkbox('Psychedelic',value=False,disabled=False)
        sampling = st.checkbox('Sampling',value=False,disabled=False)
        sombre = st.checkbox('Sombre',value=False,disabled=False)

   
    with col3:
        st.subheader("""Feelings""")
        angry=st.checkbox('Angry',value=False,disabled=False)
        bittersweet =st.checkbox('Bittersweet',value=False,disabled=False)
        heavy  = st.checkbox('Heavy/Dense',value=False,disabled=False)
        introspective = st.checkbox('Introspective',value=False,disabled=False)
        lonely = st.checkbox('Lonely',value=False,disabled=False)
        melancholic = st.checkbox('Melancholic', value=False, disabled=False)
        mellow = st.checkbox('Mellow',value=False,disabled=False)
        passionate = st.checkbox('Passionate',value=False,disabled=False)
        sad = st.checkbox('Sad',value=False,disabled=False)
        uplifting = st.checkbox('Uplifting',value=False,disabled=False)

    st.header("""Let's define some numerical scales""")
    col4,col5,col6 = st.columns([6,1,6])
    with col4:
        st.subheader("""Acousticness""")
        acoustic = st.slider('Measures the usage of acoustic and non-eletronic instruments in the tracks. Value 1, least acoustic. Value 5, most acousitc.',1,5)
        st.subheader("""Instrumentalness""")
        instrumentalness = st.slider('Measures the presence of vocals and instruments in the tracks. Value 1, higher presence of vocals. Value 5, higher presence of instruments.',1,5)

    with col6:
        st.subheader("""Danceability""")
        danceability = st.slider('Measures how suitable the tracks are for dancing based on the rhythm, tempo and beat strength. Value 1, least danceable. Value 5, most danceable.',1,5)
        st.subheader("""Speechiness""")
        speechiness = st.slider('Measures the presence of spoken words in the tracks. Value 1, higher singing aspect. Value 5, higher rapping/spoken performances.',1,5)

    ok = st.button("Predict Album Rating")
    if ok:
        X = np.array([[acoustic,speechiness,instrumentalness,danceability,rb,metal,jazz,punk,country,hiphop,dance,soul,pop,rock,futuristic,instrumental,sombre,energetic,melodic,atmospheric,sampling,psychedelic,female,malevocals,mysterious,sentimental,aggressive,romantic,dark,political,conscious,concept,playful,poetic,sad,uplifting,heavy,angry,lonely,bittersweet,passionate,mellow,melancholic,introspective]])
        X= X.astype(float)
        rating = regressor.predict(X)
        if acoustic==1 and instrumentalness==1 and danceability==1 and speechiness==1 and rb==False and metal==False and jazz==False and punk==False and country==False and hiphop==False and dance==False and soul==False and pop==False and rock==False and futuristic==False and instrumental==False and sombre==False and energetic==False and melodic==False and atmospheric==False and sampling==False and psychedelic==False and female==False and malevocals==False and mysterious==False and sentimental==False and aggressive==False and romantic==False and dark==False and political==False and conscious==False and concept==False and playful==False and poetic==False and sad==False and uplifting==False and heavy==False and angry==False and lonely==False and bittersweet==False and passionate==False and mellow==False and melancholic==False and introspective==False:
            st.subheader(f"Insert some data first.")
        else:
            st.header(f"Estimated Album Rating: {rating[0]:.2f}")

show_predict_page()






    