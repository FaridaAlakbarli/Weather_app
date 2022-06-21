import requests
import json
from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk
from datetime import datetime
from pytz import timezone, country_timezones


root = Tk()
root.geometry('300x250')
root.title('Current weather')



label1 = Label(root, text = 'loading', bd = 10, bg = '#baf0f7', font = ('Arial', 20))
label1.grid(row=0, column=0)
			
label2 = Label(root, text = 'loading', bd = 5)
label2.grid(row=1, column=0)

label3 = Label(root, text = 'loading', bd = 5)
label3.grid(row=1, column=1)

label4 = Label(root, text = 'loading', bd = 5)
label4.grid(row=2, column=1, columnspan = 2)

label5 = Label(root)
label5.grid(row = 0, column = 1)

label6 = Label(root, text = 'Enter location: ')
label6.grid(row = 6, column = 0)

label7 = Label(root)
label7.grid(row = 2, column =1)

label_time = Label(root)
label_time.grid(row = 8, column = 0)

var = StringVar()
entry = Entry(root, textvariable = var)
entry.grid(row = 6, column = 1)

def get_from_file():
	with open ('weather.txt', 'r') as f:
		try:
			f1 = f.readline()
			dict1 = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid=8b5e6c4eeafce928c354244cf1230eb4&units=metric'.format(f1)).json()
				 

			iconurl1 = 'http://openweathermap.org/img/wn/' + dict1['weather'][0]['icon'] +'@2x.png'	
					
			response1 = requests.get(iconurl1)
			img1 = Image.open(BytesIO(response1.content)).resize((40, 40))
			img21 = ImageTk.PhotoImage(img1)
			
			country = country_timezones(dict1['sys']['country'])
			
			time_now = datetime.now()
			
			time_there = time_now.astimezone(timezone(country[0]))
			
			format = "%Y-%m-%d %H:%M:%S"
					
			label1.config(text = dict1['name'])
			
			label2.config(text = str(dict1['main']['temp']) + ' Celcius')
				
			label3.config(text = dict1['weather'][0]['description'])

			label4.config(text = 'wind: ' + str(dict1['wind']['speed']) + 'm/h')
				
			label5['image'] = img21
			
			label_time.config(text = time_there.strftime(format))
			
			f.close()
			
			root.after(500, get_from_file)
				
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
		
		country = country_timezones(dict['sys']['country'])
			
		time_now = datetime.now()
		
		global time_there1
		global format1
			
		time_there1 = time_now.astimezone(timezone(country[0]))
			
		format1 = "%Y-%m-%d %H:%M:%S"
		
		
		update_data()	

	except:
		show_error()

    
def update_data():
	label1.config(text = dict['name'])
	
	label2.config(text = str(dict['main']['temp']) + 'Celcius')
	
	label3.config(text = dict['weather'][0]['description'])
	
	label4.config(text = 'wind: ' + str(dict['wind']['speed']) + 'm/h')
	
	label5.config(image = img2)
	
	label7.config(text = '')
	
	label_time.config(text = time_there1.strftime(format1))
    
def show_error():
	label1.config(text = '')
	label1.config(bg= '#d9d9d9')
	
	label2.config(text = '')

	label3.config(text = '')

	label4.config(text = '')
	
	label5.config(image = '')
	
	label_time.config(text = '')
	
	label7.config(text = 'Check your connection or spelling')
	
dots_label = Label(root)
dots_label.grid(row = 7, column = 1)
	
dots =''
def dot():
	global dots
	dots = dots + '.'
	dots_label.config(text = dots)
	if len(dots) == 3:
		dots = ''
	
	
	
		
def loop_work():
	get_data
	dot()
	root.after(500, loop_work)
	
	
	
entry.bind('<Return>', get_data)

get_from_file()
loop_work()


root.mainloop()

