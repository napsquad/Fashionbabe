from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()


def retrieve_input():
    onput = textEntry.get("1.0",'end-1c')
    textDisplay.insert("1.0", "<user placeholder>: " + onput + "\n")


bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

textEntry = Text(frame, bg="Red", height=10)
textEntry.pack(side=BOTTOM)

coin_count = Label(frame, text="coin count : " + "<count placeholder>")
coin_count.pack(side=TOP)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

textDisplay = Text(frame, bg="Blue")
textDisplay.pack(side=TOP)

userLbl = Label(frame, bg="Purple", text="<USER : user>", width=10)
userLbl.pack(side=RIGHT)

sendButton = Button(frame, text="Send Message", command=retrieve_input)
sendButton.pack(side=LEFT)

chatRoom = Label(frame, bg="Yellow", text="<chatroom name: <placeholder>>")
chatRoom.pack(side=RIGHT)


root.mainloop()