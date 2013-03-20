import sqlite3,os

cxn = sqlite3.connect('tags.db')
cur = cxn.cursor()
try:
	cur.execute('CREATE TABLE filetags(file_path VARCHAR(255), tag VARCHAR(20))')
except:
	pass
control=0
#try:
while control!=-1:
	print("1) TAG A FILE")
	print("2) LIST TAGS")
	print("3) LIST FILES")
	print("4) FIND FILES BY SINGLE TAG")
	print("5) FIND FILES BY TAGS")
	print("6) CLEAR DATABASE")
	print("-1) QUIT")
	control=int(input("$ "))
	if control==1:
		file_dir=input("FILE$ ")
		tag=input("TAG$ ")
		cur.execute('INSERT INTO filetags VALUES("'+file_dir+'","'+tag+'")')
cur.close()
cxn.commit()
cxn.close()