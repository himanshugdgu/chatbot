from tkinter import *
from playsound import playsound
from speech_project import analyzer
from PIL import Image, ImageTk
from tts import speak
from threading import Thread
from speech_project import main
from stt import takeCommand         

root = Tk()
width = 600
height = 400
blue = '#9999ff'
root.geometry('{}x{}+{}+{}'.format(width, height, 470, 100))
border_color = Frame(root, background=blue)

i = 0
bgimage = Image.open(r'Command_line\1624.jpg')
bgimage = bgimage.resize((602, 402))
bgimage = ImageTk.PhotoImage(bgimage)
Label(root, image=bgimage).place(x=-1, y=-1)


def threading():
    t2 = Thread(target=work2)
    t2.start()
    t1 = Thread(target=work1)
    t1.start()


def work1():
    insert_into(
        "-------------------------------------------------------------------------------------------------------\nUser Said => "+entry_box.get())
    entry_box.delete(0, END)

def work2():
    query = entry_box.get().lower()
    output = main(query)
    if (output == 100):
        root.destroy()
    insert_into('Bot => '+output)
    speak(output)

def calculation():
    query = takeCommand()
    entry_box.insert(0, query)
    threading()


entry_box = Entry(root, relief="solid", font=("default", 16), width=42)
entry_box.place(x=10, y=height-40)
entry_box.bind('<Return>', lambda event: threading())

image = Image.open(r'GUI\amazon-alexa-logo.png')
image = image.resize((50, 50))
img = ImageTk.PhotoImage(image)


# listbox = Listbox(root, height=12,
#                   width=52,
#                   bg="#66b3ff",
#                   activestyle='dotbox',
#                   font="Helvetica",
#                   fg='#000')
# listbox.place(x=10, y=35)
Label(root, text="HUMAN LANGUAGE INTERFACE", font=(35)).pack()
label_frame = Frame(root, highlightbackground="blue",
                    highlightthickness=2, width=550, height=300, bg="#ff0066")
label_frame.pack_propagate(0)
label_frame.pack()
Label(label_frame, image=bgimage).place(x=-1, y=-1)

chats = Label(label_frame, text="", wraplength=550, justify="center")
chats.pack()
myscrollbar = Scrollbar(label_frame, orient="vertical")
myscrollbar.pack(side="right", fill="y")


def insert_into(text):
    chats['text'] = chats['text']+'\n'+text
    # listbox.insert(i, text)

# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
# listbox.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox.yview)
button = Button(root, borderwidth=0, image=img, command=lambda: calculation())
button.place(x=width-65, y=height-60)
root.mainloop()