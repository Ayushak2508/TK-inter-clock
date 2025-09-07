import time
import tkinter as tk

root = tk.Tk()
root.title("Clock")
root.geometry("600x400")
root.config(bg="black")
root.resizable(False, False)

d_lable =tk.Label(root , text="", font=("arial" , 20 , "bold") , fg="lightgreen" , bg="black")
d_lable.place(x=30 , y=55)

time_lable = tk.Label(root,text="",font=("Arial", 65,"bold" ) ,fg="lightgreen" , bg="black" , relief="ridge")
time_lable.pack(pady=20)

wts_lable = tk.Label(root , text="" , font=("Arial" , 20 , "bold") , fg="lightgreen" , bg="black")
wts_lable.place(x=150,y=250)

def my_clock():
    day = time.strftime("%a")
    d_lable.config(text=day)
    current_time = time.strftime("%H :%M :%S")
    time_lable.config(text=current_time)
    root.after(1000, my_clock)

def what_to_say():
    current_hour = int(time.strftime("%H"))
    if 6 < current_hour < 12:
        wts_lable.config(text="Good Morning")
    elif 12 <= current_hour < 16:
        wts_lable.config(text="Good Afternoon")
    elif 16 <= current_hour < 20:
        wts_lable.config(text="Good Evening")
    else:
        wts_lable.config(text="Good Night")

what_to_say()
my_clock()
root.mainloop()
