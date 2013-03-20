import tkinter as tk
import sqlite3,os
import sys
def send():
	new_tags = myEntryBox.get().split(";")
	
	file_dir=" ".join(sys.argv[1:])
	root.destroy()
	cxn = sqlite3.connect('C:\\Python32\\PyQt_test\\tags.db')
	cur = cxn.cursor()
	for new_tag in new_tags:
		cur.execute('INSERT INTO filetags VALUES("'+file_dir+'","'+new_tag+'")')
	cur.close()
	cxn.commit()
	cxn.close()
def filter(event):
	if event.char=="\r":
		send()
root = tk.Tk()
root.geometry("100x40+"+str(int(root.winfo_screenwidth()/2)-50)+"+"+str(int(root.winfo_screenheight()/2)-20))
myEntryBox = tk.Entry(root)
myEntryBox.focus_set()
myEntryBox.pack()
print(myEntryBox.size())
root.bind("<Key>",filter)
mySubmitButton = tk.Button(root, text='Submit', command=send)
mySubmitButton.pack()
root.mainloop()
