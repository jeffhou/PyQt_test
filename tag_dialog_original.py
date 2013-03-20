import tkinter as tk
import sys
def send():
	global new_tag
	new_tag = myEntryBox.get()
	print("FILE: "+" ".join(sys.argv[1:]))
	print("TAG: " + new_tag)
	root.destroy()
new_tag = ''
root = tk.Tk()
myEntryBox = tk.Entry(root)
myEntryBox.pack()

mySubmitButton = tk.Button(root, text='Submit', command=send)
mySubmitButton.pack()
root.mainloop()
input()