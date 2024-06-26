import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images\gustavo.jpeg')

with col2:
    st.title('Gustavo Marchioretto')
    content = """
    Hi, I am Gustavo! I am a Python programmer. Nesse curso, tive a oportunidade de aprender profundamente a linguagem Python, desde machine learning e data science até web development. Aprendi também OOP, APIs, SQL, Git, GUIs, Flash, Django, Bootstrap, ML e AI.
Apenas alguns exemplos que fiz no curso foram aplicativos web, sistema de recomendação de filmes, painéis de visualização de dados e GUIs de desktop.    
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Fell free too contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")
