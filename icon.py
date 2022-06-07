import requests
import json
from Tkinter import *
import io
from PIL import Image, ImageTk
import requests
	
weather_data =requests.get('https://api.openweathermap.org/data/2.5/weather?q=Baku&appid=8b5e6c4eeafce928c354244cf1230eb4&units=metric').json()

list = ['clouds', 'name', 'weather', 'main', 'wind']


dict = {}
for i in weather_data:
	if i in list:
		dict[i] = weather_data[i]
		
iconurl = 'http://openweathermap.org/img/wn/' + dict['weather'][0]['icon'] +'@2x.png'		

#print(dict['main']['temp'])

icon = requests.get(iconurl)
icon_bytes = io.BytesIO(icon.content)

img = Image.open(icon_bytes)
image = ImageTk.PhotoImage(img)


root = Tk()
root.geometry('200x200')

label = Label(root, image = image)
label.pack()

root.mainloop()
