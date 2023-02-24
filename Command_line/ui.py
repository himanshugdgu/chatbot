from threading import Thread
from tkinter import *
from speech_project import main
from tts import speak
# GUI
root = Tk()
root.title("Chatbot")
# root.geometry('300x500')
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

def threading():

    t1=Thread(target=work1)
    t1.start()

    t2=Thread(target=work2)
    t2.start()
  
# work function
def work1():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
    e.delete(0, END)

def work2():
    query = e.get().lower()
    output = main(query)
    txt.insert(END, "\n" + 'Bot -> '+output)
    speak(output)
# Send function


def send():
    def work():
        send = "You -> " + e.get()
        txt.insert(END, "\n" + send)
    t1=Thread(target=work)
    t1.start()
    query = e.get().lower()
    output = main(query)
    txt.insert(END, "\n" + 'Bot -> '+output)
    e.delete(0, END)
    speak(output)

lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="JARVIS",font=FONT_BOLD, pady=10, width=20, height=1).grid(row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.2)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=threading).grid(row=2, column=1)
root.bind('<Return>',lambda event:threading())
root.mainloop()