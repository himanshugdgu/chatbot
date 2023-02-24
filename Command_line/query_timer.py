import time
from tkinter import *
from tkinter import messagebox
from timer_calculator import get_timer

def timer1(query=None):
	if(query!=None):
		string = get_timer(query)
		hours =int(string[:2])
		mins = int(string[3:5])
		secs = int(string[6:8])
		temp = hours+mins+secs
	# creating Tk window
	root = Tk()

	# setting geometry of tk window
	root.geometry("300x250+1000+1000")

	# Using title() to display a message in
	# the dialogue box of the message in the
	# title bar.
	root.title("Time Counter")

	# Declaration of variables
	hour=StringVar()
	minute=StringVar()
	second=StringVar()

	# setting the default value as 0
	if(query==None):
		hour.set("00")
		minute.set("00")
		second.set("00")
	else:
		hour.set(hours)
		minute.set(mins)
		second.set(secs)

	# Use of Entry class to take input from the user
	hourEntry= Entry(root, width=3, font=("Arial",18,""),
					textvariable=hour)
	hourEntry.place(x=80,y=20)

	minuteEntry= Entry(root, width=3, font=("Arial",18,""),
					textvariable=minute)
	minuteEntry.place(x=130,y=20)

	secondEntry= Entry(root, width=3, font=("Arial",18,""),
					textvariable=second)
	secondEntry.place(x=180,y=20)


	def submit():
		try:
			
			temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
		except:
			print("Please connect to internet")
		while temp >-1:
			# if(query==None):
			# mins,secs = divmod(temp,60)
			# hours=0
			# if mins >60:
			# 	hours, mins = divmod(mins, 60)
			# else:

			hour.set("{0:2d}".format(hours))
			minute.set("{0:2d}".format(mins))
			second.set("{0:2d}".format(secs))

			# updating the GUI window after decrementing the
			# temp value every time
			root.update()
			time.sleep(1)

			# when temp value = 0; then a messagebox pop's up
			# with a message:"Time's up"
			if (temp == 0):
				messagebox.showinfo("Time Countdown", "Time's up ")
			
			# after every one sec the value of temp will be decremented
			# by one
			temp -= 1

	# button widget
	btn = Button(root, text='Set Time Countdown', bd='5',
				command= submit)
	btn.place(x = 70,y = 120)
	if(query!=None):
		submit()
	root.mainloop()
if __name__ == "__main__":
	timer1("set timer for 3 sec")
