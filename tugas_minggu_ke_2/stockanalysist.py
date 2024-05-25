# command untuk run -> streamlit run stockanalysist.py
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from datetime import date, timedelta
import streamlit as st

# command untuk run -> streamlit run stockanalysist.py

gap = 365
today = date.today()
today = today.strftime(f"%Y-%m-%d")
start_date = date.today() - timedelta(days=gap)
start_date = start_date.strftime(f"%Y-%m-%d")

st.title("Annual Stock Price Data Plot")
st.write('Stock Symbol : https://stockanalysis.com/stocks/')
a = st.text_input("Input Stock Symbol :")

if a != "" :
    data = web.DataReader(a, 'stooq').loc[start_date:today]
    data['Volume'] = data['Volume']/1000000
    day = [10, 20, 50]

    for sma in day:
        column_name = f"MA for {sma} days"
        data[column_name] = data['Close'].rolling(sma).mean()

    for sma in day:
        column_name = f"Volume MA for {sma} days"
        data[column_name] = data['Volume'].rolling(sma).mean()
    
    fig, ax = plt.subplots(3,layout="constrained",figsize=(15, 15))
    data["Close"].plot(ax = ax[0], title=a+" Stock Prices ", fontsize=20, label="Close Price")
    data[["Close",'MA for 10 days','MA for 20 days','MA for 50 days']].plot(ax = ax[1],title="CLOSE Moving Average",fontsize=20)
    data[['Volume MA for 10 days','Volume MA for 20 days','Volume MA for 50 days']].plot(ax = ax[2],title="VOLUME Moving Average",fontsize=20)

    st.pyplot(fig)

# command untuk run -> streamlit run stockanalysist.py
