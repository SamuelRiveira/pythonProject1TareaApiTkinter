from tkinter import  ttk
import tkinter as tk
from PIL import Image, ImageTk

import requests
from PIL.ImageOps import expand

from dataclass_wizard import fromdict
from models.apiResponse import APIResponse

print("CARGANDO")

# API
response = requests.get("https://dummyjson.com/products")
body = response.json()
api_response = fromdict(APIResponse, body)

indice = 6

# Load Imagen from url
def load_image(url, size=(300, 300)):
    response_img = requests.get(url, stream=True)
    img = Image.open(response_img.raw).resize(size)
    response_img.close()
    return ImageTk.PhotoImage(img)

def siguiente():
    global indice
    indice += 1

def anterior():
    global indice
    if indice > 0:
        indice -= 1

# Create root
root = tk.Tk()
root.resizable(False, False)
root.title("Productos")

# Main Frame
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Image frame
image_frame = ttk.Frame(main_frame)
image_frame.grid(row=0, column=0, sticky=(tk.W, tk.N), padx=(0, 10))

# Thumbnail
thumbnail = load_image(api_response.products[indice].thumbnail)
thumbnail_label = ttk.Label(image_frame, image=thumbnail)
thumbnail_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

# Images
additional_images = []
for i, image in enumerate(api_response.products[indice].images):
    img = load_image(image, size=(100, 100))
    additional_images.append(img)
    img_label = ttk.Label(image_frame, image=img)
    img_label.grid(row=1, column=i, padx=2)

# Info frame
info_frame = ttk.Frame(main_frame)
info_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

# Title
ttk.Label(info_frame, text=api_response.products[indice].title, font=("Helvetica", 16, "bold")).grid(row=0, column=0, sticky=tk.W)

# Description
ttk.Label(info_frame, text=api_response.products[indice].description, wraplength=400).grid(row=1, column=0, pady=(0, 10), sticky=tk.W)

# Price and discount
price_frame = ttk.Frame(info_frame)
price_frame.grid(row=2, column=0, sticky=tk.W)
ttk.Label(price_frame, text=f"${api_response.products[indice].price:.2f}", font=("Helvetica", 14, "bold")).grid(row=0, column=0)
if api_response.products[indice].discountPercentage > 0:
    ttk.Label(price_frame, text=f"({api_response.products[indice].discountPercentage}% off)", foreground="green").grid(row=0, column=1, padx=(5, 0))

# Category and stock
ttk.Label(info_frame, text=f"Category: {api_response.products[indice].category}").grid(row=3, column=0, sticky=tk.W)
ttk.Label(info_frame, text=f"In Stock: {api_response.products[indice].stock}").grid(row=4, column=0, sticky=tk.W)

# Tags
tags_frame = ttk.Frame(info_frame)
tags_frame.grid(row=5, column=0, sticky=tk.W, pady=(5, 0))
for i, tag in enumerate(api_response.products[indice].tags):
    ttk.Label(tags_frame, text=tag, background="lightgray", padding=(5, 2)).grid(row=0, column=i, padx=(0, 5))

# Dimensions
dimensions = api_response.products[indice].dimensions
ttk.Label(info_frame, text=f"Dimensions: {api_response.products[indice].dimensions.width}W x {api_response.products[indice].dimensions.height}H x {api_response.products[indice].dimensions.depth}D").grid(row=6, column=0, sticky=tk.W, pady=(10, 0))

# Availability, minimum order, and return policy
ttk.Label(info_frame, text=f"Availability: {api_response.products[indice].availabilityStatus}").grid(row=7, column=0, sticky=tk.W)
ttk.Label(info_frame, text=f"Minimum Order: {api_response.products[indice].minimumOrderQuantity}").grid(row=8, column=0, sticky=tk.W)
ttk.Label(info_frame, text=f"Return Policy: {api_response.products[indice].returnPolicy}").grid(row=9, column=0, sticky=tk.W)

# Buttons frame
buttons_frame = ttk.Frame(main_frame)
buttons_frame.grid(row=2, column=0, columnspan=2, pady=(10, 0))
ttk.Button(buttons_frame, text="Anterior", command=anterior).grid(row=0, column=0, padx=10)
ttk.Button(buttons_frame, text="Siguiente", command=siguiente).grid(row=0, column=1, padx=10)

print("CARGADO")
root.mainloop()