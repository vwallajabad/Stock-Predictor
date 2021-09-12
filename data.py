Stock = input("Enter stock ticker: ")
#Edit ONLY this for stock prediction
#{
BETA = float(input("Enter stock beta: ")) #Stock Beta
price0 = float(input("Enter stock price 30 days ago: ")) #Stock price 5 trading days ago
price1 = float(input("Enter stock price 29 days ago: ")) #Stock price 4 trading days ago
price2 = float(input("Enter stock price 28 days ago: ")) #Stock price 3 trading days ago
price3 = float(input("Enter stock price 27 days ago: ")) #Stock price 2 trading days ago
price4 = float(input("Enter stock price 26 days ago: ")) #Stock price Today
price5 = float(input("Enter stock price 25 days ago: ")) #Stock price 5 trading days ago
price6 = float(input("Enter stock price 24 days ago: ")) #Stock price 4 trading days ago
price7 = float(input("Enter stock price 23 days ago: ")) #Stock price 3 trading days ago
price8 = float(input("Enter stock price 22 days ago: ")) #Stock price 2 trading days ago
price9 = float(input("Enter stock price 21 days ago: ")) #Stock price Today
price10 = float(input("Enter stock price 20 days ago: ")) #Stock price 5 trading days ago
price11 = float(input("Enter stock price 19 days ago: ")) #Stock price 4 trading days ago
price12 = float(input("Enter stock price 18 days ago: ")) #Stock price 3 trading days ago
price13 = float(input("Enter stock price 17 days ago: ")) #Stock price 2 trading days ago
price14 = float(input("Enter stock price 16 days ago: ")) #Stock price Today
price15 = float(input("Enter stock price 15 days ago: ")) #Stock price 5 trading days ago
price16 = float(input("Enter stock price 14 days ago: ")) #Stock price 4 trading days ago
price17 = float(input("Enter stock price 13 days ago: ")) #Stock price 3 trading days ago
price18 = float(input("Enter stock price 12 days ago: ")) #Stock price 2 trading days ago
price19 = float(input("Enter stock price 11 days ago ")) #Stock price Today
price20 = float(input("Enter stock price 10 days ago: ")) #Stock price 5 trading days ago
price21 = float(input("Enter stock price 9 days ago: ")) #Stock price 4 trading days ago
price22 = float(input("Enter stock price 8 days ago: ")) #Stock price 3 trading days ago
price23 = float(input("Enter stock price 7 days ago: ")) #Stock price 2 trading days ago
price24 = float(input("Enter stock price 6 days ago: ")) #Stock price Today
price25 = float(input("Enter stock price 5 days ago: ")) #Stock price 5 trading days ago
price26 = float(input("Enter stock price 4 days ago: ")) #Stock price 4 trading days ago
price27 = float(input("Enter stock price 3 days ago: ")) #Stock price 3 trading days ago
price28 = float(input("Enter stock price 2 days ago: ")) #Stock price 2 trading days ago
price29 = float(input("Enter stock price today: ")) #Stock price Today
#}
'''
Please do not modify the following code but feel free to view it on github at
https://github.com/vwallajabad/stock.prediction

Thanks,
-vwallajabad
'''
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

