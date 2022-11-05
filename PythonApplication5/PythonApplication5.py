import tkinter as tk
from PIL import ImageTk, Image
import random
import glob
from tkinter import *
import PIL.Image
import jsons
import requests
from tkinter import messagebox
from bitmap import BitMap
import datetime as dt
from time import strftime
import datetime

api_key = "1672d20ff231a862e381c9e5a78f8ab4"
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

class app(Frame):
    
    def __init__(self, mainwin, *args, **kvargs):
        super().__init__(*args, **kvargs)  

        self.pic_list = []
        self.main_color = "joy" 

        for name in glob.glob(r'C:\Users\user\source\repos\PythonApplication4\projektUMD\*'):
            val = name
            self.pic_list.append(val)

        self.pack(fill='both', expand=True)

        self.counter = 0

        self.mainwin = mainwin
        self.mainwin.title('Tkinter Picure Frame')
        self.mainwin.state('zoomed')

        self.mainwin.configure(bg = 'grey')
        self.frame = tk.Frame(mainwin)

        self.frame.place(relheight = 0.65, relwidth = 0.6, relx = 0.32, rely = 0.15)
                 #----------------------------------------------------------------------------------
               
        self.img = tk.Label(self.frame)
        self.img.grid(row = 0, column = 2, columnspan=2)
        self.img.pack(side = RIGHT)

        self.pic()

#------------------------------------------------------------------------------------------
        
        def selected():              
            if self.module.get() == 1:
                self.main_color = "energy"
                print("1")
            elif self.module.get() == 'calm':
                self.main_color = "calm"
            elif self.module.get() == 'joy':
                self.main_color = "joy"


        self.module = tk.StringVar(self.mainwin, "1")   


        self.values = {"no mood" : "1",        
                  "energy" : "2",
                  "calm" : "3",
                  "melancholy" : "4",
                  "joy" : "5"}

        for (text, value) in self.values.items():              
             tk.Radiobutton(self.mainwin, text = text, variable = self.module,
             value = value, command = selected()).pack(side = LEFT, ipady = 5)   
                                                                                 

#--------------------------------------------------------------------------------------------

        #self.radio_1 = tk.Radiobutton(self.mainwin, text='energy',
         #         variable=self.module, value='energy')

        #self.radio_2 = tk.Radiobutton(self.mainwin, text='calm',
          #        variable=self.module, value='calm')

        #self.radio_3 = tk.Radiobutton(self.mainwin, text='joy.',
         #         variable=self.module, value='joy')



#        self.btn = tk.Button(self.mainwin, text='Choose your mood: ', command = selected())

        #self.btn.pack(side = LEFT)
        #self.radio_1.pack(side = LEFT)
        #self.radio_2.pack(side = LEFT)
        #self.radio_3.pack(side = LEFT)

        #----------------------------------------------------------------------------------

        self.city_text = tk.StringVar() 
        self.city_entry = Entry(self, textvariable = self.city_text)
        self.city_entry.grid(row = 2, column = 1, columnspan=2)

        self.search_btn = Button(self, text = 'Search weather', width = 16, command = self.search) 
        self.search_btn.grid(row = 3, column = 1, columnspan=2)                                    

        self.location_lbl = Label(self, text = '', font = ('bold', 24)) 
        self.location_lbl.grid(row = 7, column = 1, columnspan=2)
        
        #img = PhotoImage(file = 'C:\\Users\\user\\OneDrive\\Pulpit\\ikony\\01n.png')
        #img_lbl = Label(app, image = img)
        #img_lbl.grid(row = 3, column = 2, columnspan=2)
        #image()

        self.date = dt.datetime.now() #widżet z datą
        self.data_lbl = Label(self, text=f"{self.date:%A, %B %d, %Y}", font="Calibri, 20")
        self.data_lbl.grid(row = 5, column = 1, columnspan = 2)

        self.my_font = ('times',35,'bold') 
        self.time_lbl = Label(self,font = self.my_font) 
        #bg='grey'
        self.time_lbl.grid(row = 6,column = 1)
        #padx=5,pady=25
        self.my_time() 

        self.temp_lbl = Label(self, text = '')
        self.temp_lbl.grid(row = 8, column = 1, columnspan=2)

        self.feels_like_lbl = Label(self, text = '') 
        self.feels_like_lbl.grid(row = 9, column = 1, columnspan=2)

        self.weather_lbl = Label(self, text = '', font = ('bold', 16)) 
        self.weather_lbl.grid(row = 10, column = 1, columnspan=2)

        self.descrp_lbl = Label(self, text = '') 
        self.descrp_lbl.grid(row = 11, column = 1, columnspan=2)

        self.humidity_lbl = Label(self, text = '') 
        self.humidity_lbl.grid(row = 12, column = 1, columnspan=2)

        self.clouds_lbl = Label(self, text = '') 
        self.clouds_lbl.grid(row = 13, column = 1, columnspan = 2)

        self.wind_lbl = Label(self, text = '') 
        self.wind_lbl.grid(row = 14, column = 1, columnspan = 2)

        self.sunrise_lbl = Label(self, text = '') 
        self.sunrise_lbl.grid(row = 15, column = 1, columnspan=2)

        self.sunset_lbl = Label(self, text = '') 
        self.sunset_lbl.grid(row = 16, column = 1, columnspan=2)


#--------------------------------------------------------------------------------
        

    def color_filter(self, img):
        width, height = img.size

        r_total = 0
        g_total = 0
        b_total = 0

        count = 0
        for x in range(0, width):
            for y in range(0, height):
                r, g, b = img.getpixel((x,y))
                r_total += r
                g_total += g
                b_total += b
                count += 1
        r_total = r_total/(width*height)
        g_total = g_total/(width*height)
        b_total = b_total/(width*height)
#---------------------------------------------------------------------------------

        
        if(r_total <= 255 and r_total >= 125 and g_total <= 170 and b_total <= 80):
           return "energy"

        if(r_total <= 125 and g_total <=255 and g_total >= 110 and b_total <=125):
           return "calm"

        if(r_total <= 255 and r_total >= 220 and g_total <=255 and g_total >= 125 and b_total <= 80):
           return "joy"

        if(r_total <= 100 and g_total <= 140 and b_total <=255 and b_total >= 120):
           return "melancholy"

#-----------------------------------------------------------------------------------

        #if(max(r_total, g_total, b_total)==r_total):
         #   return "red"
        #if(max(r_total, g_total, b_total)==g_total):
         #   return "green"
        #if(max(r_total, g_total, b_total)==b_total):
            #return "blue"
#-----------------------------------------------------------

    def pic(self):

        if self.counter == len(self.pic_list) - 1:
            self.counter = 0
        else:
            self.counter = self.counter + 1

        self.file = self.pic_list[self.counter]
        if(self.color_filter(PIL.Image.open(self.file).resize((50,50))) == self.main_color or self.main_color == "no mood"): 
            self.load = PIL.Image.open(self.file)

            self.pic_width = self.load.size[0]
            self.pic_height = self.load.size[1]

            self.real_aspect = self.pic_width/self.pic_height

            self.cal_width = int(self.real_aspect * 500)

            self.load2 = self.load.resize((self.cal_width, 500))
            self.render = ImageTk.PhotoImage(self.load2)
            self.img.config(image = self.render)
            self.img.image = self.render
            root.after(2000, self.pic) 

        else:
            self.pic()

    def my_time(self):
        time_string = strftime('%H:%M:%S %p') 
        self.time_lbl.config(text = time_string)
        self.time_lbl.after(1000, self.my_time) 


    def get_weather(self, city):
        result = requests.get(url.format(city, api_key))
        if result:
            json = result.json()
            city = json['name']
            country = json['sys']['country']
            temp_Kelvin = json['main']['temp']
            temp_Cel = temp_Kelvin - 273.15
            icon = json['weather'][0]['icon']
            weather = json['weather'][0]['main']
            description = json['weather'][0]['description']          
            feels_like = json['main']['feels_like'] - 273.15
            sunrise_unix = json['sys']['sunrise']
            sunrise = datetime.datetime.fromtimestamp(sunrise_unix)
            sunset_unix = json['sys']['sunset']
            sunset = datetime.datetime.fromtimestamp(sunset_unix)
            humidity = json['main']['humidity']
            clouds = json['clouds']['all']
            wind = json['wind']['speed']
            final = (city, country, temp_Cel, feels_like, icon, weather, description, humidity, sunrise, sunset, clouds, wind)
            return final
        else:
            return None


    def search(self):
        city = self.city_text.get()
        weather = self.get_weather(city)
        if weather: 
            self.location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
            #img_lbl['image'] = PhotoImage(Image.open('C:\\Users\\user\\OneDrive\\Pulpit\\ikony\\{}.png'.format(weather[4])))
            #img_lbl.config(image=PhotoImage(Image.open('C:\\Users\\user\\OneDrive\\Pulpit\\ikony\\{}.png'.format(weather[4]))))
            #print('C:\\Users\\user\\OneDrive\\Pulpit\ikony\\{}.png'.format(weather[4]))
            self.temp_lbl['text'] = 'Temperature:      {:.1f}°C'.format(weather[2])
            self.weather_lbl['text'] = weather[5]
            self.feels_like_lbl['text'] = 'Feels like temp:      {:.1f}°C'.format(weather[3])
            self.descrp_lbl['text'] = '{}'.format(weather[6])
            self.humidity_lbl['text'] = 'Humidity:      {}%'.format(weather[7])
            self.sunrise_lbl['text'] = 'Sunrise:       {}'.format(weather[8])
            self.sunset_lbl['text'] = 'Sunset:        {}'.format(weather[9])
            self.clouds_lbl['text'] = 'Clouds:       {}%'.format(weather[10])
            self.wind_lbl['text'] = 'Wind speed:     {} m/s'.format(weather[11])
            #image()
        else:
            messagebox.showerror('Error', 'City not found') 

#-------------------------------------------------------------------------------------------------

root = tk.Tk()

#img = ImageTk.PhotoImage(Image.open('C:\\Users\\user\\source\\repos\\PythonApplication4\\projektUMD\\1.jpg'))
myprog = app(root)

root.mainloop()


#img = ImageTk.PhotoImage(Image.open('C:\\Users\\user\\source\\repos\\PythonApplication4\\projektUMD\\1.jpg'))

