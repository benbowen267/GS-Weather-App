import HomePage
import GSSYDNEY
import streamlit as st
PAGES = {
    "Home Page": HomePage,
    "GS Sydney": GSSYDNEY
}
st.sidebar.title('Navigation Pages')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
#app.run()
