
from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz
import os

root = Tk()
root.title("Phone Number Tracker")
root.geometry("365x584+300+100")
root.resizable(False, False)
entry_widget_text = "input sample: +23412345678"

def Track():
    enter_number = entry.get()
    number = phonenumbers.parse(enter_number)
    valid = phonenumbers.is_valid_number(number)
    if valid is True:
        #country
        locate = geocoder.description_for_number(number, 'en')
        country.config(text=locate)

        #operator like airtel, mtn
        operator = carrier.name_for_number(number, 'en')
        sim.config(text=operator)

        #phone timezone
        time = timezone.time_zones_for_number(number)
        zone.config(text=time[0])

        #longitude and latitude
        geolocator = Nominatim(user_agent="myGeocoder")
        location = geolocator.geocode(locate)
        lng = location.longitude
        lat = location.latitude
        longitude.config(text=lng)
        latitude.config(text=lat)

        #time showing in phone
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(result)
        home = pytz.timezone(result)
        print(home)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
    else:
        not_valid = "Please enter the correct number using country code e.g. +2348088888888 for Nigeria"
        # input_check_reply(not_valid)
        response_message.config(text=not_valid)
        response_window.deiconify()

def on_entry_click(event):
    """Function to handle when the user clicks on the input field."""
    if enter_number.get() == entry_widget_text:
        # it Clears the input field and set the text color to black
        enter_number.delete(0, END)
        enter_number.config(fg="black")

# Hides the response window
def hide_response():
    response_window.withdraw()

# Create a warning message widget for the response
response_window = Toplevel(root)
response_window.geometry("300x200+320+150")  # Set the size and position of the window
response_message = Message(response_window, text="", width=250, font=("Helvetica", 14), fg="white", bg="red")
response_message.place(relx=0.5, rely=0.5, anchor="center")
hide_button = Button(response_window, text="OK", command=hide_response)
hide_button.place(relx=0.5, rely=0.8, anchor="center")
response_window.withdraw()  # Hide the response window initially

#setting path for all images used
local_dir = os.path.dirname(__file__)
icon_path = os.path.join(local_dir, 'logo image.png')
logo_path = os.path.join(local_dir, 'logo image.png')
search_path = os.path.join(local_dir, 'search png.png')
bottom_box_path = os.path.join(local_dir, 'bottom png.png')
search_image_path = os.path.join(local_dir, 'search.png')

#icon image
icon = PhotoImage(file = icon_path)
root.iconphoto(False, icon)

#logo
logo = PhotoImage(file = logo_path)
Label(root, image=logo).place(x=240, y=70)

Eback = PhotoImage(file = search_path)
Label(root, image=Eback).place(x=20, y=190)

#heading
Heading = Label(root, text = "TRACK NUMBER", font = ('arial', 15, 'bold'))
Heading.place(x=90, y=110)

#bottom box
Box = PhotoImage(file = bottom_box_path)
Label(root, image=Box).place(x=-2, y=355)

#entry
entry = StringVar()
enter_number = Entry(root, fg="gray", textvariable=entry, width=25, justify="center", bd=0, font=("arial", 15))
enter_number.insert(0, entry_widget_text)
enter_number.bind("<FocusIn>", on_entry_click)
enter_number.pack()
enter_number.place(x=50, y=230)

#search button
Search_image = PhotoImage(file = search_image_path)
search = Button(root, image=Search_image, borderwidth=0, cursor="hand2", bd=0, command=Track)
search.place(x=35, y=300)

#label
country=Label(root, text="Country:", bg="#57adff", fg="black", font=("arial", 10, 'bold'))
country.place(x=50, y=400)

sim=Label(root, text="SIM:", bg="#57adff", fg="black", font=("arial", 10, 'bold'))
sim.place(x=200, y=400)

zone=Label(root, text="TimeZone:", bg="#57adff", fg="black", font=("arial", 10, 'bold'))
zone.place(x=50, y=450)

clock=Label(root, text="Phone Time:", bg="#57adff", fg="black", font=("arial", 10, 'bold'))
clock.place(x=200, y=450)

longitude=Label(root, text="Longitude:", bg="#57adff", fg="black", font=("arial", 10, 'bold'))
longitude.place(x=50, y=500)

latitude=Label(root, text="Latitude:", bg="#57adff", fg="black", font=("arial", 10, 'bold'))
latitude.place(x=200, y=500)

root.mainloop()