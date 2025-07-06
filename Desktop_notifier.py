import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk

BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"

# Function to fetch weather data from OpenWeatherMap
def get_weather(city_name):
    params = {
        'q': city_name,
        'units': 'metric',
        'appid': '3a989c89fbf66cf73f20ce7416d8b102'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

def show_notification(weather_data):
    description = weather_data['list'][0]['weather'][0]['description']
    temperature = weather_data['list'][0]['main']['temp']
    city = weather_data['city']['name']
    message = f"Weather in {city}: {description}, Temperature: {temperature}°C"
    messagebox.showinfo("Weather Notification", message)

def reset_input():
    city_entry.delete(0, tk.END)

# Load the background image

# GUI setup
root = tk.Tk()

root.geometry("600x400")
root.title("Desktop Weather Notifier")
root.resizable(False, False)
background_image = Image.open("C:/S.jpg")
background_image_tk = ImageTk.PhotoImage(background_image)

# Create a Label widget to display the background image
background_label = tk.Label(root, image=background_image_tk)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Function for the Get Weather button
def fetch_weather():
    city_name = city_entry.get()
    if city_name:
        try:
            weather_data = get_weather(city_name)
            show_notification(weather_data)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.", font=("Helvetica", 20, "bold"))

# Create labels and buttons
parent_bg_color = root.cget("bg")

city_label = tk.Label(root, text="Enter City:", font=("Helvetica", 20, "bold"),
                      bg=parent_bg_color, bd=0, highlightthickness=0)
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=40, font=("Helvetica", 14), justify="center")
city_entry.pack(pady=(0, 20))

get_weather_button = tk.Button(root, text="Enter", command=fetch_weather,
                               bg=parent_bg_color, bd=0, highlightthickness=0,font=("Helvetica", 10, "bold"))
get_weather_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_input,
                         bg=parent_bg_color, bd=0, highlightthickness=0,font=("Helvetica", 10, "bold"))
reset_button.pack(pady=20)

quit_button = tk.Button(root, text="Quit", command=root.quit,
                        bg=parent_bg_color, bd=0, highlightthickness=0,font=("Helvetica", 10, "bold"))
quit_button.pack()

# Run the GUI event loop
root.mainloop()