import streamlit as st
from streamlit_auth import Auth

def main():
    st.title("Streaming App")
    
    # Configuración de autenticación
    auth = Auth(app_name="Streaming App")
    auth.login()
    
    # Página de inicio
    if st.sidebar.button("Inicio"):
        show_homepage()
    
    # Página de películas
    if st.sidebar.button("Películas"):
        show_movies()
    
    # Página de series
    if st.sidebar.button("Series"):
        show_tv_shows()

def show_homepage():
    st.header("Bienvenido a la página de inicio")
    # Aquí puedes agregar contenido relacionado con la página de inicio

def show_movies():
    st.header("Películas")
    # Aquí puedes agregar contenido relacionado con la página de películas

def show_tv_shows():
    st.header("Series")
    # Aquí puedes agregar contenido relacionado con la página de series

if __name__ == "__main__":
    main()
