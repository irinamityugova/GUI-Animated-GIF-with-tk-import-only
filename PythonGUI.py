import tkinter as tk

#GUI Frame
root = tk.Tk()
root.geometry('400x224')
root.title("GUI Animated GIF with tk import only")
frm = tk.Frame(root, background="dark blue", height="224", width="400").grid()

#GIF Initiation
img = tk.PhotoImage(file="image.gif", format = 'gif -index 0')
lbl = tk.Label(frm, background="gray", image=img)
lbl.grid(column=0, row=0)
imgCnt = 0

#GIF Image Iteration
def showGif(imgCnt=imgCnt):
    
    if imgCnt > 37:
        return
    nextimage = tk.PhotoImage(file="image.gif", format = 'gif -index ' + str(imgCnt))
    lbl.configure(image=nextimage)
    lbl.image = nextimage
    lbl.after(50, showGif, imgCnt+1)

#Iteration Call
showGif()

#GUI Playloop
root.mainloop()
