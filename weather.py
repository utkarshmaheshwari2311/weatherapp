from tkinter import messagebox, Label, Button, FALSE, Tk, Entry
from tkinter import *
import requests
def find_weather():
    api_address = 'http://api.openweathermap.org/data/2.5/weather?'
    ident = '&appid=4a369a065de8228621bc21e706654d81'
    city = city_name.get()
    url = api_address + 'q=' + city + ident
    json_data = requests.get(url).json()
    print(json_data)
    
window = Tk()
window.resizable(width=FALSE, height=FALSE)
window.title("WEATHER APP")
window.geometry("300x200")

cityname_text = Label(window, text="CITY NAME:")
city_name = Entry(window)
city_name.place(x=80,y=180)
search = Button(text="current_weather", command=find_weather)
search.place(x=100,y=100)

cityname_text.pack()
city_name.pack()
search.pack()
window.mainloop()
