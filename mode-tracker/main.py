import streamlit as st   #for creating the web interface
import pandas as pd     #for data manipulation  
import datetime         #for handling date and time
import csv        #for reading and writing csv files
import os      #for interacting with the operating system

#define the file name for storing mood data
MOOD_FILE = 'mood_log.csv'

#function to load mood data from the csv file
def load_mood_data():
    #check if the file exists
    if not os.path.exists(MOOD_FILE):
        #if not, return an empty dataframe
        return pd.DataFrame(columns=['Date', 'Mood'])
    #read and return the data from the file
    return pd.read_csv(MOOD_FILE)

#function to save mood data to the csv file
def save_mood_data(date, mood):
    #open the file in append mode
    with open(MOOD_FILE, 'a',  encoding='utf-8') as file:
        #create a csv writer object
        writer = csv.writer(file)
        #add new mode entry
        writer.writerow([date, mood])


st.title('Mood Tracker')
#get today's date
today = datetime.date.today()

st.subheader("How are you feeling today?")
mood = st.selectbox('Select Your Mood', ['Happy 😄', ' Shocked 😲', 'Angry 😡' ,' Sad 😢', 'Neutral 😐'])

if st.button('Log Mood'):
    save_mood_data(today, mood)
    st.success('Mood Logged Successfully!')

data = load_mood_data()

if not data.empty:
    st.subheader("Mood Trends Over Time")

    data['Date'] = pd.to_datetime(data['Date'])
    #create freqency of each mode
    mood_counts = data.groupby("Mood").count()["Date"]

    st.bar_chart(mood_counts)

