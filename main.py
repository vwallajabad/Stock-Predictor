import yfinance
input_stock = input(': ')

Stock = yfinance.Ticker(input_stock)

data = Stock.history(period='5mo').reset_index()

BETA = Stock.info['beta'] #Stock Beta

price0 = data.Open[0]
price1 = data.Open[1]
price2 = data.Open[2]
price3 = data.Open[3] 
price4 = data.Open[4] 
price5 = data.Open[5]
price6 = data.Open[6]
price7 = data.Open[7]
price8 = data.Open[8] 
price9 = data.Open[9] 
price10 = data.Open[10]
price11 = data.Open[11]
price12 = data.Open[12]
price13 = data.Open[13] 
price14 = data.Open[14] 
price15 = data.Open[15]
price16 = data.Open[16]
price17 = data.Open[17]
price18 = data.Open[18] 
price19 = data.Open[19] 
price20 = data.Open[20]
price21 = data.Open[21]
price22 = data.Open[22]
price23 = data.Open[23] 
price24 = data.Open[24] 
price25 = data.Open[25]
price26 = data.Open[26]
price27 = data.Open[27]
price28 = data.Open[28] 
price29 = data.Open[29] 

#Import Some Modules
import numpy
import matplotlib.pyplot as plt 
import replit

#Dataset Variables 
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [price0, price1, price2, price3, price4, price5, price6, price7, price8, price9, price10, price11, price12, price13, price14, price15, price16, price17, price18, price19, price20, price21, price22, price23, price24, price25, price26, price27, price28, price29]

#Machine Learning Train
train_x = x[:80]
train_y = y[:80]

#Machine Learning Test
test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, BETA))

myline = numpy.linspace(0, 40, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))

replit.clear()
print("Thanks for using my stock predictor! \nTo view the source code visit:\nhttps://github.com/vwallajabad/stock.prediction")
#Shows Graph
plt.show()

retry = input("Would you like to use it again type Y for yes and N for no: ")

