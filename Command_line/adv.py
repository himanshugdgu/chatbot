from re import L
import tkinter as tk
from tkinter import *
from tkinter.ttk import Style
from PIL import ImageTk, Image
from playsound import playsound
from speech_project import analyzer
from PIL import Image, ImageTk
from tts import speak
from threading import Thread
from speech_project import main
from stt import takeCommandEnglish
from languages_ import takeCommandHindi
from time import strftime
from weather_finder import weather_forecast
from playsound import playsound
import music_player2
from SnakeGame import game

# from tic_tac_toe import game1

root = Tk()
root.title("Jarvis")
topframe = Frame(root, bg='#74ddfe', width=1280, height=70)
topframe.pack()
topframe.pack_propagate(0)


def show():
    cur_voice.config(text=clicked.get())


options = ["Ravi", "David", "Mark", "Heera", "Zira☕"]
clicked = StringVar()
clicked.set(options[2])

lang_int = 0  # english is 0 , hindi is 1


def change_lang():
    play_click_sound()
    if (cur_lang.cget('text') == "English"):
        cur_lang.config(text="Hindi")
    else:
        cur_lang.config(text="English")


Label(topframe, text="Your Current Language :", font=(
    "Arial", 13), bg='#74ddfe').place(x=360, y=25)
cur_lang = Button(topframe, text="English", font=("Arial", 13, "bold"),
                  borderwidth=1, relief="solid", pady=5, padx=5, command=change_lang)
cur_lang.place(x=550, y=18)


Label(topframe, text="Set Voices :", font=(
    "Arial", 12, "bold"), bg='#74ddfe').place(x=800, y=25)
drop = OptionMenu(topframe, clicked, *options)
drop.config(font=("Arial", 12))
drop.place(x=900, y=22)
button = Button(topframe, text="Change", command=show, font=(
    "Arial", 12), padx=10, pady=5, bg="#37475A", fg="#fff").place(x=990, y=19)
Label(topframe, text="Current Voice : ", font=(
    "Arial", 12), bg='#74ddfe').place(x=1090, y=25)
cur_voice = Label(topframe, text=options[2], font=(
    "Arial", 12, "underline"), bg='#131A22', fg="#fff", pady=5, padx=5, borderwidth=1, relief="solid")
cur_voice.place(x=1210, y=23)

Label(topframe, text="", borderwidth=1, font=(
    200), bg="#000").place(x=1084, y=24)

def threading():
    t1 = Thread(target=work1)
    t1.start()
    t2 = Thread(target=work2)
    t2.start()

def work1():
    bot_chat.config(text="Loading...")
    user_chat.config(text=entry_box.get())


def work2():
    query = entry_box.get().lower()
    output = main(query)
    if (output == 100):
        root.destroy()
    bot_chat.config(text=output)
    entry_box.delete(0, END)
    speak(output)


def threading_weather():
    output = weather_forecast()
    user_chat.config(text="Weather Forecast In Gurgaon")
    bot_chat.config(text=output)
    speak(output)


def play_click_sound():
    playsound(r"Command_line\click_sound.mp3")


def get_weather():
    play_click_sound()
    Thread(target=threading_weather).start()


def mic():
    if (cur_lang.cget('text') == "English"):
        query = takeCommandEnglish()
    else:
        query = takeCommandHindi()
    entry_box.insert(0, query)
    threading()

# def Label_configure():
#     user_chat.config(text = entry_box.get())
#     bot_chat.config(text="Loading...")
#     entry_box.delete(0, END)

# def func():
#     user_chat.config(text = entry_box.get())
#     bot_chat.config(text="Loading...")
#     entry_box.delete(0, END)


def time():
    string = strftime('%H:%M %p')
    lbl.config(text=string)
    lbl.after(1000, time)


leftframe = Frame(root, bg='#252021', width=200, height=630)
leftframe.place(x=0, y=70)
leftframe.pack_propagate(0)

lbl = Label(leftframe, font=('calibri', 20, 'bold'), pady=10,
            padx=20, background='#3d3839', foreground='white')
lbl.place(x=20, y=30)
time()

def open_game1():
    game()

def open_game2():
    import tic_tac_toe

# def open_game3():
    

def open_timer():
    import non_query_timer

def about_jarvis():
    user_chat.config(text="")
    bot_chat.config(
        text="I am your Virtual Assistant. \nYou can call me JARVIS\nJARVIS  stands for Just a rather very intelligent system. It is virtual assistant can engage in two way conversation.")

# left tile contents


home = Button(leftframe, text="  Home               ",
              bg="#555555", fg="#fff", font=("Arial", 18))
home.place(x=0, y=120)
Button(leftframe, text="  Music               ", bg="#252021",
       fg="#fff", font=("Arial", 18), command=lambda: [play_click_sound(), music_player2.play()]).place(x=0, y=170)
Button(leftframe, text="  Communicate    ", bg="#555555",
       fg="#fff", font=("Arial", 18), command=lambda: [play_click_sound(), mic()]).place(x=0, y=220)
Button(leftframe, text="  Alarms              ", bg="#252021",
       fg="#fff", font=("Arial", 18), command=lambda: [play_click_sound(), open_timer()]).place(x=0, y=270)
Button(leftframe, text="  Timers              ", bg="#555555",
       fg="#fff", font=("Arial", 18), command=lambda: [play_click_sound(), open_timer()]).place(x=0, y=320)
Button(leftframe, text="  Snake Game          ", bg="#252021",
       fg="#fff", font=("Arial", 18), command=lambda: [play_click_sound(), open_game1()]).place(x=0, y=370)
Button(leftframe, text="  Tic-Tac-Toe        ", bg="#555555",
       fg="#fff", font=("Arial", 18), command=lambda: [play_click_sound(), open_game2()]).place(x=0, y=420)
Button(leftframe, text="  Online Games       ", bg="#252021",
       fg="#fff", font=("Arial", 18), command=lambda: [play_click_sound(), open_game3()]).place(x=0, y=420)
Button(leftframe, text="  About Jarvis         ", bg="#555555",
       fg="#fff", font=("Arial", 18), command=lambda: [play_click_sound(), about_jarvis()]).place(x=0, y=570)

# home.bind("<Enter>",lambda e:highlight())
# home.bind("<Leave>",lambda e:lowlight())

bgimage = Image.open(r'Command_line\1624.jpg')
bgimage = bgimage.resize((1080, 630))
bgimage = ImageTk.PhotoImage(bgimage)
Label(root, image=bgimage).place(x=200, y=70)

image = Image.open(r'Command_line\alexa_icon.PNG')
image = image.resize((50, 53))
img = ImageTk.PhotoImage(image)

button = Button(topframe, borderwidth=0, image=img, bg="#31C4F3",
                command=lambda: mic())
button.place(x=10, y=9)
mic_text = Label(topframe, text="click to talk",
                 bg="#74ddfe", font=("Arial", 16, "italic"))
mic_text.place(x=70, y=23)

tile1 = Frame(root, bg='#064B73', width=250, height=250,
              highlightbackground="#0098E6", highlightthickness=2)
tile1.place(x=230, y=100)
tile1.pack_propagate(0)

tile1_img = Image.open(r'Command_line\earphone_img.jpg')
tile1_img = tile1_img.resize((200, 120))
tile1_img = ImageTk.PhotoImage(tile1_img)
Label(tile1, image=tile1_img).pack()
Label(tile1, text="Listen to your favourite songs with Jarvis. Discover songs and playlists from Youtube",
      wraplength=200, fg="#fff", bg="#064B73", pady=13).pack()
Button(tile1, text="Play Music", fg="#fff",
       bg="#08AAE3", padx=20, pady=0, font=(15), command=lambda: [play_click_sound(), music_player2.play()]).pack()


tile2 = Frame(root, bg='#064B73', width=250, height=250,
              highlightbackground="#0098E6", highlightthickness=2)
tile2.place(x=500, y=100)
tile2.pack_propagate(0)

tile2_img = Image.open(r'Command_line\weather_img.jpg')
tile2_img = tile2_img.resize((200, 120))
tile2_img = ImageTk.PhotoImage(tile2_img)
Label(tile2, image=tile2_img).pack()
Label(tile2, text='''"Jarvis, how's the weather today?"\nPlan for the day's adventure and just ask Jarvis about the weather''',
      wraplength=200, fg="#fff", bg="#064B73", pady=13).pack()
Button(tile2, text="Weather Today", fg="#fff",
       bg="#08AAE3", padx=10, pady=0, font=(15), command=get_weather).pack()

tile3 = Frame(root, bg='#064B73', width=250, height=250,
              highlightbackground="#0098E6", highlightthickness=2)
tile3.place(x=230, y=380)
tile3.pack_propagate(0)

tile3_img = Image.open(r'Command_line\clock_img.jpg')
tile3_img = tile3_img.resize((200, 120))
tile3_img = ImageTk.PhotoImage(tile3_img)
Label(tile3, image=tile3_img).pack()
Label(tile3, text='Now set alarms and timer with Jarvis\nJust say "Set Alarms"\n',
      wraplength=200, fg="#fff", bg="#064B73", pady=13).pack()
Button(tile3, text="Set Alarms", fg="#fff",
       bg="#08AAE3", padx=20, pady=0, font=(15), command=open_timer).pack()


tile4 = Frame(root, bg='#064B73', width=250, height=250,
              highlightbackground="#0098E6", highlightthickness=2)
tile4.place(x=500, y=380)
tile4.pack_propagate(0)

tile4_img = Image.open(r'Command_line\different_lang_img.jpg')
tile4_img = tile4_img.resize((200, 120))
tile4_img = ImageTk.PhotoImage(tile4_img)
Label(tile4, image=tile4_img).pack()
Label(tile4, text='Now you can talk to Jarvis in Hindi also\nJarvis has multi-language support',
      wraplength=200, fg="#fff", bg="#064B73", pady=13).pack()
Button(tile4, text="Change Language", fg="#fff",
       bg="#08AAE3", padx=20, pady=0, font=(15), command=change_lang).pack()


chat_window = Frame(root, bg='#505050', width=400, height=500,
                    highlightbackground="#0098E6", highlightthickness=2)
chat_window.place(x=800, y=100)
chat_window.pack_propagate(0)
# entry_box=Text(chat_window, width=33, height=3,font=(20))
entry_box = Entry(chat_window, relief="solid", font=("default", 16), width=28)
entry_box.place(x=13, y=450)
# entry_box.insert(0, "Ask Me Anything")
entry_box.bind('<Return>', lambda event: threading())


def cancel():
    entry_box.delete(0, END)


cross_img = Image.open(r'Command_line\remove.png')
cross_img = cross_img.resize((20, 20))
cross_img = ImageTk.PhotoImage(cross_img)

cross = Button(chat_window, image=cross_img, command=cancel)
cross.place(x=352, y=451)

user_chat = Label(chat_window, text="", bg="#505050",
                  fg="#FFBF00", font=(23), pady=40, wraplength=350)
user_chat.pack()

bot_chat = Label(chat_window, text="Hello Buddy...",
                 bg="#505050", fg="#fff", font=(23), pady=40, wraplength=350,)

bot_chat.pack()

root.state("zoomed")
root.minsize(1280, 800)
root.maxsize(1280, 800)
root.mainloop()
