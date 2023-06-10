# MAKE UKRAINE_GRIVNYA/MY DISCORD-Danilkin|DG#7825/My GitHub-https://github.com/DGioriginal
# COMPANY-DGi.org
import webbrowser
import Tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from time import sleep
tk = Tk()
tk.config(cursor="hand1")
tk.title('Click-KILL_putin')
x = tk.winfo_screenwidth()  
y = tk.winfo_screenheight()  
tk.geometry('{}x{}'.format(int(x*0.7), int(y*0.7)))
n = 0
misec= 0
rank= 0
click = 0
head = ImageTk.PhotoImage(file="huyutin-heard.gif")
pay = ImageTk.PhotoImage(file="click-38$.png")
pay2= ImageTk.PhotoImage(file="strong head.jpg")
bg = ImageTk.PhotoImage(file="bg_kill.png")
label1 = Label(tk, image = bg)
label1.place(x = 0, y = 0)
def close():
        main_window.withdraw()  
        t = Toplevel(main_window) 
def info():
    info = Tk()
    info.config(cursor="hand1")
    info.title('Click-KILL_putin')
    info.geometry("250x250")
    btn1 = Button(text="", image= head, background="snow", foreground="snow",
             padx="1", pady="1", font="10", command=close)
    btn1.pack() 
def nplus():
    global n
    global misec
    n = n + 1
    n = n + misec
    label['text'] = str(n) + '$'
    label2['text'] = str(misec) + '/X' 

def discord():
    webbrowser.open('https://discord.gg/mQvaHrebEM', new=2)
def error_show():
    messagebox.showerror("Payment error", "You have -38$, please click more and you pay this")

def clicks():
    global misec
    global n
    if n > 38 or n == 38:
        misec = misec + 1
        label2['text'] = str(misec) + '/X'
        n= 0
        sleep(1)
    if n < 38:
        error_show()


def motion(event):
    globals
    tk.config(cursor="pirate")
def endmotion(event):
    globals
    tk.config(cursor="hand1")
label2 = Label(tk, text=str(misec)+'/X',background="blue", font=('Helvetica 16'))
label2.place(x=0, y=0)

btn1 = Button(text="", image= head, background="snow", foreground="snow",
             padx="1", pady="1", font="10", command=nplus)
btn1.place(x=0, y=30)
btn1.bind('<Motion>', motion)
label = Label(tk, text=str(n)+'$', font=('Helvetica 50'))
label.place(x=110, y=435)
btn2 = Button(text="", image= pay, background="snow", foreground="snow", font="10", command=clicks)
btn2.place(x=645, y=60)
btn3 = Button(text="", image= pay2, background="snow", foreground="snow", font="10", command=clicks)
btn3.place(x=345, y=60)
label3 = Label(tk, text='--------------STORE-----------',background="blue", font=('Helvetica 38'))
label3.place(x=345, y=10)
mainloop()
