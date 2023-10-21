import streamlit as st
import bcrypt

def main():
    st.title("Streaming App")
    
    # Check if user is logged in
    if "username" not in st.session_state:
        show_login_page()
    else:
        show_homepage()

def show_login_page():
    st.header("Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        # Check if username and password are valid
        if check_credentials(username, password):
            st.session_state["username"] = username
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

def check_credentials(username, password):
    # You can replace this with your own authentication logic
    # For simplicity, we're using a hardcoded username and password
    hashed_password = b'$2b$12$3X3Z6Z6Z6Z6Z6Z6Z6Z6Z6Z6Z6Z6Z6Z6Z6Z6Z6Z6Z6Z6Z6Z6Z6Z6Z6'
    return bcrypt.checkpw(password.encode(), hashed_password)

def show_homepage():
    st.header(f"Welcome, {st.session_state['username']}!")
    # Add content for the homepage here

if __name__ == "__main__":
    main()
