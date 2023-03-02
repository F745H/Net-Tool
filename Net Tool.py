from tkinter import *
from tkinter import messagebox
import os
import sys

container = Tk()


pingVar = StringVar()
tracertVar = StringVar()
checkBtVar = BooleanVar()


def about():
        #About
        messagebox.showinfo("About", "\nThis software is coded by Vyankatesh Pipalwa")


def how():
        #How to
        messagebox.showinfo("How to use"," 1)To use ping type ip or host address in box.\n 2)To find route of packet type ip or host address in box.\n 3)To restart network devices press Restart.\n 4)To resolve network press Resolve.\n 5)To get maximum performance of system press Boost.\n\n Note:- Run as administrator this software to use properly.")


def compati():
        #Compatibility
        messagebox.showinfo("Compatibility","This software is compatible with all Windows operating systems.")


def delEntryPing():
        #Delete Characters from ping entry box
        pingEntry.delete(0, END)


def delEntryTracert():
        #Delete Characters from tracert entry box
        tracertEntry.delete(0, END)


def resolved():
        #Resolved message
        messagebox.showinfo("Done","Network Resolved.")


def boosted():
        #Boosted message
        messagebox.showinfo("Done","Now your system is pretty fast.\nYou will feel it.")


def ping():
        #Ping
        host = pingVar.get()
        flag=checkBtVar.get()
        if len(host)==0:
               messagebox.showwarning("Warning", "Please enter ip/host address in the field!")
        elif len(host)>=0:
                if flag==FALSE:
                        os.system(f"start cmd.exe @cmd /k ping -t {host}")
                else:       
                        os.system(f"start cmd.exe @cmd /k ping {host}")
                delEntryPing()


def tracert():
        #Traceroute
        ip = tracertVar.get()
        print(ip)
        if len(ip)==0:
               messagebox.showwarning("Warning", "Please enter ip/host address in the field!")
        elif len(ip)>=0:
                os.system(f"start cmd.exe @cmd /k tracert {ip}")
                delEntryTracert()
    

def restart():
        #Restart network devices
        os.system('start cmd.exe @cmd /k powershell Restart-NetAdapter -Name "Ethernet" ; Restart-NetAdapter -Name "Wi-Fi" ; Write-Host "Done"')


def resolve():
        #Resolve network problems
        os.system("ipconfig /release")
        os.system("ipconfig /flushdns")
        os.system("ipconfig /renew")
        os.system("netsh int ip set dns")
        os.system("netsh winsock reset")
        os.system("netsh int ip reset resetlog.txt")
        resolved()


def boost():
        #Boost speed
        os.system(f"del %systemroot%\Temp\*.* /s /q")
        os.system(f"del %temp%\*.* /s /q")
        os.system(f"del %systemroot%\prefetch\*.* /s /q")
        os.system(f"del %APPDATA%\Microsoft\Windows\Recent\*.* /f /q")
        boosted()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


#Title
container.title("Net Tool")
#Width X Height
container.geometry("590x380")
#Background color
container.config(bg="SeaGreen3")
#Icon
iconPath = resource_path("logoV2.ico")
container.iconbitmap(iconPath)


#Ping Label
pingUserLabel = Label(container, text='Ping', bg="SeaGreen2", font=("Helvetica", "10", "bold"))
pingUserLabel.grid(row=0, column=1, padx=10, pady=10)
#Text box
pingEntry = Entry(container, textvariable=pingVar, bd=2)
pingEntry.grid(row=1, column=1, padx=10, pady=10)
#Check box
checkButton = Checkbutton(container, text = "4 packets", variable = checkBtVar, onvalue = TRUE, offvalue = FALSE, bg="SeaGreen2", activebackground="SeaGreen2")
checkButton.grid(row=1, column=2, padx=0, pady=0)
#Button
pingButton = Button(container, text='Ping', width=10, activebackground='#8af', command=ping)
pingButton.grid(row=2, column=1, padx=10, pady=10)
pingClearButton = Button(container, text='Clear', width=10, activebackground='#8af', command=delEntryPing)
pingClearButton.grid(row=2, column=2, padx=10, pady=10)


#Traceroute Label
tracertUserLabel = Label(container, text='Traceroute', bg="SeaGreen2", font=("Helvetica", "10", "bold"))
tracertUserLabel.grid(row=3, column=1, padx=10, pady=10)
#Text box
tracertEntry = Entry(container, textvariable=tracertVar, bd=2)
tracertEntry.grid(row=4, column=1)
#Button
tracertButton = Button(container, text='Tracert', width=10, activebackground='#8af', command=tracert)
tracertButton.grid(row=5, column=1, padx=10, pady=20)
tracertClearButton = Button(container, text='Clear', width=10, activebackground='#8af', command=delEntryTracert)
tracertClearButton.grid(row=5, column=2, padx=10, pady=20)


#Restart Label
restartUserLabel = Label(container, text='Restart Network Devices', bg="SeaGreen2", font=("Helvetica", "10", "bold"))
restartUserLabel.grid(row=6, column=1, padx=20, pady=10)
#Button
restartButton = Button(container, text='Restart', width=10, activebackground='#8af', command=restart)
restartButton.grid(row=7, column=1, padx=20, pady=10)


#Resolve Label
resolveUserLabel = Label(container, text='Resolve Network Problems', bg="SeaGreen2", font=("Helvetica", "10", "bold"))
resolveUserLabel.grid(row=6, column=2, padx=20, pady=10)
#Button
resolveButton= Button(container, text='Resolve', width=10, activebackground='#8af', command=resolve)
resolveButton.grid(row=7, column=2, padx=20, pady=10)


#Boost Label
boostUserLabel = Label(container, text='Boost System Speed', bg="SeaGreen2", font=("Helvetica", "10", "bold"))
boostUserLabel.grid(row=6, column=3, padx=20, pady=10)
#Button
boostButton= Button(container, text='Boost', width=10, activebackground='#8af', command=boost)
boostButton.grid(row=7, column=3, padx=20, pady=10)


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