import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import ttk
import lxml

url = "https://www.pricecharting.com/console/pokemon-promo"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

Card_Names = [item.text.strip() for item in soup.find_all('td', class_ = 'title')]

Prices_PSA10 =  [item.text.strip() for item in soup.find_all('td', class_ = 'price numeric new_price')]

Prices_PSA9 = [item.text.strip() for item in soup.find_all('td', class_ = 'price numeric cib_price')]

Prices_Ungraded = [item.text.strip() for item in soup.find_all('td', class_ = 'price numeric used_price')]

data = {
        
        'Card_Names' : Card_Names,
        
        'Prices_Ungraded' : Prices_Ungraded,
        
        'Prices_PSA9' : Prices_PSA9,
        
        'Prices_PSA10' : Prices_PSA10

        }

df = pd.DataFrame(data)

root = tk.Tk()
root.title("Dataframe CardPrices")

icon_path = 'icon.ico'
root.iconphoto(False, tk.PhotoImage(file=icon_path))

tree = ttk.Treeview(root)
tree.pack(fill=tk.BOTH, expand=True)

tree["columns"] = list(df.columns)
tree["show"] = "headings"

for column in df.columns:
    tree.heading(column, text=column)

for index, row in df.iterrows():
    tree.insert("", "end", values=list(row))

root.mainloop()