import requests
import json
from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk


root = Tk()
root.geometry('400x200')
root.title('Weather')

var1 = StringVar(value = 'loading')	 
var2 = StringVar(value = 'loading')	
var3 = StringVar(value = 'loading')	
var4 = StringVar(value = 'loading')	



label1 = Label(root, textvariable = var1, bd = 10, bg = '#baf0f7', font = ('Arial', 20))
label1.grid(row=0, column=0)
			
label2 = Label(root, textvariable = var2, padx = 15, bd = 5)
label2.grid(row=1, column=0)

label3 = Label(root, textvariable = var3, bd = 5)
label3.grid(row=1, column=2)

label4 = Label(root, textvariable = var4, padx = 15, bd = 5)
label4.grid(row=2, column=2)

label5 = Label(root)
label5.grid(row = 0, column = 2)

label = Label(root, text = 'Enter location: ')
label.grid(row = 4, column = 0)

var = StringVar()
entry = Entry(root, textvariable = var)
entry.grid(row = 4, column = 1)

with open ('weather.txt', 'r') as f:
	try:
		f1 = f.readline()
		dict1 = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid=8b5e6c4eeafce928c354244cf1230eb4&units=metric'.format(f1)).json()
		 

		iconurl1 = 'http://openweathermap.org/img/wn/' + dict1['weather'][0]['icon'] +'@2x.png'	
			
		response1 = requests.get(iconurl1)
		img1 = Image.open(BytesIO(response1.content)).resize((40, 40))
		img21 = ImageTk.PhotoImage(img1)
			
		label1['textvariable'] = var1.set(dict1['name'])
		
		label2['textvariable'] = var2.set(str(dict1['main']['temp']) + 'Celcius')
		
		label3['textvariable'] = var3.set(dict1['weather'][0]['description'])

		label4['textvariable'] = var4.set('wind: ' + str(dict1['wind']['speed']) + 'm/h')
		
		label5['image'] = img21
		f.close()
	except KeyError:
		pass


	
def get_data(event):
	try:
		string = entry.get()
		with open('weather.txt', 'w') as fil:
			fil.write(string)
			fil.close()
		entry.delete(0,len(string))
	
		global dict
		dict = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid=8b5e6c4eeafce928c354244cf1230eb4&units=metric'.format(string)).json()
	 
		iconurl = 'http://openweathermap.org/img/wn/' + dict['weather'][0]['icon'] +'@2x.png'	
		global img2
		
		response = requests.get(iconurl)
		img = Image.open(BytesIO(response.content)).resize((40, 40))
		img2 = ImageTk.PhotoImage(img)
		
			
		update_data()	
			
	except:
		print('aaszm')
		show_error()

    
def update_data():
	label1['textvariable'] = var1.set(dict['name'])
	
	label2['textvariable'] = var2.set(str(dict['main']['temp']) + 'Celcius')
	
	label3['textvariable'] = var3.set(dict['weather'][0]['description'])
	
	label4['textvariable'] = var4.set('wind: ' + str(dict['wind']['speed']) + 'm/h')
	
	label5['image'] = img2
    
def show_error():
	label1['textvariable'] = var1.set('Zay Zay')

	label2['textvariable'] = var2.set('Zart Zort Celcius')

	label3['textvariable'] = var3.set('Neterseng qadang alem')

	label4['textvariable'] = var4.set('Niye bele oluuuur ? m/h')
	
	
entry.bind('<Return>', get_data)


root.mainloop()

