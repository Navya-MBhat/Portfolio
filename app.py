import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json

# emoji taken from the website ...  https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Portfolio" , page_icon=":smiling_face_with_halo:", layout="wide")

def load_lottie_code(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# loading animation from lottiefiles
lottie_code_completion = load_lottie_code("https://lottie.host/f0f250bb-60bb-408e-8ccb-72c33c39b93a/4PXdFzxG70.json")
lottie_code_education = load_lottie_code("https://lottie.host/55292042-fac0-4173-9607-3d2a59745aad/qOOi1Sv1IE.json")

# Header Section
with st.container():
    st.subheader("Hey there! I am Navya Bhat :snowflake:")
    st.title(" # Fresher  # Enthusiatic Learner")
    st.write("Passionate about AI and Machine learning and open to explore the python development,software and web development..")
    st.write("[Linkedin Profile  ||  ](https://www.linkedin.com/in/navya-bhat-b95721299)", "[Github Profile :)](https://github.com/Navya-MBhat)")

# My work..
with st.container():
    st.write("---")
    left_column , right_column = st.columns(2)
    with left_column:
        st.header("My accomplishments ")
        st.write("##")
        st.write(
            """
            - Attended 2 days PowerBI workshop by Skill nation
            - Attended 16th International conference on COMmunication System & NETworkS (COMSNET 2024)
            - Participated in bootstrap program, conducting lecture on Wix- a website builder 
            - Attended international webinar on AI & Machine learning
            - Attended workshop on php
            - Participated in internal hackathon organized by MCA department,PES University, Bengaluru

            """
        )
        st.write("##")
        
    with right_column:
        st_lottie(lottie_code_completion  , height=300 , key="completion")

# My education..
with st.container():
    st.write("---")
    left_column , right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_code_education , height=300 , key="education")
    with right_column:
        st.header(" Education ")
        st.write("##")
        st.write(
            """
            - Currently doing Masters in Computer Applications at PES University, Bengaluru
            - B.Sc degree graduate from Karnataka Science College, Dharwad
            - Completed 12th and 10th from Jawahar Navodaya Vidyalaya , Malagi           

            """
        )
        st.write("##")
        
# Projects
with st.container():
    st.write("---")
    st.header("Projects")
    st.write("##")
    st.write(
        """
        - Personalised reccommendation system using Graphology : 
          Implementing machine learning to characterize the personality features of a person 
          using their handwriting and reccommending a set of activities with rule based reccommendation system

        - Biginner friendly projects using html, css , java script, Reactjs, vite.
           (can look up in Github profile)
        """
        )
    
