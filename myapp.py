import yfinance as yf
import streamlit as st 
import pandas as pd

st.write("""
         # Precio de una acción en particular
         
         Aqui vamos a ver el precio de una acción!
         
         """)

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2020-3-26', end='2024-3-26')
         
st.line_chart(tickerDf.Close)

st.line_chart(tickerDf.Volume)
         