from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
import time
from bs4 import BeautifulSoup
import urllib.request as urllib2
from tkinter import messagebox
import os
import requests

w = Tk()

# Using piece of code from old splash screen
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

def openMailer():
        os.system('python mailer.py')
def openWriter():
        os.system('python writer.py')

#w.configure(bg='#ED1B76')
w.overrideredirect(1) #for hiding titlebar

#new window to open
def new_win():
    q=Tk()
    q.title('Marketing Software By Vinit Patel')
    q.minsize(500,200) # minimum possible size of the window
    l1 = Label(text="Choose the service you want to use", font=("times new roman", 18, "bold")).grid()
   

    B1 = Button(q, activebackground="skyblue", text="Mailer", font=("times new roman", 20, "bold"),
                      bg="black",fg="white", command=openMailer).place(x=60, y=50, width=90, height=30)
    B2 = Button(q, activebackground="skyblue", text="Writer", font=("times new roman", 20, "bold"),
                      bg="black",fg="white", command=openWriter).place(x=260, y=50, width=90, height=30)


    q.mainloop()

    



Frame(w, width=427, height=250, bg='#272727').place(x=0,y=0)
label1=Label(w, text='Marketing Software', fg='white', bg='#272727') # decorate it 
label1.configure(font=("Game Of Squids", 24, "bold"))   # You need to install this font in your PC or try another one
label1.place(x=80,y=90)

label2=Label(w, text='Developer : Vinit Patel - 202103103510385', fg='white', bg='#272727') #decorate it 
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)


# making animation

image_a = ImageTk.PhotoImage(Image.open('c2.png'))
image_b = ImageTk.PhotoImage(Image.open('c1.png'))


for i in range(5): # 5 loops
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

w.destroy()

    # new_win()                


def connection_check():
    try:
        urllib2.urlopen('http://google.com')
        return True
    except urllib2.URLError as err:
        return False
    
def get_date():
    r = requests.get('https://www.calendardate.com/todays.htm')
    soup = BeautifulSoup(r.text, 'html.parser')
    a=soup.find_all(id='tprg')[6].get_text()
    a=a.replace('-','') # removing hyphen from date                           
    a=a.replace(' ','') # removing space from date                            
    return a
    
if connection_check() == True:
    limit = 20240327
    current_date = int(get_date())
    if current_date <= limit:
        new_win()
    else:
        root = Tk()
        root.withdraw()
        messagebox.showinfo("Marketing Software By Vinit Patel", "Subscription Expired !!! \nPlease renew your subsrription inorder to use software")
else:
    root = Tk()
    root.withdraw()
    messagebox.showinfo("Marketing Software By Vinit Patel", 'Check Your internet Connection !')
    
w.mainloop()

