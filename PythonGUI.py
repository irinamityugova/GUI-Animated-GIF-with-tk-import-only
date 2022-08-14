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

def animate(i, max=37) :
    for i in range(frameCnt) : 
        frame = tk.PhotoImage(file="image.gif", format = 'gif -index '+str(i))
        lbl.configure(image = frame)
        print(i, str(frame))
        return

root.after(500, animate, 0)
root.mainloop()
