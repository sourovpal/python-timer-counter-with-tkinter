from tkinter import *
from playsound import playsound
import time

root = Tk()
root.title("Timer")
root.geometry("400x570+450+200")
root.config(bg="#2C3E50")
root.resizable(False, False)
heading = Label(root, text="Timer", font="arial 30 bold", bg="#2C3E50", fg="#F1C40F")
heading.pack(pady=10)

Label(root, font=("arial", 15, "bold"), text="Current Time: ", bg="#2C3E50", fg="#F1C40F").place(x=85, y=70)
def clock():
    clock_time = time.strftime("%H:%M:%S %p")
    current_time.config(text=clock_time)
    current_time.after(1000, clock)

current_time = Label(root, font=("arial", 13, "bold"), pady=5, text="", fg="#F1C40F", bg="#2C3E50")
current_time.place(x=220, y=70)
clock()

#timer

hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font="arial 50", bg="#2C3E50", bd=0, fg="#fff").place(x=45, y=155)
hrs.set("00")
Label(root, text="Hours", font="arial 12", bg="#2C3E50", fg="#fff").place(x=60, y=225)


mins = StringVar()
Entry(root, textvariable=mins, width=2, font="arial 50", bg="#2C3E50", bd=0, fg="#fff").place(x=165, y=155)
mins.set("00")
Label(root, text="Min", font="arial 12", bg="#2C3E50", fg="#fff").place(x=185, y=225)

sec = StringVar()
Entry(root, textvariable=sec, width=2, font="arial 50", bg="#2C3E50", bd=0, fg="#fff").place(x=285, y=155)
sec.set("00")
Label(root, text="Sec", font="arial 12", bg="#2C3E50", fg="#fff").place(x=305, y=225)

def setTime(time):
    hrs.set("00")
    mins.set(time)
    sec.set("00")


Image1 = PhotoImage(file="brush.png")
btn1 = Button(root, image=Image1, bg="#2C3E50", bd=0, command= lambda:setTime("02"), cursor="hand2")
btn1.place(x=7, y=300)

Image2 = PhotoImage(file="face.png")
btn2 = Button(root, image=Image2, bg="#2C3E50", bd=0, command= lambda:setTime("15"), cursor="hand2")
btn2.place(x=138, y=300)

Image3 = PhotoImage(file="eggs.png")
btn3 = Button(root, image=Image3, bg="#2C3E50", bd=0, command= lambda:setTime("10"), cursor="hand2")
btn3.place(x=265, y=300)

def Timer(stop = False):
    times = int(hrs.get())*3600+int(mins.get())*60+int(sec.get())
    if times <= 0:
        pass
        # playsound("time-up.wav")
        # playsound("start-time.wav")

    while times > -1:

        minute, second = (times//60, times%60)
        hour = 0
        if minute > 60:
            hour, minute = (minute//60, minute%60)

        if hour < 10:
            hrs.set(f"0{hour}")
        else:
            hrs.set(hour)

        if minute < 10:
            mins.set(f"0{minute}")
        else:
            mins.set(minute)

        if second < 10:
            sec.set(f"0{second}")
        else:
            sec.set(second)

        root.update()
        time.sleep(1)
        if(times == 0):
            # playsound("time-up.wav")
            hrs.set("00")
            mins.set("00")
            sec.set("00")
        times -= 1

stop_btn = Button(root, text="Stop", bg="#F1C40F", font=("arial", 13, "bold"), padx=40, pady=5, cursor="hand2", command= lambda:Timer(False))
stop_btn.place(x=50, y=460)
start_btn = Button(root, text="Start", bg="#F1C40F", font=("arial", 13, "bold"), padx=40, pady=5, cursor="hand2", command= lambda:Timer(True))
start_btn.place(x=220, y=460)


root.mainloop()