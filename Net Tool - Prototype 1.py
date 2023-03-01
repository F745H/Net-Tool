from tkinter import *
from tkinter import messagebox
import subprocess
import os

container = Tk()

pingVar = StringVar()
inputVar = IntVar()
tracertVar = StringVar()
checkBtVar = BooleanVar()

def about():
        #About
        messagebox.showinfo("About", "Net Tool means Network Resolving Tool.\nThis software is coded by Vyankatesh Pipalwa")

def how():
        #How to
        messagebox.showinfo("How to use"," 1)To use ping type ip or host address in box.\n 2)To find route of packet type ip or host address in box.\n 3)To restart network devices press Restart.\n 4)To resolve network press Resolve.\n\n Note:- Run as administrator this software to use properly.")

def compati():
        #Compatibility
        messagebox.showinfo("Compatibility","This software is compatible with all Windows operating systems.")

def delEntryPing():
        e1.delete(0, END)

def delEntryTracert():
        e3.delete(0, END)

def resolved():
        messagebox.showinfo("Done","Network Resolved.")

def ping():
        host = pingVar.get()
        packet = inputVar.get()
        flag=checkBtVar.get()
        if len(host)==0:
               messagebox.showwarning("Warning", "Please enter ip/host address in the field!")
        elif len(host)>=0:
                if flag==FALSE:
                        os.system(f"start cmd.exe @cmd /k ping -t {host}")
                elif flag==TRUE & packet=='':
                        messagebox.showwarning("Warning", "Please enter packet numbers in the field!")
                else:       
                        os.system(f"start cmd.exe @cmd /k ping -c {packet} {host}")
                delEntryPing()

def tracert():
        ip = tracertVar.get()
        print(ip)
        if len(ip)==0:
               messagebox.showwarning("Warning", "Please enter ip/host address in the field!")
        elif len(ip)>=0:
                os.system(f"start cmd.exe @cmd /k tracert {ip}")
                delEntryTracert()

def activateCheck():
        if checkBtVar.get()==1:
            e2.config(state=NORMAL)
        elif checkBtVar.get()==0:
            e2.config(state=DISABLED)
            
def restart():
        os.system('start cmd.exe @cmd /k powershell Restart-NetAdapter -Name "Ethernet" ; Restart-NetAdapter -Name "Wi-Fi" ; Write-Host "Done"')

def resolve():
        subprocess.call("ipconfig /release")
        subprocess.call("ipconfig /flushdns")
        subprocess.call("ipconfig /renew")
        subprocess.call("netsh int ip set dns")
        subprocess.call("netsh winsock reset")
        subprocess.call("netsh int ip reset resetlog.txt")
        resolved()


#Title
container.title("Net Tool")
#Width X Length
container.geometry("480x380")
#Background color
container.config(bg="#856ff8")
#Icon
container.iconbitmap('D:\PycharmProjects\Exit_Message\logoV2.ico')


#Ping Label
user_label = Label(container, text='Ping:-', bg="#856ff8", font=("Helvetica", "10", "bold"))
user_label.grid(row=0, column=1, padx=10, pady=10)
#Text box
e1 = Entry(container, textvariable=pingVar, bd=2)
e1.grid(row=1, column=1, padx=10, pady=10)
#Check box
c1 = Checkbutton(container, text = "No. of packets", variable = checkBtVar, onvalue = TRUE, offvalue = FALSE, command=activateCheck, bg="#856ff8", activebackground="grey")
c1.grid(row=1, column=2, padx=0, pady=0)
#Text box
e2 = Entry(container, textvariable=inputVar, bd=2, width=3)
e2.grid(row=1, column=3)
e2.config(state=DISABLED)
#Button
button1= Button(container, text='Ping', width=10, activebackground='#8af', command=ping)
button1.grid(row=2, column=1, padx=10, pady=10)
button2= Button(container, text='Clear', width=10, activebackground='#8af', command=delEntryPing)
button2.grid(row=2, column=2, padx=10, pady=10)


#Traceroute Label
user_label2 = Label(container, text='Traceroute:-', bg="#856ff8", font=("Helvetica", "10", "bold"))
user_label2.grid(row=3, column=1, padx=10, pady=10)
#Text box
e3 = Entry(container, textvariable=tracertVar, bd=2)
e3.grid(row=4, column=1)
#Button
button3= Button(container, text='Tracert', width=10, activebackground='#8af', command=tracert)
button3.grid(row=5, column=1, padx=10, pady=20)
button4= Button(container, text='Clear', width=10, activebackground='#8af', command=delEntryTracert)
button4.grid(row=5, column=2, padx=10, pady=20)


#Restart Label
user_label3 = Label(container, text='Restart Network Devices:-', bg="#856ff8", font=("Helvetica", "10", "bold"))
user_label3.grid(row=6, column=1, padx=20, pady=10)
#Button
button5= Button(container, text='Restart', width=10, activebackground='#8af', command=restart)
button5.grid(row=7, column=1, padx=20, pady=10)


#Resolve Label
user_label4 = Label(container, text='Resolve Network Problems:-', bg="#856ff8", font=("Helvetica", "10", "bold"))
user_label4.grid(row=6, column=2, padx=20, pady=10)
#Button
button5= Button(container, text='Resolve', width=10, activebackground='#8af', command=resolve)
button5.grid(row=7, column=2, padx=20, pady=10)


#Menu section
menu = Menu(container)
container.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=container.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Compatibility', command=compati)
helpmenu.add_command(label='How', command=how)
helpmenu.add_command(label='About', command=about)
#Loop
container.mainloop()