import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import numpy as np
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
import mplfinance as mpf
import stockstats
from get_all_tickers import get_tickers as gt
from pandas_datareader import data
from millify import millify
import random

report = open("report.txt", "w")
input_smaDay = 20
downloadStartDate = dt.datetime.now() - dt.timedelta(days=input_smaDay * 2 + 16)
TenWeeksAgoDate = dt.datetime.now() - dt.timedelta(days=70)
downloadEndDate = dt.datetime.now()

print("Start generating Sell report ......")
report.write("--------------- SELL LIST ---------------\n")
input_checkForSellList = ['TSLA']
sellcount = 0
for i in range(0, len(input_checkForSellList)):
    isSell = False
    print("Checking for " + input_checkForSellList[i])
    df = yf.download(input_checkForSellList[i], downloadStartDate, downloadEndDate, interval='1d')
    if (df.empty):
        continue
    lastDayPrice = df["Close"].iloc[-1]

    sma = df.rolling(window=input_smaDay).mean()

    if (df["High"].iloc[-1] > sma["Close"].iloc[-1] and df["Low"].iloc[-1] < sma["Close"].iloc[-1]):
        isSell = True

    stock = stockstats.StockDataFrame.retype(df)
    rsi = stock["rsi_14"]
    if (rsi.iloc[-1] > 62):
        isSell = True

    if (isSell):
        sellcount = sellcount + 1
        print("Added to sell list :" + input_checkForSellList[i])
        report.write(str(sellcount) + " ********************\n")
        report.write("Stock: " + input_checkForSellList[i] + "\n")
        report.write("Current Price: " + str(lastDayPrice) + "\n")

        df10w = yf.download(input_checkForSellList[i], TenWeeksAgoDate, downloadEndDate, interval='1d')
        report.write("10 weeks high: " + str(df10w["High"].max()) + "\n")
        report.write("10 weeks low: " + str(df10w["Low"].min()) + "\n")
        report.write("RSI: " + str(rsi.iloc[-1]) + "\n")
        report.write("SMA: " + str(sma["Close"].iloc[-1]) + "\n")
        report.write("Today's volume: " + str(df10w["Volume"].iloc[-1]) + "\n")
        report.write("Average volume: " + str(df10w["Volume"].mean()) + "\n")
        marketCap = data.get_quote_yahoo(input_checkForSellList[i])['marketCap']
        report.write("Market capital: " + str(millify(marketCap, precision=2)) + "\n")
        report.flush()

print("Start generating Buy report ......")
report.write("\n--------------- BUY LIST ---------------\n")

stocksList = gt.get_tickers()
input_rsi_high = 200
input_rsi_low = 5
input_max_days = 50
input_amplification = 0.8
buyCount = 0
for i in range(0, len(stocksList)):
    print("Checking for " + stocksList[i])
    try:
        marketCap = data.get_quote_yahoo(stocksList[i])['marketCap']
    except:
        print("exception")
        continue
    if (marketCap.values[0] < 2000000000):
        print("Market cap below 2B BBBBBBBBBBBBBBBB")
        continue
    df = yf.download(stocksList[i], downloadStartDate, downloadEndDate, interval='1d')
    if (df.empty):
        print("df is empty yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        continue
    lastDayPrice = df["Close"].iloc[-1]
    sma = df.rolling(window=input_smaDay).mean()
    if (df["Low"].iloc[-1] < sma["Close"].iloc[-1]):
        print("last day lowest below SMA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        continue
    if (df["Close"].iloc[-1] < 6):
        print("less than 5$ 5555555555555555555555555555555555555555555555555555555555")
        continue

    stock = stockstats.StockDataFrame.retype(df)
    rsi = stock["rsi_14"]
    if (rsi.iloc[-1] > input_rsi_high):
        print("rsi too high hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        continue
    if (rsi.iloc[-1] < input_rsi_low):
        print("rsi too low lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
        continue
    if (rsi.iloc[-1] < rsi.iloc[-3]):
        print("2 days ago > today rsi 22222222222222222222222222222222222222222222222222222222222222222222222222222222")
        continue
    xDaysAgoDate = dt.datetime.now() - dt.timedelta(days=input_max_days)
    dfXDays = yf.download(stocksList[i], xDaysAgoDate, downloadEndDate, interval='1d')
    if (dfXDays["High"].max() < input_amplification * dfXDays["Close"].iloc[-1]):
        print(
            "Max < current stock MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
        continue

    buyCount = buyCount + 1
    print("Added to buy list :" + stocksList[
        i] + " ///////////////////////////////////////////////////////////////////////////////////////////")
    report.write(str(buyCount) + " ********************\n")
    report.write("Stock: " + stocksList[i] + "\n")

    report.write("Current Price: " + str(lastDayPrice) + "\n")
    df10w = yf.download(stocksList[i], TenWeeksAgoDate, downloadEndDate, interval='1d')
    report.write("10 weeks high: " + str(df10w["High"].max()) + "\n")
    report.write("10 weeks low: " + str(df10w["Low"].min()) + "\n")
    report.write("RSI: " + str(rsi.iloc[-1]) + "\n")
    report.write("SMA: " + str(sma["Close"].iloc[-1]) + "\n")
    report.write("Today's volume: " + str(df10w["Volume"].iloc[-1]) + "\n")
    report.write("Average volume: " + str(df10w["Volume"].mean()) + "\n")
    report.write("Market capital: " + str(millify(marketCap, precision=2)) + "\n")
    report.flush()

report.close()
