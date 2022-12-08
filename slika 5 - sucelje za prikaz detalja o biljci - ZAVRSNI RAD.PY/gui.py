from crud import get_all_users
from datetime_utils import *
from weather_api import WeatherForecast
from main import session
from tkinter.ttk import Entry
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from random import randint
from biljka import *
from posuda import *

lista_posuda = []
lista_biljaka = []
preporuke = ['supstrat 1', 'supstrat 2', 'supstrat 3', 'supstrat 4']

root = tk.Tk()
root.title('Algebra | PyPosuda')
root.configure(bg='#282828') # tamno siva pozadina

root.geometry('700x500')


frame = tk.Frame(root, width=600, height=400)
frame.grid(column=0, row=0, padx=10, pady=5)
frame.place(anchor='e', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open('slika_1.jpg'))
label = tk.Label(frame, image=img)
label.grid(column=0, row=1, padx=10, pady=10)


sync_image = tk.Button(root, text='Sync' ,bg='#282828', fg='white',font=('Arial', 10))
sync_image.grid(column=2, row=5, padx=5, pady=5)

moj_profil_image = tk.Button(root, text='Moj profil' ,bg='#282828', fg='white',font=('Arial', 10), command=lambda: moj_profil_clicked())
moj_profil_image.grid(column=2, row=6, padx=5, pady=5)

vrijednost_senzora = tk.LabelFrame (root, width=300, height=300, text='Vrijednost', bg='#282828', fg='white',font=('Arial', 10)) #Frame
vrijednost_senzora.grid(column=3, row=3, columnspan=15, padx=15, pady=15)
vrijednost_senzora.place(anchor='nw',relx=0.5, rely=0.5)


zaljevanje =[
    ('1', ' treba zaliti'),
    ('2', 'ne treba zaliti')    
]

def refresh_values():
    vlaznost_i_tempratura.configure(text="Hi")

voda = tk.StringVar()
voda.set('da')

for text, zaliti in zaljevanje:
    tk.Radiobutton(vrijednost_senzora, text=text, variable=voda, value=zaljevanje, bg="#282828", fg="white",font=("Arial", 10)).pack(anchor='w') #ancor centrira na lijevo

my_button = tk.Button(vrijednost_senzora, text='Dodati vode',bg='#282828', fg='white',font=('Arial', 10))
my_button.pack()

vlaznost_i_tempratura = tk.LabelFrame(
    root, width=300, height=300, text='Temperatura zraka i vlažnost:', bg='#282828', fg='white', font=('Arial', 10))
vlaznost_i_tempratura.grid(column=0, row=1, columnspan=15, padx=15, pady=15)
vlaznost_i_tempratura.place(anchor='nw', relx=0.5, rely=0.5)

lux_i_ph = tk.LabelFrame(root, width=400, height=200, text='PH vrijednost i LUX vrijednost:',
                         bg='#282828', fg='white', font=('Arial', 10))
lux_i_ph.grid(column=0, row=2, columnspan=15, padx=10, pady=10)
lux_i_ph.place(anchor='nw', relx=0.5, rely=0.65)





def create_weather_frame():
    weather_frame = tk.Frame(
        vlaznost_i_tempratura, width=200, height=100, bg='#282828'
    )
    weather_frame.grid(row=0, column=2, padx=10, pady=10)

    ph_lux_frame = tk.Frame(
        lux_i_ph, width=400, height=200, bg='#282828'
    )
    ph_lux_frame.grid(row=2, column=2, padx=10, pady=10)

    def refresh_temperature():
        zagreb_forecast = WeatherForecast("zagreb")
        temperature_data = zagreb_forecast.get_formatted_weather_data()

        temperature_label.configure(
            text=f"{temperature_data['current_temperature']} °C ({temperature_data['description']})")
        humidity_label.configure(text=temperature_data['humidity'])

    def random_ph_label():
        return f"pH vrijednost: {np.random.randint(5, 10)} "

    def random_lux_label():
        return f"Razina svjetla: {np.random.randint(700, 1200)} "

    temperature_label = tk.Label(
        weather_frame, bg='#282828', fg='white', text="", font=('Arial', 10)
    )
    temperature_label.grid(row=2, column=3, padx=5, pady=5)

    humidity_label = tk.Label(
        weather_frame, bg='#282828', fg='white', text="", font=('Arial', 10)
    )
    humidity_label.grid(row=2, column=4, padx=5, pady=5)

    ph_label = tk.Label(
        ph_lux_frame, bg='#282828', fg='white', text=random_ph_label(), font=('Arial', 10)
    )
    ph_label.grid(row=1, column=5, padx=5, pady=5)

    lux_label = tk.Label(
        ph_lux_frame, bg='#282828', fg='white', text=random_lux_label(), font=('Arial', 10)
    )
    lux_label.grid(row=2, column=5, padx=5, pady=5)

    last_refresh_label = tk.Label(
        weather_frame, bg='#282828', fg='white', text="", font=('Arial', 10)
    )
    last_refresh_label.grid(row=2, column=5, padx=5, pady=5)

    refresh_temperature()

    ph_label = tk.Label(
        weather_frame, bg='#282828', fg='white', text="", font=('Arial', 10)
    )
    ph_label.grid(row=2, column=5, padx=5, pady=5)

    lux_label = tk.Label(
        weather_frame, bg='#282828', fg='white', text="", font=('Arial', 10)
    )
    lux_label.grid(row=2, column=5, padx=5, pady=5)





create_weather_frame()

root.mainloop()

