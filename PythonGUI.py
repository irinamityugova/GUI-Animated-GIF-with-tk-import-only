from fileinput import filename
import tkinter as tk

root = tk.Tk()
root.geometry('300x200')
root.title("Irina's App")

frm = tk.Frame(root, background="dark blue", height="200", width="300").grid()

frameCnt = 36
frame = tk.PhotoImage(file="image.gif", format = 'gif -index 0')

lbl = tk.Label(frm, background="gray", image=frame , height="200", width="300")
lbl.grid(column=0, row=0)
frameCnt=0

def showGif(frameCnt):
    
    if frameCnt > 37:
        return
    print(">> frameCnt: "+str(frameCnt))
    frame = tk.PhotoImage(file="image.gif", format = 'gif -index ' + str(frameCnt))
    lbl.configure(image=frame)
    lbl.image = frame
    root.after(500, showGif(frameCnt+1))

"""def nextImg(i, frmt, max=37) :
        print("next")
        frmt = 'gif -index '+str(i)
        print(frmt)
        nextimage = tk.PhotoImage(file="image.gif", format = frmt)
        lbl.configure(image=nextimage)
        root.after(200, nextImg, i+1, label)
        if i==max : return"""

"""def animate(i, max=37, label=lbl) :
        img = tk.PhotoImage(file="image.gif", format = 'gif -index '+str(i))
        #label.configure(image = tk.PhotoImage(file="image.gif", format = 'gif -index 20'))
        
        print(">> iteration: "+str(i))
        print("label: " + str(label))
        print("img: " + str(img))

        if i==max : return print("done")
        root.after(200, animate, i+1, label)
"""
root.after(500, showGif, frameCnt+1)
root.mainloop()

