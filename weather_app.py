import requests
import json
from tkinter import *
from time import time, ctime


list = ['clouds', 'name', 'weather', 'main', 'wind']


dict = {}


root = Tk()
root.geometry('300x200')

	
def get_data():
	try:
		weather_data =requests.get('https://api.openweathermap.org/data/2.5/weather?q=Baku&appid=8b5e6c4eeafce928c354244cf1230eb4&units=metric').json()
	 
		for i in list:
			dict[i] = weather_data[i]
			
		root.after(500, update_data)	
			
	except:
		print('aaszm')
		show_error()

var1 = StringVar(value = 'loading')	 
var2 = StringVar(value = 'loading')	
var3 = StringVar(value = 'loading')	
var4 = StringVar(value = 'loading')	

label1 = Label(root, textvariable = var1, bd = 10, bg = '#baf0f7', font = ('Arial', 20))
label1.grid(row=0, column=0)
			
label2 = Label(root, textvariable = var2, padx = 15, bd = 5)
label2.grid(row=1, column=0)

label3 = Label(root, textvariable = var3, bd = 5)
label3.grid(row=0, column=2)

label4 = Label(root, textvariable = var4, padx = 15, bd = 5)
label4.grid(row=2, column=2)
    
'''def show_data():	
    label1.configure(text = dict['name'])

    label2.configure(text = str(dict['main']['temp']) + ' Celcius')

    label3.configure(text = dict['weather'][0]['description'])

    label4.configure(text = 'wind: ' + str(dict['wind']['speed']) + 'm/h')'''
    
def update_data():
	label1['textvariable'] = var1.set(dict['name'])
	
	label2['textvariable'] = var2.set(str(dict['main']['temp']) + 'Celcius')
	
	label3['textvariable'] = var3.set(dict['weather'][0]['description'])
	
	label4['textvariable'] = var4.set('wind: ' + str(dict['wind']['speed']) + 'm/h')
    
def show_error():
	label1.configure(text = 'Zay Zay')

	label2.configure(text = 'Zart Zort Celcius')

	label3.configure(text = 'Neterseng qadang alem')

	label4.configure(text = 'wind: Niye bele oluuuur ? m/h')
	
	
	
get_data()


root.mainloop()
