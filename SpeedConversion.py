import tkinter as tk
import ttkbootstrap as ttk 

def calc():
    input = entryint.get()
    ans = input * 5/18
    outputstr.set(ans)



def mcalc():
    input2 = entryint2.get()
    ans2 = input2 * 18/5
    outputstr2.set(ans2)
#window
#window
window = ttk.Window(themename="vapor")
window.title("Speed Conversion")
window.geometry("720x380")
#Body
h1 = ttk.Label(master=window,text="Km/hr to m/s",font="Calibri 20 bold")
h1.pack()
#entryfield
entryframe = ttk.Frame(master=window)
entryint = tk.DoubleVar()
entryfield = ttk.Entry(master=entryframe,textvariable=entryint)
b1 = ttk.Button(master=entryframe,text="km/h",command= calc)

entryfield.pack(side="left")
b1.pack(side="left")
entryframe.pack(pady="10")
#output
outputstr = tk.StringVar()
answer = ttk.Label(master=window,font="Calibri 20",textvariable= outputstr)
unit1 = ttk.Label(master= window,font="Calibri 20 italic",text ="m/s" )
answer.pack()
unit1.pack()

#m/s to km/h
div = ttk.Label(master=window,text="<=======================>",font="Calibri 20 bold")
div.pack(pady="5")
h2 = ttk.Label(master=window,text="m/s to km/h",font="Calibri 20 bold")
h2.pack()
#entryfield
entryframe2 = ttk.Frame(master=window)
entryint2 = tk.DoubleVar()
entryfield2 = ttk.Entry(master=entryframe2,textvariable=entryint2)
b12 = ttk.Button(master=entryframe2,text="m/s",command= mcalc)

entryfield2.pack(side="left")
b12.pack(side="left")
entryframe2.pack(pady="10")
#output
outputstr2 = tk.StringVar()
answer2 = ttk.Label(master=window,text= calc,font="Calibri 20",textvariable= outputstr2)
unit2 = ttk.Label(master= window,text ="km/hr",font="Calibri 20 italic")
answer2.pack()
unit2.pack()













#run
window.mainloop()