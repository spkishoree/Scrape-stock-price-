import bs4 as bs
import requests
import datetime, time
import tkinter as tk
def getStockPrice():
    resp = requests.get('https://www.icicidirect.com/equity/stockpricequote/nse/jubilant-ingrev/75293')
    #resp = requests.get('https://www.timeanddate.com/')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    #stock_price = soup.findAll('span', {'id': 'ij0'})[0].string
    stock_price = float(soup.findAll('h2',{'id': 'eqIdxLTP'})[0].string)
    print(stock_price)
    price_lable['text'] = stock_price
    if int(stock_price) < 770:
        price_lable["fg"] = 'red'
    elif int(stock_price) > 795:
        price_lable["fg"] = 'green'
    else:
        price_lable["fg"] = 'blue'
    price_lable.after(1,getStockPrice)
    return stock_price


price = tk.Tk()
price.title("jubilantingrevia stock price")
price_lable = tk.Label(price,font='ariel 60',bg="black")
price_lable.grid(row=0,column=0)
stock_price = getStockPrice()
price.mainloop()
