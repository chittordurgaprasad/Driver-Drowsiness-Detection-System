from tkinter import *
window = Tk()
window.geometry('1080x720')
window.title("Drowsiness Detection GUI")
window.configure(background="black")
header= Frame(window, bg ="black")
content=Frame(window, bg= "white")
footer= Frame(window, bg= "black")
window.columnconfigure(0,weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=8)
window.rowconfigure(2,weight=1)
header.grid(row=0, sticky="news")
content.grid(row=1, sticky="news")
footer.grid(row=2, sticky="news")
label = Label(header, text="Welcome to Driver Drowsiness Detection System",fg="white", bg="black")
label.pack(fill="y")
labelclick = Label(content, text="Click okay to display Camera", fg="black", bg="white")
labelclick.pack(fill="y")
labelclose = Label(content, text="After opening the GUI, press 'q' to quit",fg="black",bg="white")
labelclose.pack(fill="y")
def onclick():
	import subprocess
	subprocess.call("python dd.py", shell=True)

bt1 = Button(content,text="Okay",fg="black",bg="white",command=onclick)
bt1.pack(fill="x")
rights = Label(footer, text="Modelled by Junaid and his team", fg="white", bg="black")
rights.pack(fill="x")

window.mainloop()
