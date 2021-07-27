import streamlit as st
import datetime
import urllib.request as urllib2
#from bs4 import BeautifulSoup
import pandas as pd
import lxml
import matplotlib as plot
from PIL import Image
import subprocess
from subprocess import check_output
import pytz


def app():
    def get_todays_date():
        tz = pytz.timezone('Australia/Sydney')
        now = datetime.datetime.now(tz)
        
        today = str(now)
        today = today[0:16]
       
        ReturnString_1 = "Date and time is " + today
        return (ReturnString_1)

    col1, col2 = st.beta_columns([2.5,10])
    st.title("Giant Steps STEM")
    #with col1:
       

    #with col2:
       # st.title("Giant Steps STEM")

    st.title('Welcome to the Darangarra Class Giant Steps Sydney Weather App')
    st.write('Designed and created by J,J & G')
    st.write('Potential inclusions weather conditions now, tempurature relative to school policy- heat stress->Drink some water, Severe weather warning, air quaility GOOD/BAD/MODERATE, UV SUNSMART any others you can think of')
    
    date = get_todays_date()

    st.write(date)
    st.write('Inclusion of digital art creations potentially from Minecraft for season or weather etc')
    st.image('GS Block.jpg')

  #define functio to read weather data and create a dataframe weatherzone and DPIE for air quaility
    
   
