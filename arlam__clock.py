import os
from tkinter import *
import datetime
from tkinter import filedialog
from pygame import mixer



root = Tk()
root.title('Alarm Clock')
root.config(bg='lightgreen')
root.geometry('550x500')
mixer.init()


hrs = StringVar()
mins = StringVar()
sec = StringVar()

def select():
    global song
    song = filedialog.askopenfile()
    
def set_alarm():
    alarmtime = f"{hrs.get()}:{mins.get()}:{sec.get()}"
    if alarmtime != ': :':
        alarmclock(alarmtime)

def alarmclock(alarm_time):
    while True:
        c_time = datetime.datetime.now().strftime("%H:%M:%S")
        #print(c_time)
        if c_time == alarm_time:
            Label(root,text='Wake UP! Wake UP! Wake UP!',bg='lightgreen',font=('arial',20,'italic')).grid(padx=20,pady=10,row=2,column=2)
            print("Wake UP!")
            mixer.music.load(song)
            mixer.music.play(loops=3)
            break
c_time = datetime.datetime.now().date()
Label(root,text=f'{c_time}',font=('arial',20,'italic'),bg='lightgreen').grid(row=1,column=2)
Label(root,text='Години:',font=('arial',20,'italic'),bg='lightgreen').grid(sticky='e',row=3,column=1)
Label(root,text='Хвилини:',font=('arial',20,'italic'),bg='lightgreen').grid(sticky='e',row=4,column=1)
Label(root,text='Секунди:',font=('arial',20,'italic'),bg='lightgreen').grid(sticky='e',row=5,column=1)


hrs_entry = Entry(root,textvariable=hrs,width=5,font=('arail',20,'italic')).grid(padx=1,pady=10,row=3,column=2)
mins_entry = Entry(root,textvariable=mins,width=5,font=('arail',20,'italic')).grid(padx=1,pady=10,row=4,column=2)
sec_entry = Entry(root,textvariable=sec,width=5,font=('arail',20,'italic')).grid(padx=1,pady=10,row=5,column=2)


set_btn =  Button(root,command=set_alarm,text='Встановити будильник',bg='lightgreen',fg='black',font=('arail',20,'italic')).grid(pady=30,row=7,column=2)
set_btn_0 =  Button(root,command=root.destroy,text='Вихід',bg='lightgreen',fg='black',font=('arail',20,'italic')).grid(padx=40,row=8,column=2)
set_btn_1 =  Button(root,command=select,text='Обрати мелодію',bg='lightgreen',fg='black',font=('arail',20,'italic')).grid(padx=40,pady=10,row=9,column=2)
mainloop()