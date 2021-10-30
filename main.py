from tkinter import *
import json
import requests
import time

window = Tk()
window.title('Weather Information')
window.geometry('600x100')
window.iconbitmap(r'C:\Users\example\OneDrive\Desktop\cloudicon.ico')


def get_weather_info():
    city = text.get()
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city +'&appid=ENTER_YOUR_API_KEY_HERE'
    response = requests.request("GET", url)
    data = json.loads(response.text)

    code = data['cod']

    if code == 200:
        main_weather = data['weather'][0]['main']
        description_weather = data['weather'][0]['description']
        real_temp_weather = round((data['main']['temp']) - 273)
        feels_like_temp_weather = round((data['main']['feels_like']) - 273)

        weather_msg = f'{city} is currently {real_temp_weather}C and feels like {feels_like_temp_weather}C. \nYou will be experiencing {description_weather}.'
        output_text.set(weather_msg)
    else:
        output_text.set('Invalid city')

def change_unit_c():
    city = text.get()
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city +'&appid=ENTER_YOUR_API_KEY_HERE'
    response = requests.request("GET", url)
    data = json.loads(response.text)

    code = data['cod']

    if code == 200:
        main_weather = data['weather'][0]['main']
        description_weather = data['weather'][0]['description']
        real_temp_weather = round((data['main']['temp']) - 273)
        feels_like_temp_weather = round((data['main']['feels_like']) - 273)

        weather_msg = f'{city} is currently {real_temp_weather}C and feels like {feels_like_temp_weather}C. \nYou will be experiencing {description_weather}.'
        output_text.set(weather_msg)
    else:
        output_text.set('Invalid city')


def change_unit_f():
    city = text.get()
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=ENTER_YOUR_API_KEY_HERE'
    response = requests.request("GET", url)
    data = json.loads(response.text)

    code = data['cod']

    if code == 200:
        main_weather = data['weather'][0]['main']
        description_weather = data['weather'][0]['description']
        real_temp_weather = ((round((data['main']['temp']) - 273))*(9/5)) + 32
        feels_like_temp_weather = ((round((data['main']['feels_like']) - 273))*(9/5)) + 32

        weather_msg = f'{city} is currently {real_temp_weather}F and feels like {feels_like_temp_weather}F. \nYou will be experiencing {description_weather}.'
        output_text.set(weather_msg)
    else:
        output_text.set('Invalid city')


label = Label(window, text='Enter City:')
label.grid(column=0, row=0, sticky=W)

#User input
text = Entry(window, width=30)
text.grid(column=1, row=0, sticky=E)

#create button
button1 = Button(window, text='Get Information', command=get_weather_info)
button1.grid(column=2, row=0, sticky=E)

#create button for C
button2 = Button(window, text='C', command=change_unit_c)
button2.grid(column=3, row=0, sticky=E)

#create button for F
button3 = Button(window, text='F', command=change_unit_f)
button3.grid(column=4, row=0, sticky=E)

#Display output
output_text = StringVar()
label_output = Label(window, textvariable=output_text)
label_output.grid(column=0, columnspan=4, row=2, sticky=W)

window.mainloop()
