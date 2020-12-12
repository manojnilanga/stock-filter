# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import yfinance as yf
import datetime as dt
import stockstats
from get_all_tickers import get_tickers as gt
from pandas_datareader import data
from millify import millify


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1112, 358)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 85, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(140, 80, 104, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 125, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(140, 120, 104, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(640, 70, 411, 81))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(140, 170, 61, 31))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 170, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(240, 170, 51, 31))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 170, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(660, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(False)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(520, 80, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setScaledContents(False)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 250, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.generate)
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(280, 120, 104, 31))
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(260, 120, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setScaledContents(False)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1112, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SMA days"))
        self.label_2.setText(_translate("MainWindow", "RSI Values"))
        self.label_3.setText(_translate("MainWindow", "MAX days"))
        self.label_4.setText(_translate("MainWindow", "To create buy report"))
        self.label_5.setText(_translate("MainWindow", ">"))
        self.label_6.setText(_translate("MainWindow", "x   current stock price"))
        self.label_7.setText(_translate("MainWindow", "To create sell report"))
        self.label_8.setText(_translate("MainWindow", "Stocks to check"))
        self.pushButton.setText(_translate("MainWindow", "Generate report"))
        self.label_9.setText(_translate("MainWindow", "-"))

        self.plainTextEdit.setPlainText("20")
        self.plainTextEdit_2.setPlainText("100")
        self.plainTextEdit_6.setPlainText("50")
        self.plainTextEdit_4.setPlainText("50")
        self.plainTextEdit_5.setPlainText("1.25")

    def generate(self):
        report = open("report.txt", "w")
        input_smaDay = int(self.plainTextEdit.toPlainText())
        input_rsi_high = int(self.plainTextEdit_2.toPlainText())
        input_rsi_low = int(self.plainTextEdit_6.toPlainText())
        input_max_days = int(self.plainTextEdit_4.toPlainText())
        input_amplification = float(self.plainTextEdit_5.toPlainText())
        input_checkForSell = self.plainTextEdit_3.toPlainText()

        downloadStartDate = dt.datetime.now() - dt.timedelta(days=input_smaDay * 2 + 16)
        TenWeeksAgoDate = dt.datetime.now() - dt.timedelta(days=70)
        downloadEndDate = dt.datetime.now()

        print("Start generating Sell report ......")
        report.write("--------------- SELL LIST ---------------\n")
        input_checkForSellList = input_checkForSell.split(",")
        sellcount = 0
        for i in range(0, len(input_checkForSellList)):
            try:
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
            except:
                continue

        print("Start generating Buy report ......")
        report.write("\n--------------- BUY LIST ---------------\n")

        stocksList = gt.get_tickers()
        buyCount = 0
        for i in range(0, len(stocksList)):
            print("Checking for " + stocksList[i])
            try:
                marketCap = data.get_quote_yahoo(stocksList[i])['marketCap']
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
            except:
                print("Exception")
                continue

        report.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
