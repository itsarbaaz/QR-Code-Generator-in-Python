from tkinter import *
from PIL import ImageTk, Image
import qrcode

window= Tk()
window.title('QR Code Generator')

def my_click():
	canvas.delete("all")
	my_text=e2.get()
	img = qrcode.make(my_text)
	img.save('E:/CODING/Code/projects/QRCODE/images/'+e.get()+'.jpeg')

	my_button2 = Button(UI_frame, text='View QRCODE', command=myqrviewer)
	my_button2.grid(row=4, column=1, padx=30, pady=20)

def myqrviewer():
	global my_img1
	my_img1 = ImageTk.PhotoImage(Image.open('E:/CODING/Code/projects/QRCODE/images/'+e.get()+'.jpeg'))

	canvas.create_image(100,50, anchor=NW, image=my_img1)
	window.update_idletasks()

UI_frame=Frame(window, width=500, height=500)
UI_frame.grid(row=0, column=0)

l1=Label(UI_frame, text="Enter Title:")
l1.grid(row=0, column=0)

e=Entry(UI_frame, width=50)
e.grid(row=1, column=0, columnspan=3, padx=30, pady=20)

l2=Label(UI_frame, text="Enter URL:")
l2.grid(row=2, column=0)

e2=Entry(UI_frame, width=50)
e2.grid(row=3, column=0, columnspan=3, padx=30, pady=20)


b1= Button(UI_frame, text="Enter", command=my_click)
b1.grid(row=4, column=0, padx=30, pady=20)

b3= Button(UI_frame, text="Exit", command=window.quit)
b3.grid(row=4, column=2, padx=30, pady=20)

#b2= Button(UI_frame, text="Exit", command=window.quit)
#b2.grid(row=2, column=1)
w1=500
h1=400
canvas = Canvas(window, width=500, height=400)
canvas.grid(row=4, column=0, padx=10, pady=5)

window.mainloop()