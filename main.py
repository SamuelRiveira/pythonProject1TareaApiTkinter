from tkinter.ttk import Label
import requests
import tkinter as tk
from dataclass_wizard import fromdict
from models.apiResponse import APIResponse

response = requests.get("https://dummyjson.com/products")

body = response.json()

api_response = fromdict(APIResponse, body)

root = tk.Tk()
root.resizable(False, False)
root.title("Productos")

l1 = Label(root, text = "Titulos")
l1.grid(row = 0, column = 0, pady = 2)

indice = 1
for product in api_response.products:
    titulos = Label(root, text = product.title)
    titulos.grid(row = indice, column = 0, pady = 2)

    indice += 1
root.mainloop()